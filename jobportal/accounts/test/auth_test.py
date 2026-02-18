from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse


class LoginApiTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='sanjay',
            email='sanjay@gmail.com',
            password='sanjay'
        )

        self.login_url = reverse('login')
        self.sign_url=reverse('signup')
        self.logout_url=reverse('logout')
    def test_login_success(self):

        data = {
            'username': 'sanjay',
            'password': 'sanjay',
        }

        response = self.client.post(self.login_url, data)

        self.assertEqual(response.status_code, status.HTTP_102_PROCESSING) #sameple
        self.assertEqual(response.data['message'], "login sucessfully")

    def test_login_failed(self):
        data={
            'username':'vedha',
            'password':'vedha'
        }

        response=self.client.post(self.login_url,data)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['message'],'invalid credentials')

    
    def test_signup_success(self):
        data={
            'username':'vedha',
            'email':'vedha@gmail.com',
            'password':'vedha',
            "confirm_password":'vedha'
        }

        response=self.client.post(self.sign_url,data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'],"User Register Sucessfully")

    def test_signup_existsusername(self):
        data={
            'username':'sanjay',
            'email':'sample@gmail.com',
            'password':'sanjay',
            "confirm_password":'sanjay'
        }
        response=self.client.post(self.sign_url,data)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'][0],"A user with that username already exists.")

    def test_signup_existsemail(self):
        data={
            'username':'vedha',
            'email':'sanjay@gmail.com',
            'password':'sanjay',
            "confirm_password":'sanjay'
        }
        response=self.client.post(self.sign_url,data)
        
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'][0],"A user with that email already exists.")
    def test_password_not_match(self):
        data={
            'username':'vedha',
            'email':'new@gmail.com',
            'password':'sanjay',
            "confirm_password":'new'
        }
        response=self.client.post(self.sign_url,data)
        self.assertEqual(response.data['password'][0],"password does not match")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)


    def test_logout_success(self):
        login_response=self.client.post(self.login_url,{
            'username':'sanjay',
            'password':'sanjay'
        })
        refresh_token=login_response.data['refresh']
        response=self.client.post(self.logout_url,{
            'refresh':refresh_token
        })

        self.assertEqual(response.status_code,status.HTTP_205_RESET_CONTENT)

    def test_logout_failed(self):
        login_response=self.client.post(self.login_url,{
            'username':'sanjay',
            'password':'sanjay'
        })
        refresh_token=login_response.data['refresh']
        response=self.client.post(self.logout_url)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)