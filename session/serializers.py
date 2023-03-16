from rest_framework import serializers

from .models import Match, Participation, TrainingSession


class MatchSerializer(serializers.ModelSerializer):
    team_name = serializers.SerializerMethodField()
    opponent_name = serializers.SerializerMethodField()
    infrastructure_name = serializers.SerializerMethodField()
    players_names = serializers.SerializerMethodField()
    players_fullnames = serializers.SerializerMethodField()

    class Meta:
        model = Match
        fields = "__all__"

    @staticmethod
    def get_players_names(obj):
        return [player.username for player in obj.players.all()]

    @staticmethod
    def get_players_fullnames(obj):
        return [f"{player.first_name} {player.last_name}" for player in obj.players.all()]

    @staticmethod
    def get_team_name(obj):
        return obj.team_name

    @staticmethod
    def get_opponent_name(obj):
        return obj.opponent_name

    @staticmethod
    def get_infrastructure_name(obj):
        return obj.infrastructure_name


class ParticipationSerializer(serializers.ModelSerializer):
    player_nickname = serializers.SerializerMethodField()
    player_fullname = serializers.SerializerMethodField()
    match_code = serializers.SerializerMethodField()
    role_display = serializers.SerializerMethodField()

    class Meta:
        model = Participation
        fields = "__all__"

    @staticmethod
    def get_player_nickname(obj):
        return obj.player_nickname

    @staticmethod
    def get_player_fullname(obj):
        return obj.player_fullname

    @staticmethod
    def get_match_code(obj):
        return obj.match_code

    @staticmethod
    def get_role_display(obj):
        return obj.role_display


class TrainingSessionSerializer(serializers.ModelSerializer):
    team_name = serializers.SerializerMethodField()
    sport_name = serializers.SerializerMethodField()
    facility_name = serializers.SerializerMethodField()

    class Meta:
        model = TrainingSession
        fields = "__all__"

    @staticmethod
    def get_team_name(obj):
        return obj.team_name

    @staticmethod
    def get_sport_name(obj):
        return obj.sport_name

    @staticmethod
    def get_facility_name(obj):
        return obj.facility_name
