import requests

from django.conf import settings
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.serializers import (
    RegisterSerializer,
    VerifyOTPSerializer,
)
from user.models import MobileNumber


def send_message_otp(phone_number,otp):
    api_url = "https://www.fast2sms.com/dev/bulkV2"
    authkey = settings.AUTH_KEY
    
    querystring = {
        "numbers" : phone_number,
        "route" : "otp",
        "variables_values" : otp,
        "authorization" : authkey,
    }
    
    headers = {
        'cache-control': "no-cache"
    }
    
    response = requests.request(
        "GET",
        api_url,
        headers = headers,
        params  = querystring
    )
    
    print(response.text)


class RegisterAPIView(APIView):
    serializer_class = RegisterSerializer
    permission_classes = (
        AllowAny,
    )

    def post(self, request):
        phone_number = request.data['phone_number']
        data = MobileNumber.objects.filter(phone_number = phone_number).first()
        
        if data is not None:
            serializer = self.serializer_class(data = request.data)
            phone_number = request.data['phone_number']
            
            if serializer.is_valid(raise_exception = True):
                instance = serializer.save()
                
                content  = {
                    'phone_number': instance.phone_number,
                    'otp': instance.otp
                }
                
                phone_number = instance.phone_number
                otp = instance.otp
                print("Success")
                send_message_otp(phone_number, otp)
                
                return Response(content, status = status.HTTP_201_CREATED)
            else:
                error = {"Error": "Login in Failed"}
                return Response(error, status = status.HTTP_400_BAD_REQUEST)
        else:
            serializer   = self.serializer_class(data = request.data)
            phone_number = request.data['phone_number']
            
            if serializer.is_valid(raise_exception = True):
                instance = serializer.save()
                
                content  = {
                    'phone_number': instance.phone_number,
                    'otp': instance.otp
                }
                
                phone_number = instance.phone_number
                otp = instance.otp
                send_message_otp(phone_number, otp)
                
                return Response(content, status = status.HTTP_201_CREATED)
            else:
                error = {'Error': 'Sign Up Failed'}
                return Response(error, status = status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = VerifyOTPSerializer

    def post(self, request):
        serializer = VerifyOTPSerializer(data = request.data)
        phone_number = request.data['phone_number']
        otp_sent   = request.data['otp']

        if phone_number and otp_sent:
            old_data = MobileNumber.objects.filter(phone_number = phone_number)
            
            if old_data is not None:
                old_data = otp_sent.first()
                otp = old_data.otp
                
                if str(otp) == str(otp_sent):
                    serializer   = self.serializer_class(data = request.data)
                    phone_number = request.data['phone_number']
                    
                    if serializer.is_valid(raise_exception = True):
                        instance = serializer.save()
                        content  = {
                            'phone_number': instance.phone_number,
                            'otp': instance.otp,
                        }
                        return Response(content, status = status.HTTP_201_CREATED)
                res = {'status': False, 'detail': 'OTP incorrect, please try again'}
                return Response(res)