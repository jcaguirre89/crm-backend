from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response
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
    permission_classes = []
    queryset = Deal.objects.all()

    def create(self, request, *args, **kwargs):
        data = dict(**request.data, user=request.user.pk)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DealNoteViewSet(viewsets.ModelViewSet):
    """ DealNote CRUD """

    serializer_class = DealNoteSerializer
    model = DealNote
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DealNote.objects.filter(deal=self.kwargs["deal_pk"])
