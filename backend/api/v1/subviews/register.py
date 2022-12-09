from rest_framework import generics
from rest_framework.response import Response

from api.v1.serializers import RegisterSerializer


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(
            data = request.data
        )
        
        serializer.is_valid(
            raise_exception = True
        )
        
        user = serializer.save()
        
        data = {
            "message": "User Created Successfully. Now perform Login to get your token",
            
            "user": RegisterSerializer(
                user,
                context=self.get_serializer_context()
            ).data
        }
        
        return Response(data)