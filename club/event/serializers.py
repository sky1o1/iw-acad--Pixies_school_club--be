from rest_framework import serializers
from club.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_title', 'event_description', 'event_date', 'created_by']

    def create(self, validated_data):
        event = Event(
            event_title=self.validated_data['event_title'],
            event_description=self.validated_data['event_description'],
            event_date=self.validated_data['event_date'],
            created_by=self.validated_data['created_by'],

        )

        event.save()
        return event


class ViewEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'event_title', 'event_description', 'event_date', 'created_by']
