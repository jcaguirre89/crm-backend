from .models import Company, Deal, Contact, CompanyNote, DealNote, ContactNote
from rest_framework import serializers


class CompanyNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyNote
        fields = ["id", "title", "content"]


class DealNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealNote
        fields = ["id", "title", "content"]


class ContactNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactNote
        fields = ["id", "title", "content"]


class CompanySerializer(serializers.ModelSerializer):
    notes = CompanyNoteSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ["id", "name", "country", "industry", "user", "notes"]


class DealSerializer(serializers.ModelSerializer):
    notes = DealNoteSerializer(many=True, read_only=True)

    class Meta:
        model = Deal
        fields = ["id", "company", "user", "country", "industry", "status", "notes"]


class ContactSerializer(serializers.ModelSerializer):
    notes = ContactNoteSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = ["id", "company", "user", "name", "email", "linkedin", "notes"]
