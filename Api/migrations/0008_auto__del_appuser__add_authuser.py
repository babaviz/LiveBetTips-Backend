# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'appUser'
        db.delete_table(u'Api_appuser')

        # Adding model 'authUser'
        db.create_table(u'Api_authuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=100)),
            ('auth_token', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'Api', ['authUser'])


    def backwards(self, orm):
        # Adding model 'appUser'
        db.create_table(u'Api_appuser', (
            ('auth_token', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('DateTimeVerified', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'Api', ['appUser'])

        # Deleting model 'authUser'
        db.delete_table(u'Api_authuser')


    models = {
        u'Api.authuser': {
            'Meta': {'object_name': 'authUser'},
            'auth_token': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Api.completedtext': {
            'Meta': {'object_name': 'CompletedText'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'Api.league': {
            'Meta': {'object_name': 'League'},
            'countryFlagUrl': ('django.db.models.fields.files.ImageField', [], {'default': "'flags/none/no-img.jpg'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'primary_key': 'True'})
        },
        u'Api.leaguetype': {
            'Meta': {'object_name': 'LeagueType'},
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'primary_key': 'True'})
        },
        u'Api.prediction': {
            'Meta': {'object_name': 'Prediction'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'Api.predictiondetail': {
            'DateTimeCompleted': ('django.db.models.fields.DateTimeField', [], {}),
            'DateTimeCreated': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'PredictionDetail'},
            'awayTeam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statusPrediction_away_team'", 'to': u"orm['Api.Team']"}),
            'completedText': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Api.CompletedText']"}),
            'flagURL': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'homeTeam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statusPrediction_home_team'", 'to': u"orm['Api.Team']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isCompleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isPushNotifSend': ('django.db.models.fields.BooleanField', [], {}),
            'isTipVerified': ('django.db.models.fields.BooleanField', [], {}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Api.League']"}),
            'leagueType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Api.LeagueType']"}),
            'prediction': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Api.Prediction']"})
        },
        u'Api.profile': {
            'Meta': {'object_name': 'Profile'},
            'confirmationCode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Api.tempUser']"})
        },
        u'Api.purchasedprediction': {
            'DateTime': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'PurchasedPrediction'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'predictionID': ('django.db.models.fields.IntegerField', [], {}),
            'userID': ('django.db.models.fields.IntegerField', [], {})
        },
        u'Api.team': {
            'Meta': {'object_name': 'Team'},
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'primary_key': 'True'})
        },
        u'Api.tempuser': {
            'DateTimeCreated': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'tempUser'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'Api.unit': {
            'Meta': {'object_name': 'Unit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['Api']