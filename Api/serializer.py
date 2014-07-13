from rest_framework import serializers
from Api.models import tempUser,PredictionDetail,Unit,PurchasedPrediction,Prediction,Profile
from django.contrib.auth.models import User 


class tempUserSerializer(serializers.ModelSerializer):
    class Meta :
       	model = tempUser
        fields = ('id','email','password','DateTimeCreated')

    def restore_object(self,attrs,instance=None):

 	if instance :
           instance.email     = attrs.get('email',instance.email)
           instance.password  = attrs.get('password',instance.password)
           instance.DateTime  = attrs.get('DateTimeCreated',instance.DateTimeCreated)
           return instance
        return tempUser(**attrs)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta :
        model = Profile 
        fields = ('id','username','authToken',)

class PredictionSerializer(serializers.ModelSerializer): 
     class Meta : 
        model = Prediction
        fields = ('id','leagueType','flagURL','homeTeam','awayTeam','isCompleted','tipDetail','DateTimeCreated','isPredictionVerified') 

class PredictionDSerializer(serializers.ModelSerializer):
     class Meta : 
         model = PredictionDetail
         fields = ('id','name','message')

class UserSerializer(serializers.ModelSerializer):
      #authToken = serializers.PrimaryKeyRelatedField(many=True)
      profile = ProfileSerializer()    
  
      class Meta :
         model = User
           


