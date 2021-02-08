import jwt
from core.serializers import UserSerializer
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework_jwt.utils import jwt_payload_handler
from django.contrib.auth.models import User
from core.models import Client, Seller
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login, logout
from django.http.response import Http404, JsonResponse

# Create views


def index(request):
    return redirect('/admin/')


'''
@login_required(login_url='/admin/')
def json_submit_client(request, id_client, id_profile):
    if request.POST:
        name = request.POST.get('Nome')
        email = request.POST.get('Email')
        location = request.POST.get('Localização')
        role = request.POST.get('Atribuição')
        creationDate = request.POST.get('Data de Entrada')
        attDate = request.POST.get('Última atualização')
        profile = request.user
        if id_client:
            client = Client.objects.get(id=id_profile)
            if client.profile == profile:
                client.name = name
                client.email = email
                client.location = location
                client.role = role
                client.creationDate = creationDate
                client.attDate = attDate
                client.save()
        else:
            Client.objects.create(name=name,
                                  email=email,
                                  location=location,
                                  role=role,
                                  creationDate=creationDate,
                                  attDate=attDate,
                                  profile=profile)
    return redirect('/')
'''

'''
@login_required(login_url='/admin/')
def json_submit_seller(request, id_profile):
    if request.POST:
        name = request.POST.get('Nome')
        email = request.POST.get('Email')
        location = request.POST.get('Localização')
        role = request.POST.get('Atribuição')
        creationDate = request.POST.get('Data de Entrada')
        attDate = request.POST.get('Última atualização')
        profile = request.user
        if Seller:
            seller = Seller.objects.get(id=id_profile)
            if seller.profile == profile:
                seller.name = name
                seller.email = email
                seller.location = location
                seller.role = role
                seller.creationDate = creationDate
                seller.attDate = attDate
                seller.save()
        else:
            Seller.objects.create(name=name,
                                  email=email,
                                  location=location,
                                  role=role,
                                  creationDate=creationDate,
                                  attDate=attDate,
                                  profile=profile)
    return redirect('/')
'''


@login_required(login_url='/admin/')
def json_delete_client(request, id_profile):
    profile = request.user
    try:
        client = Client.objects.get(id=id_profile)
    except Exception:
        raise Http404()
    if profile == client.profile:
        client.delete()
    else:
        raise Http404()
    return redirect('/')


@login_required(login_url='/admin/')
def json_delete_seller(request, id_profile):
    profile = request.user
    try:
        seller = Seller.objects.get(id=id_profile)
    except Exception:
        raise Http404()
    if profile == seller.profile:
        seller.delete()
    else:
        raise Http404()
    return redirect('/')


def json_comercial_client(request, id_profile):
    profile = User.objects.get(id=id_profile)
    client = Client.objects.filter(profile=profile).values('profile', 'name', 'email', 'location', 'role', 'creationDate',
                                                           'attDate')
    return JsonResponse(list(client), safe=False)


@login_required(login_url='/admin/')
def json_comercial_seller(request, id_profile):
    profile = User.objects.get(id=id_profile)
    seller = Seller.objects.filter(profile=profile).values('profile', 'name', 'email', 'location', 'role', 'creationDate',
                                                           'attDate')
    return JsonResponse(list(seller), safe=False)


class CreateUserAPIView(APIView):
    # Allow any user (authenticated or not) to access this url
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):

    # Allow only authenticated users to access this url
    permission_classes = (IsAuthenticated,)  # (AllowAny,)
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        serializer = UserSerializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):

    try:
        username = request.data['username']
        password = request.data['password']

        user = User.objects.get(username=username, password=password)
        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = {}
                user_details['name'] = "%s %s" % (
                    user.first_name, user.last_name)
                user_details['token'] = token
                user_logged_in.send(sender=user.__class__,
                                    request=request, user=user)
                return Response(user_details, status=status.HTTP_200_OK)

            except Exception as e:
                raise e
        else:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'error': 'please provide a email and a password'}
        return Response(res)
