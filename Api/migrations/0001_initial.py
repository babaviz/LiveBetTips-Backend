# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'tempUser'
        db.create_table(u'Api_tempuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=100)),
            ('Password', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('DateTimeCreated', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'Api', ['tempUser'])

        # Adding model 'Profile'
        db.create_table(u'Api_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Api.tempUser'])),
            ('ConfirmationCode', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'Api', ['Profile'])

        # Adding model 'User'
        db.create_table(u'Api_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=100)),
            ('Password', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('DateTimeVerified', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'Api', ['User'])

        # Adding model 'Team'
        db.create_table(u'Api_team', (
            ('Name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, primary_key=True)),
        ))
        db.send_create_signal(u'Api', ['Team'])

        # Adding model 'LeagueType'
        db.create_table(u'Api_leaguetype', (
            ('Name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, primary_key=True)),
        ))
        db.send_create_signal(u'Api', ['LeagueType'])

        # Adding model 'League'
        db.create_table(u'Api_league', (
            ('Name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, primary_key=True)),
            ('CountryFlagUrl', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'Api', ['League'])

        # Adding model 'Prediction'
        db.create_table(u'Api_prediction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Message', self.gf('django.db.models.fields.TextField')(max_length=1000)),
        ))
        db.send_create_signal(u'Api', ['Prediction'])

        # Adding model 'Unit'
        db.create_table(u'Api_unit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Value', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'Api', ['Unit'])

        # Adding model 'CompletedText'
        db.create_table(u'Api_completedtext', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Message', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'Api', ['CompletedText'])

        # Adding model 'PredictionDetail'
        db.create_table(u'Api_predictiondetail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('LeagueType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Api.LeagueType'])),
            ('League', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Api.League'])),
            ('FlagURL', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('HomeTeam', self.gf('django.db.models.fields.related.ForeignKey')(related_name='statusPrediction_home_team', to=orm['Api.Team'])),
            ('AwayTeam', self.gf('django.db.models.fields.related.ForeignKey')(related_name='statusPrediction_away_team', to=orm['Api.Team'])),
            ('Prediction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Api.Prediction'])),
            ('isPushNotifSend', self.gf('django.db.models.fields.BooleanField')()),
            ('isCompleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('CompletedText', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Api.CompletedText'])),
            ('DateTimeCreated', self.gf('django.db.models.fields.DateTimeField')()),
            ('DateTimeCompleted', self.gf('django.db.models.fields.DateTimeField')()),
            ('isTipVerified', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'Api', ['PredictionDetail'])

        # Adding model 'PurchasedPrediction'
        db.create_table(u'Api_purchasedprediction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('UserID', self.gf('django.db.models.fields.IntegerField')()),
            ('PredictionID', self.gf('django.db.models.fields.IntegerField')()),
            ('DateTime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'Api', ['PurchasedPrediction'])


    def backwards(self, orm):
        # Deleting model 'tempUser'
        db.delete_table(u'Api_tempuser')

        # Deleting model 'Profile'
        db.delete_table(u'Api_profile')

        # Deleting model 'User'
        db.delete_table(u'Api_user')

        # Deleting model 'Team'
        db.delete_table(u'Api_team')

        # Deleting model 'LeagueType'
        db.delete_table(u'Api_leaguetype')

        # Deleting model 'League'
        db.delete_table(u'Api_league')

        # Deleting model 'Prediction'
        db.delete_table(u'Api_prediction')

        # Deleting model 'Unit'
        db.delete_table(u'Api_unit')

        # Deleting model 'CompletedText'
        db.delete_table(u'Api_completedtext')

        # Deleting model 'PredictionDetail'
        db.delete_table(u'Api_predictiondetail')

        # Deleting model 'PurchasedPrediction'
        db.delete_table(u'Api_purchasedprediction')


    models = {
        u'Api.completedtext': {
            'Message': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Meta': {'object_name': 'CompletedText'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Api.league': {
            'CountryFlagUrl': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Meta': {'object_name': 'League'},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'primary_key': 'True'})
        },
        u'Api.leaguetype': {
            'Meta': {'object_name': 'LeagueType'},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'primary_key': 'True'})
        },
        u'Api.prediction': {
            'Message': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'Meta': {'object_name': 'Prediction'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Api.predictiondetail': {
            'AwayTeam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statusPrediction_away_team'", 'to': u"orm['Api.Team']"}),
            'CompletedText': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Api.CompletedText']"}),
            'DateTimeCompleted': ('django.db.models.fields.DateTimeField', [], {}),
            'DateTimeCreated': ('django.db.models.fields.DateTimeField', [], {}),
            'FlagURL': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'HomeTeam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statusPrediction_home_team'", 'to': u"orm['Api.Team']"}),
            'League': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Api.League']"}),
            'LeagueType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Api.LeagueType']"}),
            'Meta': {'object_name': 'PredictionDetail'},
            'Prediction': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Api.Prediction']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isCompleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isPushNotifSend': ('django.db.models.fields.BooleanField', [], {}),
            'isTipVerified': ('django.db.models.fields.BooleanField', [], {})
        },
        u'Api.profile': {
            'ConfirmationCode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'object_name': 'Profile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Api.tempUser']"})
        },
        u'Api.purchasedprediction': {
            'DateTime': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'PurchasedPrediction'},
            'PredictionID': ('django.db.models.fields.IntegerField', [], {}),
            'UserID': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Api.team': {
            'Meta': {'object_name': 'Team'},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'primary_key': 'True'})
        },
        u'Api.tempuser': {
            'DateTimeCreated': ('django.db.models.fields.DateTimeField', [], {}),
            'Email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '100'}),
            'Meta': {'object_name': 'tempUser'},
            'Password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Api.unit': {
            'Meta': {'object_name': 'Unit'},
            'Value': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Api.user': {
            'DateTimeVerified': ('django.db.models.fields.DateTimeField', [], {}),
            'Email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '100'}),
            'Meta': {'object_name': 'User'},
            'Password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['Api']