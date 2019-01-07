from django.contrib.auth import logout
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from django.contrib import auth
from urllib import parse
from urllib import request as requestalter
import json
from django.utils import timezone

def get_user(request):
    if not hasattr(request, '_cached_user'):
        request._cached_user = auth.get_user(request)
    return request._cached_user



class CustomMiddleware(MiddlewareMixin):

    def process_request(self,request):
        request.user = SimpleLazyObject(lambda: get_user(request))
        user = request.user
        session_expriry_date = request.session.get_expiry_date()
        now = timezone.now()
        seconds_left = (session_expriry_date-now).total_seconds()
        print(seconds_left)
        time = "00:00:20"
        prefered_time=sum(x * int(t) for x, t in zip([3600, 60, 1], time.split(":")))
        if user.is_authenticated and seconds_left<prefered_time:
            token = request.session['refresh_token']
            print(token)
            creds = {'grant_type':'refresh_token','client_id':'yD8oVDsbfip7yZLqqBeMGf1AYRwvRF2CzudzzqM9','client_secret':'Et427gqwkzMdNGiJKUa1UaChYBlbXffvmNBKaT0ue7eCjepai7D8rTltbwwcGLksIw5WikVLVVK9pOAvh8AwnNzRlzSOF2MTAXkku1qWeJUDDVke8XM7kt58C8OJMuOC','refresh_token':token}
            creds = parse.urlencode(creds).encode()
            url = 'http://127.0.0.1:8000/o/token/'
            req = requestalter.Request(url,creds)
            resp = requestalter.urlopen(req)
            raw_data  = resp.read()
            request.session.set_expiry(3600)
            return
        elif seconds_left==0:
            logout(request)
            return None
        else:
            return
