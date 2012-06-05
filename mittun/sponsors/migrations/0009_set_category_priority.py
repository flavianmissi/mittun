# -*- coding: utf-8 -*-
from south.v2 import SchemaMigration

from mittun.sponsors import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        priorities = {
            "Diamond": 0,
            "Platinum": 5,
            "Gold": 10,
            "Silver": 20,
            "Bronze": 30,
            "Partner": 40,
            "FOSS": 50,
        }

        for category in models.Category.objects.all():
            category.priority = priorities.get(category.name, 1000)
            category.save()

    def backwards(self, orm):
        pass
