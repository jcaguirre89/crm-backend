from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import (
    ContactSerializer,
    ContactNoteSerializer,
    DealSerializer,
    DealNoteSerializer,
)
from .models import Deal, Contact, DealNote, ContactNote


class ContactViewSet(viewsets.ModelViewSet):
    """ Contact CRUD """

    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Contacts.objects.all()
        deal_pk = self.request.query_params.get('deal', None)
        if deal_pk is not None:
            queryset = queryset.filter(deal__pk=deal_pk)
        return queryset


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


class DealNoteViewSet(viewsets.ModelViewSet):
    """ DealNote CRUD """

    serializer_class = DealNoteSerializer
    model = DealNote
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DealNote.objects.filter(deal=self.kwargs["deal_pk"])
