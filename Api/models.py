from django.db import models
import datetime
from django.forms import ModelForm
from django.contrib.auth.models import User

class tempUser(models.Model):
    Email    = models.EmailField(max_length=100,unique=True,blank=False)
    Password = models.CharField(max_length=100)
    DateTimeCreated = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
             self.DateTimeCreated = datetime.datetime.today()
        return super(tempUser, self).save(*args, **kwargs)

class Profile(models.Model):
    user  = models.ForeignKey(tempUser)
    ConfirmationCode = models.CharField(max_length=50)
 
class User(models.Model):
    Email = models.EmailField(max_length=100,unique=True,blank=False)
    Password = models.CharField(max_length=100)
    DateTimeVerified = models.DateTimeField(editable=False)

    def __unicode__(self):
      return self.Email

    def save(self,*args,**kwargs):
        if not self.id:
            self.DateTimeVerified = datetime.datetime.today()
        return super(User,self).save(*args,**kwargs)

class Team(models.Model):
    Name = models.CharField(max_length=200,unique=True,primary_key=True)
    
    def __unicode__(self):
        return self.Name

class LeagueType(models.Model):
     Name = models.CharField(max_length=200,unique=True,primary_key=True)

     def __unicode__(self):
        return self.Name

class League(models.Model):
     Name = models.CharField(max_length=200,unique=True,primary_key=True)
     CountryFlagUrl = models.CharField(max_length=200)
 
     def __unicode__(self):
        return self.Name
     
class Prediction(models.Model):
    Name = models.CharField(max_length=200)
    Message = models.TextField(max_length=1000)

    def __unicode__(self):
       return self.Name

class Unit(models.Model):
     Value = models.CharField(max_length=200)

     def __unicode__(self):
         return self.Value

class CompletedText(models.Model):
     Message = models.CharField(max_length=255)
  
     def __unicode__(self):
        return self.Message 

class PredictionDetail(models.Model):
     LeagueType = models.ForeignKey(LeagueType)
     League     = models.ForeignKey(League) 
     FlagURL    = models.CharField(max_length=200,editable = False)
     HomeTeam   = models.ForeignKey(Team,related_name = 'statusPrediction_home_team')
     AwayTeam   = models.ForeignKey(Team,related_name = 'statusPrediction_away_team')
     Prediction = models.ForeignKey(Prediction)
     isPushNotifSend = models.BooleanField()
     isCompleted = models.BooleanField(default = False) 
     CompletedText = models.ForeignKey(CompletedText)   
     DateTimeCreated = models.DateTimeField()
     DateTimeCompleted = models.DateTimeField()
     isTipVerified = models.BooleanField()
  
     def save(self,*args,**kwargs):
          
         self.FlagURL = self.League.CountryFlagUrl
         return super(PredictionDetail,self).save(*args,**kwargs)     

class PurchasedPrediction(models.Model):
      UserID = models.IntegerField()
      PredictionID = models.IntegerField()
      DateTime = models.DateTimeField(editable = False)

      def save(self,*args,**kwargs):
          if not self.id : 
             self.DateTime = datetime.datetime.today()     
          return super(PurchasedPrediction,self).save(*args,**kwargs)
 
# Create your models here.
