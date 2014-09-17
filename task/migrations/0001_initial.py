# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Task'
        db.create_table(u'task_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('task_id', self.gf('uuidfield.fields.UUIDField')(max_length=32)),
            ('board', self.gf('django.db.models.fields.CharField')(default='Backlog', max_length=11)),
            ('from_unit', self.gf('uuidfield.fields.UUIDField')(max_length=32)),
            ('to_unit', self.gf('uuidfield.fields.UUIDField')(max_length=32)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('complete_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expires_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('command', self.gf('jsonfield.fields.JSONField')(default={})),
            ('response', self.gf('jsonfield.fields.JSONField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'task', ['Task'])


    def backwards(self, orm):
        # Deleting model 'Task'
        db.delete_table(u'task_task')


    models = {
        u'task.task': {
            'Meta': {'object_name': 'Task'},
            'board': ('django.db.models.fields.CharField', [], {'default': "'Backlog'", 'max_length': '11'}),
            'command': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'complete_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'expires_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'from_unit': ('uuidfield.fields.UUIDField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'response': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'task_id': ('uuidfield.fields.UUIDField', [], {'max_length': '32'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'to_unit': ('uuidfield.fields.UUIDField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['task']