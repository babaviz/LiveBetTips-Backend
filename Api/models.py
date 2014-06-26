from django.db import models
import datetime
from django.forms import ModelForm
from django.contrib.auth.models import User

class tempUser(models.Model):
    email    = models.EmailField(max_length=100,unique=True,blank=False)
    password = models.CharField(max_length=100)
    DateTimeCreated = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
             self.DateTimeCreated = datetime.datetime.today()
        return super(tempUser, self).save(*args, **kwargs)

class Profile(models.Model):
    username  = models.EmailField(max_length=100,unique=True)
    confirmationCode = models.CharField(max_length=50)
    authToken = models.CharField(max_length=100)
 
class Team(models.Model):
    name = models.CharField(max_length=200,unique=True,primary_key=True)
    
    def __unicode__(self):
        return self.name

class LeagueType(models.Model):
     name = models.CharField(max_length=200,unique=True,primary_key=True)

     def __unicode__(self):
        return self.name

class League(models.Model):
     name = models.CharField(max_length=200,unique=True,primary_key=True)
     countryFlagUrl = models.ImageField(upload_to='flags/',default='flags/none/no-img.jpg')
 

     def __unicode__(self):
        return self.name
     
class Prediction(models.Model):
    name = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)

    def __unicode__(self):
       return self.name

class Unit(models.Model):
     value = models.CharField(max_length=200)

     def __unicode__(self):
         return self.value

class CompletedText(models.Model):
     message = models.CharField(max_length=255)
  
     def __unicode__(self):
        return self.message 

class PredictionDetail(models.Model):
     leagueType = models.ForeignKey(LeagueType)
     league     = models.ForeignKey(League) 
     flagURL    = models.CharField(max_length=200,editable = False)
     homeTeam   = models.ForeignKey(Team,related_name = 'statusPrediction_home_team')
     awayTeam   = models.ForeignKey(Team,related_name = 'statusPrediction_away_team')
     prediction = models.ForeignKey(Prediction)
     isPushNotifSend = models.BooleanField()
     isCompleted = models.BooleanField(default = False) 
     completedText = models.ForeignKey(CompletedText)   
     DateTimeCreated = models.DateTimeField()
     DateTimeCompleted = models.DateTimeField()
     isTipVerified = models.BooleanField()
  
     def save(self,*args,**kwargs):
          
         self.flagURL = self.league.countryFlagUrl
         return super(PredictionDetail,self).save(*args,**kwargs)     

class PurchasedPrediction(models.Model):
      userID = models.IntegerField()
      predictionID = models.IntegerField()
      DateTime = models.DateTimeField(editable = False)

      def save(self,*args,**kwargs):
          if not self.id : 
             self.DateTime = datetime.datetime.today()     
          return super(PurchasedPrediction,self).save(*args,**kwargs)
 
# Create your models here.
