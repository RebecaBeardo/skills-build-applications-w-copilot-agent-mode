from bson import ObjectId
from rest_framework import serializers

from .models import Activity, LeaderboardEntry, Team, UserProfile, Workout


def stringify_object_ids(data):
    if isinstance(data, ObjectId):
        return str(data)
    if isinstance(data, dict):
        return {key: stringify_object_ids(value) for key, value in data.items()}
    if isinstance(data, list):
        return [stringify_object_ids(item) for item in data]
    return data


class ObjectIdSafeModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return stringify_object_ids(representation)


class TeamSerializer(ObjectIdSafeModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class UserProfileSerializer(ObjectIdSafeModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class ActivitySerializer(ObjectIdSafeModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class LeaderboardEntrySerializer(ObjectIdSafeModelSerializer):
    class Meta:
        model = LeaderboardEntry
        fields = '__all__'


class WorkoutSerializer(ObjectIdSafeModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'
