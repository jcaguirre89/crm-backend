from enum import Enum, unique
from django.db import models
from django.utils import timezone


@unique
class BaseChoices(Enum):
    """

    Usage:
    class Country(BaseChoices):
        CHILE = "Chile"
        COLOMBIA = "Colombia"
        PERU = "Peru"

    # Then in another model
    class Company(models.model):
        name = models.CharField(max_length=1000)
        country = models.CharField(
            max_length=1000, choices=Country.choices(), default=Country.CHILE
        )
    """

    @property
    def as_tuple(self):
        """ return tuple of single item for django choices """
        return self.value, self.name

    @classmethod
    def choices(cls):
        """ return full tuple for choices """
        return tuple(item.as_tuple for item in list(cls))


class Country(models.Model):
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Industry(models.Model):
    class Meta:
        verbose_name = 'Industry'
        verbose_name_plural = 'Industries'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Status(models.Model):
    class Meta:
        verbose_name_plural = 'Statuses'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class IC_Member(models.Model):
    class Meta:
        verbose_name = 'IC Member'
        verbose_name_plural = 'IC Members'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Deal(TimeStampedModel):
    name = models.CharField(max_length=1000)
    description = models.TextField(blank=True)
    # TODO: check that these are valid (within corresponding models)
    # I'm not using FK to keep things simple in front and back
    country = models.CharField(max_length=100, blank=True)
    industry = models.CharField(max_length=100, blank=True)
    sector = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)
    lead_ic = models.CharField(
        max_length=100, blank=True, help_text="IC member that's championing the deal"
    )
    reception_date = models.DateField(default=timezone.now)
    rejection_date = models.DateField(blank=True, null=True)
    rejection_reason = models.TextField(blank=True)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Contact(TimeStampedModel):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.CharField(max_length=200, blank=True)
    linkedin = models.CharField(max_length=200, blank=True)
    deal = models.ForeignKey(Deal, blank=True, null=True, on_delete=models.CASCADE, related_name="contacts")
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="contacts"
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name(self):
        return str(self)


class BaseNote(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


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


class Checklist(TimeStampedModel):
    NOT_STARTED = "not_started"
    STARTED = "started"
    DONE = "done"

    STATUSES = (
        (NOT_STARTED, "Not Started"),
        (STARTED, "Started"),
        (DONE, "Done"),
    )
    deal = models.OneToOneField(Deal, on_delete=models.CASCADE, related_name='checklist')
    one_pager = models.CharField(
        max_length=20,
        blank=True,
        choices=STATUSES,
        default=NOT_STARTED,
        verbose_name="One Pager",
    )
    met_mgt = models.CharField(
        max_length=20,
        blank=True,
        choices=STATUSES,
        default=NOT_STARTED,
        verbose_name="Met with Management",
    )
    financial_model = models.CharField(
        max_length=20, blank=True, choices=STATUSES, default=NOT_STARTED
    )
    risk_matrix = models.CharField(
        max_length=20,
        blank=True,
        choices=STATUSES,
        default=NOT_STARTED,
    )
    presented_ic = models.CharField(
        max_length=20,
        blank=True,
        choices=STATUSES,
        default=NOT_STARTED,
    )
    investment_memo = models.CharField(
        max_length=20,
        blank=True,
        choices=STATUSES,
        default=NOT_STARTED,
    )
    term_sheet = models.CharField(
        max_length=20,
        blank=True,
        choices=STATUSES,
        default=NOT_STARTED,
    )

    def __str__(self):
        return self.deal.name
