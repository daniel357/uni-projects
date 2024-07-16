from collections import OrderedDict
from typing import Any

from django.contrib.auth.models import User

from base import serializers
from base.models.UserProfile import UserProfile
from base.serializers.UserSerializer import UserSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = (
            "user",
            "u_first_name",
            "u_last_name",
            "u_date_of_birth",
            "u_bio",
            "u_location",
            "activation_code",
            "activation_expiry_date",
            "active",
        )

    def create(self, validated_data: OrderedDict[str, Any]) -> UserProfile:
        user_data = validated_data.pop("user")
        user_data['is_active'] = False
        user = User.objects.create_user(**user_data)
        user_profile = UserProfile.objects.create(user=user, **validated_data)
        return user_profile


class UserProfileDetailSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    # tennis_player_count = serializers.IntegerField()
    # coach_count = serializers.IntegerField()
    # tournament_count = serializers.IntegerField()

    def get_username(self, user_profile: UserProfile) -> str:
        return user_profile.user_id  # type: ignore

    class Meta:
        model = UserProfile
        fields = (
            "username",
            "u_first_name",
            "u_last_name",
            "u_date_of_birth",
            "u_bio",
            "u_location",
            "tennis_player_count",
            "coach_count",
            "tournament_count",
        )