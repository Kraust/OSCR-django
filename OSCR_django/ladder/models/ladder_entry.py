""" LadderEntry Models """

from core.models import BaseModel
from django.db import models

from .ladder import Ladder


class LadderEntry(BaseModel):
    """LadderEntry Model"""

    player = models.TextField()
    data = models.JSONField()

    combatlog = models.ForeignKey("combatlog.CombatLog", on_delete=models.CASCADE)
    ladder = models.ForeignKey(Ladder, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player} | {self.ladder.name} ({self.ladder.difficulty}) - {self.data['dps']:,.0f} DPS"

    @classmethod
    def ordering_fields(cls):
        base_fields = ["player", "ladder__name", "ladder__difficulty"]
        data_fields = []
        """Custom Method to get Ordering Fields"""
        if LadderEntry.objects.count():
            for k, _ in LadderEntry.objects.first().data.items():
                data_fields.append(f"data__{k}")

        return base_fields + data_fields
