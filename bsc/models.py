from pickle import TRUE
from django.db import models
from core.models import User
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.

class Perspective(models.Model):
    perspective_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    perspective_name = models.CharField(max_length=120, blank=False)
    perspective_weight = models.FloatField(blank=True, null=True)
    vp_corporate_perspective_weight = models.FloatField(blank=True, null=True)
    vp_cooperative_perspective_weight = models.FloatField(blank=True, null=True)
    vp_credit_perspective_weight = models.FloatField(blank=True, null=True)
    vp_finance_perspective_weight = models.FloatField(blank=True, null=True)
    vp_hc_perspective_weight = models.FloatField(blank=True, null=True)
    vp_internal_perspective_weight = models.FloatField(blank=True, null=True)
    vp_ifb_perspective_weight = models.FloatField(blank=True, null=True)
    vp_is_perspective_weight = models.FloatField(blank=True, null=True)
    vp_legal_perspective_weight = models.FloatField(blank=True, null=True)
    vp_bod_perspective_weight = models.FloatField(blank=True, null=True)
    vp_risk_perspective_weight = models.FloatField(blank=True, null=True)
    vp_strategy_perspective_weight = models.FloatField(blank=True, null=True)
    vp_tech_perspective_weight = models.FloatField(blank=True, null=True)
  

    def __str__(self):
        return f"{self.perspective_name}"


class Objectives(models.Model):
    objective_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    objective_name = models.CharField(max_length=120, blank=False)
    objective_weight = models.FloatField(blank=False)
    perspective = models.ForeignKey(Perspective, on_delete=models.CASCADE)
    vp_corporateobjective_weight = models.FloatField(blank=True, null=True)
    vp_cooperativeobjective_weight = models.FloatField(blank=True, null=True)
    vp_creditobjective_weight = models.FloatField(blank=True, null=True)
    vp_financeobjective_weight = models.FloatField(blank=True, null=True)
    vp_hcobjective_weight = models.FloatField(blank=True, null=True)
    vp_internalobjective_weight = models.FloatField(blank=True, null=True)
    vp_ifbobjective_weight = models.FloatField(blank=True, null=True)
    vp_isobjective_weight = models.FloatField(blank=True, null=True)
    vp_legalobjective_weight = models.FloatField(blank=True, null=True)
    vp_bodobjective_weight = models.FloatField(blank=True, null=True)
    vp_riskobjective_weight = models.FloatField(blank=True, null=True)
    vp_strategyobjective_weight = models.FloatField(blank=True, null=True)
    vp_techobjective_weight = models.FloatField(blank=True, null=True)

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
    January = models.FloatField(blank=True, default=0)
    February = models.FloatField(blank=True, default=0)
    March = models.FloatField(blank=True, default=0)
    April = models.FloatField(blank=True, default=0)
    May = models.FloatField(blank=True, default=0)
    June = models.FloatField(blank=True, default=0)
    July = models.FloatField(blank=True, default=0)
    August = models.FloatField(blank=True, default=0)
    September = models.FloatField(blank=True, default=0)
    October = models.FloatField(blank=True, default=0)
    November = models.FloatField(blank=True, default=0)
    December = models.FloatField(blank=True, default=0)
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
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.kpi_name}"
