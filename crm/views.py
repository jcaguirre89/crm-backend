from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import (
    CompanySerializer,
    CompanyNoteSerializer,
    ContactSerializer,
    ContactNoteSerializer,
    DealSerializer,
    DealNoteSerializer,
)
from .models import Company, Deal, Contact, CompanyNote, DealNote, ContactNote


class CompanyViewSet(viewsets.ModelViewSet):
    """ Company CRUD """

    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [IsAuthenticated]


class CompanyNoteViewSet(viewsets.ModelViewSet):
    """ CompanyNote CRUD """

    serializer_class = CompanyNoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CompanyNote.objects.filter(company=self.kwargs["company_pk"])


class ContactViewSet(viewsets.ModelViewSet):
    """ Contact CRUD """

    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contact.objects.filter(company=self.kwargs["company_pk"])


class ContactNoteViewSet(viewsets.ModelViewSet):
    """ ContactNote CRUD """

    serializer_class = ContactNoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ContactNote.objects.filter(contact=self.kwargs["contact_pk"])


class DealViewSet(viewsets.ModelViewSet):
    """ Deal CRUD """

    serializer_class = DealSerializer
    model = Deal
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Deal.objects.filter(company=self.kwargs["company_pk"])


class DealNoteViewSet(viewsets.ModelViewSet):
    """ DealNote CRUD """

    serializer_class = DealNoteSerializer
    model = DealNote
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DealNote.objects.filter(deal=self.kwargs["deal_pk"])
