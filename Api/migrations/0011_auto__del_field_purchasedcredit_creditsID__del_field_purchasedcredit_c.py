# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PurchasedCredit.creditsID'
        db.delete_column(u'Api_purchasedcredit', 'creditsID')

        # Deleting field 'PurchasedCredit.credits'
        db.delete_column(u'Api_purchasedcredit', 'credits')

        # Adding field 'PurchasedCredit.credit'
        db.add_column(u'Api_purchasedcredit', 'credit',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'PurchasedCredit.creditID'
        db.add_column(u'Api_purchasedcredit', 'creditID',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'PurchasedCredit.creditsID'
        db.add_column(u'Api_purchasedcredit', 'creditsID',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'PurchasedCredit.credits'
        db.add_column(u'Api_purchasedcredit', 'credits',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Deleting field 'PurchasedCredit.credit'
        db.delete_column(u'Api_purchasedcredit', 'credit')

        # Deleting field 'PurchasedCredit.creditID'
        db.delete_column(u'Api_purchasedcredit', 'creditID')


    models = {
        u'Api.completedtext': {
            'Meta': {'object_name': 'CompletedText'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'Api.credit': {
            'Meta': {'object_name': 'Credit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'Api.league': {
            'Meta': {'object_name': 'League'},
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'primary_key': 'True'})
        },
        u'Api.leaguetype': {
            'Meta': {'object_name': 'LeagueType'},
            'countryFlagUrl': ('django.db.models.fields.files.ImageField', [], {'default': "'flags/none/no-img.jpg'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'primary_key': 'True'})
        },
        u'Api.prediction': {
            'DateTimeCompleted': ('django.db.models.fields.DateTimeField', [], {}),
            'DateTimeCreated': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'Prediction'},
            'awayTeam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statusPrediction_away_team'", 'to': u"orm['Api.Team']"}),
            'completedText': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Api.CompletedText']"}),
            'covered': ('django.db.models.fields.BooleanField', [], {}),
            'flagURL': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'homeTeam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statusPrediction_home_team'", 'to': u"orm['Api.Team']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isCompleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isPredictionVerified': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'isPushNotifSend': ('django.db.models.fields.BooleanField', [], {}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Api.League']"}),
            'leagueType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Api.LeagueType']"}),
            'pending': ('django.db.models.fields.BooleanField', [], {}),
            'tipDetail': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Api.PredictionDetail']"}),
            'verified': ('django.db.models.fields.BooleanField', [], {})
        },
        u'Api.predictiondetail': {
            'Meta': {'object_name': 'PredictionDetail'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'Api.profile': {
            'Meta': {'object_name': 'Profile'},
            'authToken': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'confirmationCode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'Api.purchasedcredit': {
            'Meta': {'object_name': 'PurchasedCredit'},
            'credit': ('django.db.models.fields.IntegerField', [], {}),
            'creditID': ('django.db.models.fields.IntegerField', [], {}),
            'dateTime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'userID': ('django.db.models.fields.IntegerField', [], {})
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