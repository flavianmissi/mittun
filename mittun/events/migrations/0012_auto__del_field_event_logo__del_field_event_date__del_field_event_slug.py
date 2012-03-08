# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Event.logo'
        db.delete_column('events_event', 'logo')

        # Deleting field 'Event.date'
        db.delete_column('events_event', 'date')

        # Deleting field 'Event.slug'
        db.delete_column('events_event', 'slug')


    def backwards(self, orm):
        
        # Adding field 'Event.logo'
        db.add_column('events_event', 'logo', self.gf('django.db.models.fields.files.ImageField')(default='foo', max_length=100), keep_default=False)

        # Adding field 'Event.date'
        db.add_column('events_event', 'date', self.gf('django.db.models.fields.DateField')(default='foo'), keep_default=False)

        # Adding field 'Event.slug'
        db.add_column('events_event', 'slug', self.gf('django.db.models.fields.SlugField')(default='foo', max_length=50, db_index=True), keep_default=False)


    models = {
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'description_en_us': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'description_pt_br': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
