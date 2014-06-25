from django.conf.urls import patterns,url

from Api import views

urlpatterns=patterns('Api.views',
   url(r'^$','registration'),
   url(r'^confirmation/(?P<confirmation_code>\w{0,50})/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$','confirmation'),
   url(r'^login/$','login'),
   url(r'^contactUs/$','contactUs'),
   url(r'^resetPassword/$','resetPassword'),
   url(r'^reset-Password/$','setNewPassword'),
   url(r'^predictions/$','showPredictions'),
   url(r'^user/(?P<userID>\w{0,50})/prediction/(?P<tipID>\w{0,50})/$','predictionDetail'),
   url(r'^user/(?P<userID>\w{0,50})/predictions','userPredictions'),
)
 
