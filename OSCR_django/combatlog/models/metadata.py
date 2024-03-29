""" Metadata Models """

from core.models import BaseModel
from django.db import models


class Metadata(BaseModel):
    """Combat Log Model"""

    map = models.TextField()
    difficulty = models.TextField()
    summary = models.JSONField()

    dps_chart = models.JSONField()
    damage_chart = models.JSONField()

    npc_dps_chart = models.JSONField()
    npc_damage_chart = models.JSONField()

    def __str__(self):
        return f"{self.map} ({self.difficulty})"
