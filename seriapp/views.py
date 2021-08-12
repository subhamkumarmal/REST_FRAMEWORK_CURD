from django.shortcuts import render
from .serializers import StudentSerializers
from .models import Students
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.


# ******************* FOR ALL QUERY FUNCTION BASED VIEWS ****************
# @api_view(['GET','POST'])
# def StudentsDetails(request):
#     if request.method == 'GET':
#         getObj=Students.objects.all()
#         seri=StudentSerializers(getObj,many=True)
#         return Response(seri.data)
#
#     elif request.method == "POST":
#         setData=StudentSerializers(data=request.data)
#         if setData.is_valid():
#             setData.save()
#             return Response(setData.data,status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)


# ***************** WITH THE HELP OF ID FUNCTION BASED OPERATIONS*********************
# @api_view(['GET','POST','PATCH'])
# def StudentsDetails(request,pk):
#     if request.method == 'GET':
#         getObj=Students.objects.get(id=pk)
#         seri=StudentSerializers(getObj)
#         return Response(seri.data)
#
#     elif request.method == "POST":
#         setData=StudentSerializers(data=request.data)
#         if setData.is_valid():
#             setData.save()
#             return Response(setData.data,status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#     elif request.method=='PATCH':
#         getObj=Students.objects.get(id=pk)
#         serializer = StudentSerializers(getObj,
#                                            data=request.data,
#                                            partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

# ************** CLASS BASED VIEW WITHOUT ID********************

class StudentsDetails(APIView):
    def get_object(self,pk):
        try:
            return Students.objects.get(id=pk)
        except Students.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        obj=self.get_object(pk)
        seri=StudentSerializers(obj)
        return Response(seri.data)
    def post(self,request,pk):
        obj=StudentSerializers(data=request.data)
        if obj.is_valid():
            obj.save()
            return Response(obj.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        obj=self.get_object(pk)
        seri=StudentSerializers(obj,data=request.data,partial=True)
        if seri.is_valid():
            seri.save()
            return Response(seri.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)





