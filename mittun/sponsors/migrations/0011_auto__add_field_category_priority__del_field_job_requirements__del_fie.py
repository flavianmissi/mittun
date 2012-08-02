# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Category.priority'
        db.add_column('sponsors_category', 'priority', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)

        # Deleting field 'Job.requirements'
        db.delete_column('sponsors_job', 'requirements_id')

        # Deleting field 'Job.responsabilities'
        db.delete_column('sponsors_job', 'responsabilities_id')

        # Deleting field 'Job.bonuses'
        db.delete_column('sponsors_job', 'bonuses_id')

        # Adding field 'Responsibility.job'
        db.add_column('sponsors_responsibility', 'job', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sponsors.Job']), keep_default=False)

        # Adding field 'Bonus.job'
        db.add_column('sponsors_bonus', 'job', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sponsors.Job']), keep_default=False)

        # Adding field 'Requirement.job'
        db.add_column('sponsors_requirement', 'job', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sponsors.Job']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Category.priority'
        db.delete_column('sponsors_category', 'priority')

        # Adding field 'Job.requirements'
        db.add_column('sponsors_job', 'requirements', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sponsors.Requirement']), keep_default=False)

        # Adding field 'Job.responsabilities'
        db.add_column('sponsors_job', 'responsabilities', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sponsors.Responsibility']), keep_default=False)

        # Adding field 'Job.bonuses'
        db.add_column('sponsors_job', 'bonuses', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sponsors.Bonus']), keep_default=False)

        # Deleting field 'Responsibility.job'
        db.delete_column('sponsors_responsibility', 'job_id')

        # Deleting field 'Bonus.job'
        db.delete_column('sponsors_bonus', 'job_id')

        # Deleting field 'Requirement.job'
        db.delete_column('sponsors_requirement', 'job_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sponsors.bonus': {
            'Meta': {'object_name': 'Bonus'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Job']"})
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
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Job']"})
        },
        'sponsors.responsibility': {
            'Meta': {'object_name': 'Responsibility'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Job']"})
        },
        'sponsors.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Category']"}),
            'description_en_us': ('django.db.models.fields.TextField', [], {}),
            'description_pt_br': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['sponsors']
