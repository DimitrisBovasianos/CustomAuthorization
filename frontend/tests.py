from django.test import TestCase
from rest_framework.test import APIRequestFactory,APITestCase
from .models import MyUser
from .views import *
from rest_framework.test import force_authenticate

class Cases(APITestCase):
  
    def setUp(self):
        self.user = MyUser.objects.create_user(username='dimi',email='thahe@gmail.com')
        self.user.set_password('king2306')
        self.user.save()



    def test_login(self):
        view = Home.as_view()
        factory = APIRequestFactory()
        request = factory.get('/')
        force_authenticate(request,self.user)
        response = view(request)
        self.assertEqual(response.status_code, 200)
