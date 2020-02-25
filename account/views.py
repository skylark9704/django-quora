from django.http import HttpResponse
from django.shortcuts import redirect, render
from google.oauth2 import id_token
from google.auth.transport import requests
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from account.models import Auth
import google_auth_oauthlib.flow


# Create your views here.
def index(request):

    CLIENT_SECRET = './secret.json'
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRET, ['https://www.googleapis.com/auth/userinfo.email',
                        'https://www.googleapis.com/auth/userinfo.profile',
                        'openid']
    )

    flow.redirect_uri = 'http://localhost:8000/account/oauth/callback'

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )

    return redirect(authorization_url)


def oauth(request):
    print(request.path)
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        './secret.json',
        scopes=['https://www.googleapis.com/auth/userinfo.email',
                'https://www.googleapis.com/auth/userinfo.profile', 'openid'],
        state=request.GET.get('state'))
    flow.redirect_uri = "http://localhost:8000/account/oauth/callback"

    authorization_response = request.get_full_path()
    token = flow.fetch_token(authorization_response=authorization_response)
    try:
        idinfo = id_token.verify_oauth2_token(
            token['id_token'],
            requests.Request(),
            '720083099513-rr2vib357lnpto3i9rgrda7hgd1mk67m'
            + '.apps.googleusercontent.com'
        )
        if idinfo['iss'] not in ['accounts.google.com',
                                 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        newLogin = get(User.objects.filter(email=idinfo['email']), 0)

        newAuth = get(Auth.objects.filter(user=newLogin), 0)
        if(newAuth):
            print('User Exists, Logging In')
            login(
                request,
                newLogin,
                backend='django.contrib.auth.backends.ModelBackend'
            )
            response = redirect('/home/')
            return response
        else:
            print('New User, Creating User and Logging In')
            user = User(
                first_name=idinfo['given_name'],
                last_name=idinfo['family_name'],
                email=idinfo['email'],
                username=idinfo['name']
            )

            user.save()

            auth = Auth(
                user=user,
                sub=idinfo['sub'],
                display_picture_url=idinfo['picture']
            )
            auth.save()
            login(request, user)
            response = redirect('/home/')
            return response
    except ValueError:
        print('Failed Verification')
        # Invalid token
        return HttpResponse('Verification Failed')


def signout(request):
    logout(request)
    return redirect('/home/')


def profile(request):

    return render(request, 'account/profile.html')


def get(l, index, default=False):
    try:
        return l[index]
    except IndexError:
        return default
