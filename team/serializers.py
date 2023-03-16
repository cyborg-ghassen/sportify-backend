from rest_framework import serializers

from .models import Team, TeamMembership


class TeamSerializer(serializers.ModelSerializer):
    member_nicknames = serializers.SerializerMethodField()
    member_fullnames = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = "__all__"

    @staticmethod
    def get_member_nicknames(obj):
        return [member.username for member in obj.members.all()]

    @staticmethod
    def get_member_fullnames(obj):
        return [f"{member.first_name} {member.last_name}" for member in obj.members.all()]


class TeamMembershipSerializer(serializers.ModelSerializer):
    team_name = serializers.SerializerMethodField()
    member_nickname = serializers.SerializerMethodField()
    member_fullname = serializers.SerializerMethodField()

    class Meta:
        model = TeamMembership
        fields = "__all__"

    @staticmethod
    def get_team_name(obj):
        return obj.team_name

    @staticmethod
    def get_member_nickname(obj):
        return obj.member_nickname

    @staticmethod
    def get_member_fullname(obj):
        return obj.member_fullname
