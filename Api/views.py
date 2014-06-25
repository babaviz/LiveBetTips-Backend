from django.shortcuts import render
from django.contrib.auth.models import User
from Api.models import tempUser,Profile,User,PredictionDetail,Team,LeagueType,Prediction,CompletedText,League,PurchasedPrediction
from Api.serializer import tempUserSerializer,UserSerializer,PredictionSerializer,PredictionDSerializer
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

@api_view(['POST'])
def registration(request):
    if request.method=='POST':
       content = ("Hello Welcome to your new LiveBetTips account.\nYou can log in right away and start using your new account.\n"
                  "Please take a moment to confirm your email address with us by clicking in link below.")
    try:
        user = User.objects.get(Email = request.DATA["Email"])
    except:
        request.DATA["Password"]=make_password(request.DATA["Password"])
        serializer =  tempUserSerializer(data=request.DATA)
        if serializer.is_valid():
           serializer.save()
        
           temp_user=tempUser.objects.get(Email = request.DATA["Email"])
           confirmation_code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(33))
           profile = Profile(user = temp_user , ConfirmationCode = confirmation_code)
           profile.save()
           
           send_mail("LiveBetTips Account Confirmation",content+"\n127.0.0.1:8000/confirmation/"+str(profile.ConfirmationCode) 
                     + "/"+profile.user.Email,'no-reply@LiveBetTips.com',[profile.user.Email],fail_silently=False)
           return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_409_CONFLICT)
    return Response(status = status.HTTP_409_CONFLICT)

def confirmation(request,confirmation_code,email):
     
   try:
      temp_user = tempUser.objects.get(Email=email)
   except:
      return HttpResponse("Sorry your doesnt exist.Please register again")
   
   pro = Profile.objects.get(user_id=temp_user.id)
   if pro.ConfirmationCode == confirmation_code:
      user = User(Email = temp_user.Email ,Password = temp_user.Password)                 
      user.save()
      temp_user.delete()
      return HttpResponse("Thankyou! Your account has been activated .Now you can login")
   return HttpResponse("Sorry your account couldn't be activated this time. Please try again later")

@api_view(['POST'])
def resetPassword(request):
    if request.method=='POST':
    
     try:
        user = User.objects.get(Email = request.DATA['Email'])      
     except : 
        return Response(status = status.HTTP_404_NOT_FOUND)
     send_mail("LiveBetTips Password Reset","Click on the link below to reset your password.\n127.0.0.1:8000/reset-Password/"
               ,'no-reply@LiveBetTips.com',[user.Email],fail_silently=False)
     return Response(status = status.HTTP_200_OK) 

def setNewPassword(request):
    if request.method == 'POST':
       
      try:
        user = User.objects.get(Email = request.POST['Email'])  
      except:
        return HttpResponse("Sorry EmailID doesn't exist.Please go back and re-enter your email id")
      password = make_password(request.POST['Password'])
      user.Password = password 
      user.save()
      return HttpResponse("Your Password has been reset.")  
    return render(request , 'Api/resetForm.html',{ })     

@api_view(['POST'])
def login(request):
   if request.method=='POST':
   
     try:
         user = User.objects.get(Email = request.DATA["Email"])
     except: 
         try:
            temp_user = tempUser.objects.get(Email = request.DATA["Email"])
         except : 
            return Response(status=status.HTTP_404_NOT_FOUND)
         return Response(status=status.HTTP_409_CONFLICT)
 
     user_serializer = UserSerializer(user)  
     if check_password(request.DATA["Password"],user.Password) :
        return Response(user_serializer.data,status = status.HTTP_200_OK)
     return Response(user_serializer.errors,status = status.HTTP_401_UNAUTHORIZED) 
    
@api_view(['POST'])
def contactUs(request) :
   if request.method=='POST':
      adminEmail= 'sarthakmeh03@gmail.com'
      userEmail = request.DATA["Email"]
      message   = request.DATA["Content"]
      subject   = request.DATA["Subject"]
      send_mail(subject,message,userEmail,[adminEmail],fail_silently=False)
      return Response(status = status.HTTP_200_OK)
   return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def showPredictions(request):
     
    if request.method=='GET':
      try:
       predictions = PredictionDetail.objects.filter(isPushNotifSend=request.GET.get('isPushed',''))
      except : 
         return Response(status = status.HTTP_404_NOT_FOUND)    
           
      predictSerializer = PredictionDSerializer(predictions) 
      return Response(predictSerializer.data,status = status.HTTP_200_OK)
    return Response(status =status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def predictionDetail(request,userID,tipID):
    if request.method=='GET':
       
      try:  
        user = User.objects.get(id = userID)
      except:
        return Response(status = status.HTTP_400_BAD_REQUEST)

      try:   
       tipDetail = PredictionDetail.objects.get(Prediction_id = tipID)
      except:
       return Response(status = status.HTTP_400_BAD_REQUEST)
      
      prediction = Prediction.objects.get(id = tipID)      
      if tipDetail.isCompleted == True : 
         completedText = CompletedText.objects.get(id = tipDetail.CompletedText_id) 
         prediction.Message = prediction.Message + ". "+completedText.Message   
               
         predictionSerializer = PredictionSerializer(prediction)
         return Response(predictionSerializer.data,status = status.HTTP_200_OK)
      else : 
         try:
          purchasePrediction=PurchasedPrediction.objects.get(UserID = userID,PredictionID = tipID)
         except: 
           return Response(status = status.HTTP_401_UNAUTHORIZED)
    
         predictionSerializer = PredictionSerializer(prediction)
         return Response(predictionSerializer.data , status=status.HTTP_200_OK)
      return Response(status = status.HTTP_404_NOT_FOUND)    
            
@api_view(['GET'])
def userPredictions(request,userID):
    if request.method == 'GET':
       predictions = [] 
       
       try: 
         user = User.objects.get(id = userID)
       except: 
         return Response(status = status.HTTP_400_BAD_REQUEST)
       
       try:      
         userPredicts = PurchasedPrediction.objects.filter(UserID = userID)
       except : 
         return Response(status = status.HTTP_400_BAD_REQUEST)
        
       for predict in userPredicts :
         try:
          predicts=PredictionDetail.objects.get(Prediction_id = predict.PredictionID)
         except :
          return Response(status = status.HTTP_404_NOT_FOUND)
         predictions.append(predicts)
            
       predictSerializer = PredictionDSerializer(predictions)
       return Response(predictSerializer.data , status = status.HTTP_200_OK)



    
 

     
