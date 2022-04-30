from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes 
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from .models import BlogPost
from .serializers import BlogPostSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import PermissionDenied

@swagger_auto_schema(method="post", request_body=BlogPostSerializer())
@api_view(["GET", "POST"])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def posts(request):
    if request.method == "GET":
        all_post = BlogPost.objects.filter(author=request.user)
        serializer = BlogPostSerializer(all_post, many=True)
        
        data = {
            "message":"success",
            "data":serializer.data
        }
    
        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = BlogPostSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.validated_data['author'] = request.user
            
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
        
        


@swagger_auto_schema(methods=['put', 'delete'], request_body=BlogPostSerializer())
@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def post_detail(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    
    if request.method not in SAFE_METHODS and post.author != request.user:
        raise PermissionDenied({
            "message":"you do not have permission to perform this action"
        })
    
    if request.method == "GET":
        serializer = BlogPostSerializer(post)
        
        data = {
            "message":"success",
            "data":serializer.data
        }
    
        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method=="PUT":
        serializer = BlogPostSerializer(post,data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            
            data = {
            "message":"success",
            "data":serializer.data
            }
    
            return Response(data, status=status.HTTP_202_ACCEPTED)
        else:
            data = {
            "message":"failed",
            "error":serializer.errors
            }
    
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        post.delete()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)