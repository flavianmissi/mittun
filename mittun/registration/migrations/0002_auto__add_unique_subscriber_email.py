# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding unique constraint on 'Subscriber', fields ['email']
        db.create_unique('registration_subscriber', ['email'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Subscriber', fields ['email']
        db.delete_unique('registration_subscriber', ['email'])


    models = {
        'registration.subscriber': {
            'Meta': {'object_name': 'Subscriber'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subscription_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['registration']
