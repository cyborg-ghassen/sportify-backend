from rest_framework import serializers

from .models import Sport, Equipment, Venue, TrainingRoom, Infrastructure


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = "__all__"


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = "__all__"


class VenueSerializer(serializers.ModelSerializer):
    sport_label = serializers.SerializerMethodField()

    class Meta:
        model = Venue
        fields = "__all__"

    @staticmethod
    def get_sport_label(obj):
        return obj.sport_label


class TrainingRoomSerializer(serializers.ModelSerializer):
    equipments_label = serializers.SerializerMethodField()
    venue_name = serializers.SerializerMethodField()
    venue_sport = serializers.SerializerMethodField()

    class Meta:
        model = TrainingRoom
        fields = "__all__"

    @staticmethod
    def get_equipments_label(obj):
        return [eq.label for eq in obj.equipments.all()]

    @staticmethod
    def get_venue_name(obj):
        return obj.venue_name

    @staticmethod
    def get_venue_sport(obj):
        return obj.venue_sport


class InfrastructureSerializer(serializers.ModelSerializer):
    equipments_label = serializers.SerializerMethodField()
    type_display = serializers.SerializerMethodField()

    class Meta:
        model = Infrastructure
        fields = "__all__"

    @staticmethod
    def get_equipments_label(obj):
        return [eq.label for eq in obj.equipments.all()]

    @staticmethod
    def get_type_display(obj):
        return obj.type_display
