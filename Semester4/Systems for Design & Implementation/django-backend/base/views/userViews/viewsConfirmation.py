from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from rest_framework import status

from django.urls import reverse
from datetime import datetime
import pytz

from base.models.UserProfile import UserProfile

User = get_user_model()


@api_view(['GET'])
def confirm(request):
    # get the confirmation code from the query parameters
    confirmation_code = request.query_params.get('confirmation_code', None)

    # get the username from the query parameters
    username = request.query_params.get('username', None)

    # check if there is an account with the given username and confirmation code
    try:
        # get the user and the profile
        user = User.objects.get(username=username)
        user_profile = UserProfile.objects.get(
            user_id_id=user.id, confirmation_code=confirmation_code)
        expiration_time = user_profile.confirmation_code_valid_until

        # check if the confirmation code is still valid
        if datetime.now(pytz.utc) > expiration_time:
            return Response({'message': 'Confirmation code expired.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # if all good activate the account
        user.is_active = True
        user.save()

        return Response({'message': 'Account activated.'},
                        status=status.HTTP_200_OK)
    except:
        return Response(
            {'message': 'Invalid confirmation link. Please try again.'},
            status=status.HTTP_400_BAD_REQUEST)
