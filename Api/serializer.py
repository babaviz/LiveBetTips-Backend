from rest_framework import serializers
from Api.models import tempUser,User,PredictionDetail,Unit,PurchasedPrediction,Prediction

class tempUserSerializer(serializers.ModelSerializer):
    class Meta :
       	model = tempUser
        fields = ('id','Email','Password','DateTimeCreated')

    def restore_object(self,attrs,instance=None):

 	if instance :
           instance.Email     = attrs.get('Email',instance.Email)
           instance.Password  = attrs.get('Password',instance.Password)
           instance.DateTime  = attrs.get('DateTimeCreated',instance.DateTimeCreated)
           return instance
        return tempUser(**attrs)

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User 
        fields = ('id','Email','Password','DateTimeVerified')

class PredictionDSerializer(serializers.ModelSerializer): 
     class Meta : 
        model = PredictionDetail
        fields = ('id','LeagueType','FlagURL','HomeTeam','AwayTeam','isCompleted','Prediction','DateTimeCreated','isTipVerified') 

class PredictionSerializer(serializers.ModelSerializer):
     class Meta : 
         model = Prediction 
         fields = ('id','Name','Message')
