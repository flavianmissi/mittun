# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Job.requirements'
        db.delete_column('sponsors_job', 'requirements_id')

        # Deleting field 'Job.responsabilities'
        db.delete_column('sponsors_job', 'responsabilities_id')

        # Deleting field 'Job.bonuses'
        db.delete_column('sponsors_job', 'bonuses_id')

        # Adding field 'Responsibility.jobs'
        db.add_column('sponsors_responsibility', 'jobs', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['sponsors.Job']), keep_default=False)

        # Adding field 'Bonus.jobs'
        db.add_column('sponsors_bonus', 'jobs', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['sponsors.Job']), keep_default=False)

        # Adding field 'Requirement.jobs'
        db.add_column('sponsors_requirement', 'jobs', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['sponsors.Job']), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Job.requirements'
        db.add_column('sponsors_job', 'requirements', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['sponsors.Requirement']), keep_default=False)

        # Adding field 'Job.responsabilities'
        db.add_column('sponsors_job', 'responsabilities', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['sponsors.Responsibility']), keep_default=False)

        # Adding field 'Job.bonuses'
        db.add_column('sponsors_job', 'bonuses', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['sponsors.Bonus']), keep_default=False)

        # Deleting field 'Responsibility.jobs'
        db.delete_column('sponsors_responsibility', 'jobs_id')

        # Deleting field 'Bonus.jobs'
        db.delete_column('sponsors_bonus', 'jobs_id')

        # Deleting field 'Requirement.jobs'
        db.delete_column('sponsors_requirement', 'jobs_id')


    models = {
        'sponsors.bonus': {
            'Meta': {'object_name': 'Bonus'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jobs': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Job']"})
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
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Sponsor']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'web_site': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'sponsors.requirement': {
            'Meta': {'object_name': 'Requirement'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jobs': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Job']"})
        },
        'sponsors.responsibility': {
            'Meta': {'object_name': 'Responsibility'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jobs': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Job']"})
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
