# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Article.body'
        db.alter_column('bloggy_article', 'body', self.gf('bloggy.fields.HTMLField')(attributes=[], tags=['ol', 'ul', 'li', 'strong', 'em', 'p']))

        # Changing field 'Article.date'
        db.alter_column('bloggy_article', 'date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))


    def backwards(self, orm):
        
        # Changing field 'Article.body'
        db.alter_column('bloggy_article', 'body', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Article.date'
        db.alter_column('bloggy_article', 'date', self.gf('django.db.models.fields.DateField')(auto_now_add=True))


    models = {
        'bloggy.article': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Article'},
            'body': ('bloggy.fields.HTMLField', [], {'attributes': '[]', 'tags': "['ol', 'ul', 'li', 'strong', 'em', 'p']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['bloggy']
