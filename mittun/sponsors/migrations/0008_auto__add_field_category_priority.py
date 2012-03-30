# encoding: utf-8
from south.db import db
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

        # Adding field 'Category.priority'
        db.add_column('sponsors_category', 'priority', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        for category in models.Category.objects.all():
            category.priority = priorities[category.name]
            category.save()

    def backwards(self, orm):

        # Deleting field 'Category.priority'
        db.delete_column('sponsors_category', 'priority')

    models = {
        'sponsors.bonus': {
            'Meta': {'object_name': 'Bonus'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'sponsors.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en_us': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'name_pt_br': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {})
        },
        'sponsors.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sponsor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Sponsor']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sponsors.job': {
            'Meta': {'object_name': 'Job'},
            'bonuses': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Bonus']"}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Sponsor']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'requirements': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Requirement']"}),
            'responsabilities': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Responsibility']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'web_site': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'sponsors.requirement': {
            'Meta': {'object_name': 'Requirement'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'sponsors.responsibility': {
            'Meta': {'object_name': 'Responsibility'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'sponsors.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Category']"}),
            'description_en_us': ('django.db.models.fields.TextField', [], {}),
            'description_pt_br': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['sponsors']
