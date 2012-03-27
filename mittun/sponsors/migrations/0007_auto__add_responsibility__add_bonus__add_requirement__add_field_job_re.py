# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Responsibility'
        db.create_table('sponsors_responsibility', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('sponsors', ['Responsibility'])

        # Adding model 'Bonus'
        db.create_table('sponsors_bonus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('sponsors', ['Bonus'])

        # Adding model 'Requirement'
        db.create_table('sponsors_requirement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('sponsors', ['Requirement'])

        # Adding field 'Job.responsabilities'
        db.add_column('sponsors_job', 'responsabilities', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['sponsors.Responsibility']), keep_default=False)

        # Adding field 'Job.requirements'
        db.add_column('sponsors_job', 'requirements', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['sponsors.Requirement']), keep_default=False)

        # Adding field 'Job.bonuses'
        db.add_column('sponsors_job', 'bonuses', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['sponsors.Bonus']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Responsibility'
        db.delete_table('sponsors_responsibility')

        # Deleting model 'Bonus'
        db.delete_table('sponsors_bonus')

        # Deleting model 'Requirement'
        db.delete_table('sponsors_requirement')

        # Deleting field 'Job.responsabilities'
        db.delete_column('sponsors_job', 'responsabilities_id')

        # Deleting field 'Job.requirements'
        db.delete_column('sponsors_job', 'requirements_id')

        # Deleting field 'Job.bonuses'
        db.delete_column('sponsors_job', 'bonuses_id')


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
            'name_pt_br': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'})
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
