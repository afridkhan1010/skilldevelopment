from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TagSerializer,LinkSerializer,CommentSerializer,ReportsSerializer,commentsrepresentation,HotDashboardserializer
from django.views.generic import View
import json
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Tag,BunchOfLinks,CommentsModel,ReportsModel


# Create your views here.
class Simple(APIView):   #getting taglist
    def get(self, request):
        tags=Tag.objects.all()
        serializer=TagSerializer(tags,many=True)
        return Response(serializer.data)

    def post(self, request,  *args, **kwargs):
        data = JSONParser().parse(request)
    
        serializer = TagSerializer(data=data)
        print('data posted')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Update_det(APIView):    
    def put(self, request,id):
        data = JSONParser().parse(request)

        update=get_object_or_404(Tag,pk=id)
        update_detail = TagSerializer(
                update, data=data)
        if update_detail.is_valid():
            update_detail.save()
            return Response(update_detail.data, status=status.HTTP_200_OK)
        return Response(update_detail.errors, status=status.HTTP_400_BAD_REQUEST)

class AllLinks(APIView):
    def get(self,request):
        print("get all links")
        
        links=BunchOfLinks.objects.all()
        print(links)
        serial_link=LinkSerializer(links,many=True)
        return Response(serial_link.data)

    def post(self,request,*args,**kwargs):
        Plinks=JSONParser().parse(request)
        serial_link=LinkSerializer(data=Plinks)
        if serial_link.is_valid():
            serial_link.save()
            
            return Response(serial_link.data, status=status.HTTP_201_CREATED)
        return Response(serial_link.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        links=JSONParser().parse(request)
        serial_link=LinkSerializer(links=links)
        return Response(serial_link.data,status=status.HTTP_200_OK)
class Links(APIView):
    def get(self,request, id):
        print("inside get method of  particular link")
     
        links=BunchOfLinks.objects.filter(pk=id) 
        serial_link=LinkSerializer(links,many=True)
        return Response(serial_link.data)

    def delete(self,request,id):
        links=JSONParser().parse(request)
        serial_link=LinkSerializer(links=links)
        return Response(serial_link.data,status=status.HTTP_200_OK)

    def put(self, request,id):
        data = JSONParser().parse(request)

        update=get_object_or_404(BunchOfLinks,pk=id)
        update_detail = LinkSerializer(
                update, data=data)
        if update_detail.is_valid():
            update_detail.save()
            return Response(update_detail.data, status=status.HTTP_200_OK)
        return Response(update_detail.errors, status=status.HTTP_400_BAD_REQUEST)





class AllComments(APIView):
    def get(self, request):
        print('inside all comments section')
        getcomments=CommentsModel.objects.all()
        print(getcomments)

        serial_comment=CommentSerializer(getcomments,many=True)
        print(getcomments.all)
        print(serial_comment.data)
        return Response(serial_comment.data)
    
    def delete(self,request):
        links=JSONParser().parse(request)
        serial_link=CommentSerializer(links=links)
        return Response(serial_link.data,status=status.HTTP_200_OK)    
class DashBoard(APIView):

    def get(self, request):
        print("inside view dash")
        hotlinks= CommentsModel.objects.all()
        print(hotlinks)
        

        serializer = HotDashboardserializer(hotlinks)
        print("----*"*30)
        print("zzzzzzzz")
        # print(serializer.data)
        return Response(serializer.data)

class Comments(APIView):
    def get(self, request,id):
        print('inside comments section by ID')
        getcomments=CommentsModel.objects.filter(id=id)

        serial_comment=commentsrepresentation(getcomments,many=True)
        print(getcomments.all)
        return Response(serial_comment.data)
    
    

    def post(self, request,*args,**kwargs):
        pcomments=JSONParser().parse(request)
        serial_comment=CommentSerializer(data=pcomments)
        
        if serial_comment.is_valid():
            serial_comment.save()
            return Response(serial_comment.data, status=status.HTTP_201_CREATED)
        return Response(serial_comment.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        
        print("delete Comments by id")
        record = get_object_or_404(CommentsModel, pk=id)
        print(record)
        
        record.delete()
        serial_comment=CommentSerializer(links=record)
        return Response(serial_comment.data,status=status.HTTP_200_OK) 
        # return Response(serializer.data)

    def put(self, request,id):

        data = JSONParser().parse(request)
        print(data)
        update=get_object_or_404(CommentsModel,pk=id)
        print(update)
        print("came back with data")


        update_detail = CommentSerializer(
                update, data=data)
        print(update_detail)
        if update_detail.is_valid():
            update_detail.save()
            return Response(update_detail.data, status=status.HTTP_200_OK)
        return Response(update_detail.errors, status=status.HTTP_400_BAD_REQUEST)


# class Commentsonly(APIView):
#     def get(self, request,id):
#         print('inside commentsonly section')
#         # getcomments=CommentsModel.objects.all()
#         getcomments=CommentsModel.objects.filter(bunch_of_links_id=id)

#         serial_comment=commentsrepresentation(getcomments,many=True)
#         print(getcomments.all)
#         return Response(serial_comment.data)
    
    
class Reports(APIView):
    def get(self, request,id):
        # getreports=ReportsModel.objects.all()
        getreports=ReportsModel.objects.filter(bunch_of_links_id=id)
        serial_report=ReportsSerializer(getreports,many=True)
        return Response(serial_report.data)
    

    def post(self, request,*args,**kwargs):
        print("in post report views")
        preports=JSONParser().parse(request)
        print("123")
        print(preports)
        serial_report=ReportsSerializer(data=preports)
        
        print("12345")
        print(serial_report)
        if serial_report.is_valid():
            serial_report.save()
            return Response(serial_report.data, status=status.HTTP_201_CREATED)
        return Response(serial_report.data, status=status.HTTP_204_NO_CONTENT)