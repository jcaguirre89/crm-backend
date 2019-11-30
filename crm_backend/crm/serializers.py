from .models import Deal, Contact, DealNote, ContactNote, Checklist
from rest_framework import serializers


class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist
        fields = '__all__'


class DealNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealNote
        fields = ["id", "title", "content"]


class ContactNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactNote
        fields = ["id", "title", "content"]


class DealSerializer(serializers.ModelSerializer):
    notes = DealNoteSerializer(many=True, read_only=True)

    class Meta:
        model = Deal
        fields = ["id", "user", "country", "industry", "status", "notes"]


class ContactSerializer(serializers.ModelSerializer):
    notes = ContactNoteSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = ["id", "deal", "user", "first_name", "last_name", "email", "linkedin", "notes"]
