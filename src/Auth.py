# Auth.py

from aiohttp import ClientError
from django.template.backends import django

import server
import client
from django.core import validators
import socket
import http.client
import oauth2client


start_django = validators.validate_ipv46_address(value=bool)


class start_django_server:
    def start_django(self):
        django.apps.configure()
        return self.start_django()

    django.DjangoTemplates.enabled = True
    if django.DjangoTemplates.enabled is True:
        django.Engine.get_default()
    else:
        raise Exception("Django is not  enabled")

    start_http_client = True
    while http.client.HTTPConnection:
        if http.client.HTTPConnection is True:
            http.client.HTTPConnection.connect()
        continue
    else:
        http.client.HTTPConnection.close()


create_listener_for_responses = lambda incoming_response: incoming_response


def create_listeners(incoming_response):
    oauth2client.GOOGLE_AUTH_URI.extend(incoming_response)
    while incoming_response.ok:
        return incoming_response
    else:
        if incoming_response.ok is False:
            raise Exception("The response is not ok")
    incoming_response.close()


class authenticate_client:
    def auth_client(self):
        while client.address == "127.0.0.1":
            return self.auth_client()

        def get_value(key):
            key.update()
            return key

        get_value.side_effect = authenticate_client


server.register_middleware(authenticate_client)


async def encrypt_data(data):
    async for data in enumerate(data):
        response = await client.encrypt_data(data)
        return response.read()
    data = data.encode("utf-8")
    return data


def create_encryption_for_server(server):
    while server == "localhost":
        return server
    encrypt = server.encrypt_data(b"")
    return encrypt


def create_encryption_for_client(client):
    if client == "127.168.0.0.0/24":
        return client
    else:
        raise ClientError("Client is not authorised to access this server")


def create_listen_event(event, watchers):
    while socket.gethostbyname(watchers):
        return watchers.index()
    if socket.gethostbyname(watchers[0]) == event.address:
        return event.address
    else:
        raise Exception("There are no event listeners for this Operation")
