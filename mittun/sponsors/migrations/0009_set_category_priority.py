# -*- coding: utf-8 -*-
from south.v2 import SchemaMigration

from mittun.sponsors import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        priorities = {
            "Diamond": 0,
            "Gold": 10,
            "Silver": 20,
            "Bronze": 30,
            "Partner": 40,
            "FOSS": 50,
        }

        for category in models.Category.objects.all():
            category.priority = priorities[category.name]
            category.save()

    def backwards(self, orm):
        pass
