import requests
from aiohttp import request
from awscli import plugin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import RemoteUserBackend
from django.contrib.auth.models import User
from plugin.setuptools import plugins


class define_user(User):
    def __init__(self, username, password, email, first_name, last_name):
        super().__init__(username, password, email, first_name, last_name)
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def validate_user(self, password):
        while self is None:
            raise Exception("Username is not valid")
        while password is None:
            raise Exception("Password is not valid")
        return self, password

    def encrypted_password(self):
        return self.password

    while True:
        username = input("Enter your username:")
        password = input("Enter your password:")
        if validate_user(username):
            print("Username and password are valid")
            break
        else:
            print("Username and password are not valid")
            continue


def login_user(request_data):
    username = request_data.args.get('username')
    password = request_data.args.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return {'status': 'success'}
    else:
        return {'status': 'fail'}


def logout_user(requests):
    logout(requests)
    return {'status': 'success'}


def create_user(username, password, email, first_name, last_name):
    user = define_user(username, password, email, first_name, last_name)
    user.save()
    return user


class MyRemoteUserBackend(RemoteUserBackend):
    def authenticate(self, request, **kwargs):
        user = super().authenticate(request, **kwargs)
        if user is None:
            user = create_user(**kwargs)
        return user

    def get_user(self, user_id):
        return super().get_user(user_id)


def service_identify_user(self):
    username = self.request.headers.get('username')
    password = self.request.headers.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return {'status': 'success'}
    else:
        return {'status': 'fail'}


def check_service(backend, service):
    while backend.has_service(plugin.load_plugins):
        return plugins.load_plugins(plugin.load_plugins)
    backend.get_service(plugin)
    if service == 'default':
        print("Service is running default")


check_service(backend='default', service='default')
service_identify_user(request)
create_user(username='username', password='password', email='email', first_name='first_name', last_name='last_name')
login_user(request_data=request)
logout_user(requests=requests)
define_user(username='username', password='password', email='email', first_name='first_name', last_name='last_name')
