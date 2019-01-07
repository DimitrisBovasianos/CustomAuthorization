from frontend.models import MyUser
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from urllib import parse
from urllib import request as requestalter
import json
from django.conf import settings

class MyAuthentication(object):

    def authenticate(self,request,username,password):
        creds = {'client_id':'<cliend_id>','client_secret':'client_secret','grant_type':'password','username':username,'password':password}
        creds = parse.urlencode(creds).encode()
        url = 'http://127.0.0.1:8000/o/token/'
        req = requestalter.Request(url,creds)
        resp = requestalter.urlopen(req)
        raw_data  = resp.read()
        json_data = raw_data.decode('utf-8')
        data = json.loads(json_data)
        token = data['access_token']
        if token:
            string = 'Bearer {}'.format(token)
            request.session.set_expiry(data['expires_in])
            request.session['refresh_token'] = data['refresh_token']
            user = MyUser.objects.get(username=username)
            return user
        else:
            return None
    def get_user(self, user_id):
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            return None

    def has_perm(self, user_obj, perm, obj=None):
        return user_obj.username == settings.ADMIN_LOGIN

