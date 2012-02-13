# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Event.description'
        db.delete_column('events_event', 'description')

        # Adding field 'Event.description_en_us'
        db.add_column('events_event', 'description_en_us', self.gf('django.db.models.fields.CharField')(default='', max_length=200), keep_default=False)

        # Adding field 'Event.description_pt_br'
        db.add_column('events_event', 'description_pt_br', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Event.description'
        db.add_column('events_event', 'description', self.gf('django.db.models.fields.CharField')(default='', max_length=200), keep_default=False)

        # Deleting field 'Event.description_en_us'
        db.delete_column('events_event', 'description_en_us')

        # Deleting field 'Event.description_pt_br'
        db.delete_column('events_event', 'description_pt_br')


    models = {
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description_en_us': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description_pt_br': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'events.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['events']
