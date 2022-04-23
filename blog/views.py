from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import BlogPost
from .serializers import BlogPostSerializer


@api_view(["GET", "POST"])
def posts(request):
    if request.method == "GET":
        all_post = BlogPost.objects.all()
        serializer = BlogPostSerializer(all_post, many=True)
        
        data = {
            "message":"success",
            "data":serializer.data
        }
    
        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = BlogPostSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            data = {
            "message":"success",
            "data":serializer.data
            }
    
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
            "message":"failed",
            "error":serializer.errors
            }
    
            return Response(data, status=status.HTTP_400_BAD_REQUEST)