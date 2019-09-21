from rest_framework import viewsets
from .serializers import (CompanySerializer, CompanyNoteSerializer,
                          ContactSerializer, ContactNoteSerializer,
                          DealSerializer, DealNoteSerializer)
from .models import Company, Deal, Contact, CompanyNote, DealNote, ContactNote


class CompanyViewSet(viewsets.ModelViewSet):
    """ Company CRUD """
    serializer_class = CompanySerializer
    model = Company


class CompanyNoteViewSet(viewsets.ModelViewSet):
    """ CompanyNote CRUD """
    serializer_class = CompanyNoteSerializer
    model = CompanyNote


class ContactViewSet(viewsets.ModelViewSet):
    """ Contact CRUD """
    serializer_class = ContactSerializer
    model = Contact


class ContactNoteViewSet(viewsets.ModelViewSet):
    """ ContactNote CRUD """
    serializer_class = ContactNoteSerializer
    model = ContactNote


class DealViewSet(viewsets.ModelViewSet):
    """ Deal CRUD """
    serializer_class = DealSerializer
    model = Deal


class DealNoteViewSet(viewsets.ModelViewSet):
    """ DealNote CRUD """
    serializer_class = DealNoteSerializer
    model = DealNote


class CompanyViewSet(viewsets.ModelViewSet):
    """ Company CRUD """
    serializer_class = CompanySerializer
    model = Company
