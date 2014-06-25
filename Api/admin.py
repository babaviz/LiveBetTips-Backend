from django.contrib import admin
from Api.models import User,Team,LeagueType,League,Prediction,Unit,CompletedText,PredictionDetail,PurchasedPrediction	


class PredictionDetailAdmin(admin.ModelAdmin):
     
     list_display = ('id','LeagueType','HomeTeam','AwayTeam','isPushNotifSend','isCompleted','isTipVerified')
     list_filter =  ['isCompleted']

class UserAdmin(admin.ModelAdmin):
     list_display = ('id','Email','Password','DateTimeVerified')

class LeagueAdmin(admin.ModelAdmin):
     list_display = ('Name','CountryFlagUrl')

class PredictionAdmin(admin.ModelAdmin):
     list_display = ('id','Name','Message')

class PurchasedPredictionAdmin(admin.ModelAdmin):
     list_display = ('id','UserID','PredictionID')

admin.site.register(User,UserAdmin)
admin.site.register(Team)
admin.site.register(LeagueType)
admin.site.register(League,LeagueAdmin)
admin.site.register(Prediction,PredictionAdmin)
admin.site.register(Unit)
admin.site.register(CompletedText)
admin.site.register(PredictionDetail,PredictionDetailAdmin)
admin.site.register(PurchasedPrediction,PurchasedPredictionAdmin)




# Register your models here.

