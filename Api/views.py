from django.shortcuts import render
from django.contrib.auth.models import User
from Api.models import tempUser,Profile,PredictionDetail,Team,LeagueType,Prediction,CompletedText,League,PurchasedPrediction
from Api.serializer import tempUserSerializer,ProfileSerializer,PredictionSerializer,PredictionDSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes	
from rest_framework import status
import random,string
from rest_framework.renderers import JSONRenderer 
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
import base64 

URL = "178.21.172.107"
@api_view(['POST'])
def registration(request):
    if request.method=='POST':
       content = ("Hello Welcome to your new LiveBetTips account.\nYou can log in right away and start using your new account.\n"
                  "Please take a moment to confirm your email address with us by clicking in link below.")
       encode = base64.b64encode(request.DATA["email"]+":"+request.DATA["password"])
    try:
        user = User.objects.get(email = request.DATA["email"])
    except:
        request.DATA["password"]=make_password(request.DATA["password"])
        serializer =  tempUserSerializer(data=request.DATA)
        if serializer.is_valid():
           serializer.save()
        
           confirmation_code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(33)) 
           profile = Profile(username = request.DATA["email"] , confirmationCode = confirmation_code,authToken = encode)
           profile.save()
           
           send_mail("LiveBetTips Account Confirmation",content+"\n"+URL+"/confirmation/"+str(profile.confirmationCode) 
                     + "/"+profile.username,'no-reply@LiveBetTips.com',[profile.username],fail_silently=False)
           return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_409_CONFLICT)
    return Response(status = status.HTTP_409_CONFLICT)

def confirmation(request,confirmation_code,emailID):
     
   try:
      temp_user = tempUser.objects.get(email=emailID)
   except:
      return HttpResponse("Sorry your doesnt exist.Please register again")
   
   profile = Profile.objects.get(username =temp_user.email)
   if profile.confirmationCode == confirmation_code:
      user = User(username=temp_user.email, email = temp_user.email ,password = temp_user.password)                 
      user.save()
      
      temp_user.delete()
      return HttpResponse("Thankyou! Your account has been activated .Now you can login")
   return HttpResponse("Sorry your account couldn't be activated this time. Please try again later")

@api_view(['POST'])
def resetPassword(request):
    if request.method=='POST':
    
     try:
        user = User.objects.get(email = request.DATA['email'])      
     except : 
        return Response(status = status.HTTP_404_NOT_FOUND)
     send_mail("LiveBetTips Password Reset","Click on the link below to reset your password.\n"+URL+"/reset-password/"
               ,'no-reply@LiveBetTips.com',[user.email],fail_silently=False)
     return Response(status = status.HTTP_200_OK) 

def setNewPassword(request):
    if request.method == 'POST':
       
      try:
        user = User.objects.get(email = request.POST['email'])  
      except:
        return HttpResponse("Sorry EmailID doesn't exist.Please go back and re-enter your email id")
      
      encode = base64.b64encode(user.email + ":" + request.POST['password'])
      pro= Profile.objects.get(username = user.email)
      pro.authToken = encode
      pro.save()
      password = make_password(request.POST['password'])
      user.password = password 
      user.save()
      return HttpResponse("Your Password has been reset.")  
    return render(request , 'Api/resetForm.html',{ })     

@api_view(['POST'])
def login(request):
   if request.method=='POST':
   
     try:
         user = User.objects.get(email = request.DATA["email"])
     except: 
         try:
            temp_user = tempUser.objects.get(email = request.DATA["email"])
         except : 
            return Response(status=status.HTTP_404_NOT_FOUND)
         return Response(status=status.HTTP_409_CONFLICT)
     
     profile = Profile.objects.get(username = user.email) 
     profileSerializer = ProfileSerializer(profile)  
     if check_password(request.DATA["password"],user.password) :
        
        return Response(profileSerializer.data,status = status.HTTP_200_OK)
     return Response(profileSerializer.errors,status = status.HTTP_401_UNAUTHORIZED) 
    
@api_view(['POST'])
@permission_classes((IsAuthenticated ,))
def contactUs(request) :
   if request.method=='POST':
      adminEmail= 'sarthakmeh03@gmail.com'
      userEmail = request.DATA["email"]
      message   = request.DATA["content"]
      subject   = request.DATA["subject"]
      send_mail(subject,message,userEmail,[adminEmail],fail_silently=False)
      return Response(status = status.HTTP_200_OK)
   return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes((IsAuthenticated ,))
def showPredictions(request):
     
    if request.method=='GET':
      try:
       predictions = Prediction.objects.filter(isPushNotifSend=request.GET.get('isPushed',''))
      except : 
         return Response(status = status.HTTP_404_NOT_FOUND)    
           
      predictSerializer = PredictionSerializer(predictions) 
      return Response(predictSerializer.data,status = status.HTTP_200_OK)
    return Response(status =status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes((IsAuthenticated ,))
def predictionDetail(request,userID,tipID):
    if request.method=='GET':
       
      try:  
        user = User.objects.get(id = userID)
      except:
        return Response(status = status.HTTP_404_NOT_FOUND)

      try:   
       tip = Prediction.objects.get(id = tipID)
      except:
       return Response(status = status.HTTP_400_BAD_REQUEST)
      
      prediction = PredictionDetail.objects.get(id = tip.tipDetail_id)      
      if tip.isCompleted == True : 
         completedText = CompletedText.objects.get(id = tip.completedText_id) 
         prediction.message = prediction.message + ". "+completedText.message   
               
         predictionSerializer = PredictionDSerializer(prediction)
         return Response(predictionSerializer.data,status = status.HTTP_200_OK)
      else : 
         try:
          purchasePrediction=PurchasedPrediction.objects.get(userID = userID,predictionID = tipID)
         except: 
           return Response(status = status.HTTP_401_UNAUTHORIZED)
    
         predictionSerializer = PredictionDSerializer(prediction)
         return Response(predictionSerializer.data , status=status.HTTP_200_OK)
      return Response(status = status.HTTP_404_NOT_FOUND)    
            
@api_view(['GET'])
@permission_classes((IsAuthenticated ,))
def userPredictions(request,userID):
    if request.method == 'GET':
       predictions = [] 
       
       try: 
         user = User.objects.get(id = userID)
       except: 
         return Response(status = status.HTTP_404_NOT_FOUND)
       
       try:      
         userPredicts = PurchasedPrediction.objects.filter(userID = userID)
       except : 
         return Response(status = status.HTTP_404_NOT_FOUND)
        
       for predict in userPredicts :
         try:
          predicts=Prediction.objects.get(id = predict.predictionID)
         except :
          return Response(status = status.HTTP_404_NOT_FOUND)
         predictions.append(predicts)
            
       predictSerializer = PredictionSerializer(predictions)
       return Response(predictSerializer.data , status = status.HTTP_200_OK)


