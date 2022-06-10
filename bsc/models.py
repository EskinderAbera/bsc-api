from pickle import TRUE
from django.db import models
from core.models import User
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.

class Perspective(models.Model):
    perspective_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    perspective_name = models.CharField(max_length=120, blank=False)
    perspective_weight = models.FloatField(blank=False)

    def __str__(self):
        return f"{self.perspective_name}"


class Objectives(models.Model):
    objective_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    objective_name = models.CharField(max_length=120, blank=False)
    objective_weight = models.FloatField(blank=False)
    perspective = models.ForeignKey(Perspective, on_delete=models.CASCADE)

    # class Types(models.TextChoices):
    #     January = "January", "January"
    #     February = "February", "February"
    #     March = "March", "March"
    #     April = "April", "April"
    #     May = "May", "May"
    #     June = "June", "June"
    #     July = "July", "July"
    #     August = "August", "August"
    #     September = "September", "September"
    #     October = "October", "October"
    #     November = "November", "November"
    #     December = "December", "December"

    # default_month = Types.January

    # month = models.CharField(
    #     _("Type"), max_length=50, choices=Types.choices, default=default_month
    # )

    def __str__(self):
        return f"{self.objective_name}"


class KPI(models.Model):
    kpi_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kpi_name = models.CharField(max_length=120, blank=False)
    kpi_weight = models.FloatField(blank=False)

    class Types(models.TextChoices):
        Percentage = "Percentage", "Percentage"
        ETB = "ETB", "ETB"
        USD = "USD", "USD"
        Numbers = "Numbers", "Numbers"
        Levels = "Levels", "Levels"

    default_kpi_unit_measurement = Types.Percentage

    kpi_unit_measurement = models.CharField(
        _("kpi_unit_measurement"), max_length=50, choices=Types.choices, default=default_kpi_unit_measurement
    )
    kpi_target = models.FloatField(blank=True)
    perspective = models.ForeignKey(Perspective, on_delete=models.CASCADE)
    objective = models.ForeignKey(Objectives, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    January = models.FloatField(blank=True, null=True)
    February = models.FloatField(blank=True, null=True)
    March = models.FloatField(blank=True, null=True)
    April = models.FloatField(blank=True, null=True)
    May = models.FloatField(blank=True, null=True)
    June = models.FloatField(blank=True, null=True)
    July = models.FloatField(blank=True, null=True)
    August = models.FloatField(blank=True, null=True)
    September = models.FloatField(blank=True, null=True)
    October = models.FloatField(blank=True, null=True)
    November = models.FloatField(blank=True, null=True)
    December = models.FloatField(blank=True, null=True)
    Score_January = models.FloatField(blank=True, default=0)
    Score_February = models.FloatField(blank=True, default=0)
    Score_March = models.FloatField(blank=True, default=0)
    Score_April = models.FloatField(blank=True, default=0)
    Score_May = models.FloatField(blank=True, default=0)
    Score_June = models.FloatField(blank=True, default=0)
    Score_July = models.FloatField(blank=True, default=0)
    Score_August = models.FloatField(blank=True, default=0)
    Score_September = models.FloatField(blank=True, default=0)
    Score_October = models.FloatField(blank=True, default=0)
    Score_November = models.FloatField(blank=True, default=0)
    Score_December = models.FloatField(blank=True, default=0)
    aggregate = models.FloatField(blank=True, default=0)

    def __str__(self):
        return f"{self.kpi_name}"
