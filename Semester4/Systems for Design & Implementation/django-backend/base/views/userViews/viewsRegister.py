from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from rest_framework import status
from datetime import datetime, timedelta
import pytz
import random
import string

from base.models.UserProfile import UserProfile

User = get_user_model()


@api_view(['POST'])
def register(request):
    # check if the username is provided and not empty
    username = request.data.get('user', {}).get('username')
    if not username:
        return Response({'error': 'Username must be set'},
                        status=status.HTTP_400_BAD_REQUEST)

    password = request.data.get('user', {}).get('password')

    # check if the username is already taken
    if User.objects.filter(username=username).exists():
        return Response({'username': 'Username already taken'},
                        status=status.HTTP_400_BAD_REQUEST)

    # validate password
    # try:
    #     validate_password(password)
    # except ValidationError as e:
    #     return Response({'password': e.messages},
    #                     status=status.HTTP_400_BAD_REQUEST)

    # create new user
    user = User.objects.create_user(username=username,
                                    password=password,
                                    is_active=False)

    # generate confirmation code
    confirmation_code = ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=12))

    # set confirmation code valid until 10 minutes from now
    confirmation_code_valid_until = datetime.now(
        pytz.utc) + timedelta(minutes=10)

    # store confirmation code and its validity time in user profile table
    user_profile = UserProfile.objects.create(
        confirmation_code=confirmation_code,
        confirmation_code_valid_until=confirmation_code_valid_until,
        user_id=user)

    # send the confirmation code to the frontend
    return Response({'confirmation_code': confirmation_code})
