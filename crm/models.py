from enum import Enum, unique
from django.db import models


@unique
class BaseChoices(Enum):
    @property
    def as_tuple(self):
        """ return tuple of single item for django choices """
        return self.value, self.name

    @classmethod
    def choices(cls):
        """ return full tuple for choices """
        return tuple(item.as_tuple for item in list(cls))


class Country(BaseChoices):
    CHILE = "Chile"
    COLOMBIA = "Colombia"
    PERU = "Peru"


class Industry(BaseChoices):
    FORESTRY = "Forestry"
    ACUICULTURE = "Acuiculture"
    MINING = "Mining"


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Company(TimeStampedModel):
    name = models.CharField(max_length=1000)
    country = models.CharField(
        max_length=1000, choices=Country.choices(), default=Country.CHILE
    )
    industry = models.CharField(
        max_length=1000, choices=Industry.choices(), default=Industry.MINING
    )
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Deal(TimeStampedModel):

    RADAR = "radar"
    PROSPECT = "prospect"
    DUE_DILIGENCE = "due diligence"
    CLOSED = "closed"
    EXITED = "exited"
    REJECTED = "rejected"

    STATUS_CHOICES = (
        (RADAR, "Radar"),
        (PROSPECT, "Prospect"),
        (DUE_DILIGENCE, "Due DIligence"),
        (CLOSED, "Closed"),
        (EXITED, "Exited"),
        (REJECTED, "Rejected"),
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="deals")
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="deals"
    )
    country = models.CharField(
        max_length=1000, choices=Country.choices(), default=Country.CHILE
    )
    industry = models.CharField(
        max_length=1000, choices=Industry.choices(), default=Industry.MINING
    )
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=RADAR)

    def __str__(self):
        return f"Deal on {self.company.name}"


class Contact(TimeStampedModel):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=200, blank=True)
    linkedin = models.CharField(max_length=200, blank=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="contacts"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="contacts"
    )


class BaseNote(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        abstract = True


class CompanyNote(BaseNote):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="company_notes"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="company_notes"
    )


class ContactNote(BaseNote):
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, related_name="contact_notes"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="contact_notes"
    )


class DealNote(BaseNote):
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, related_name="deal_notes")
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="deal_notes"
    )
