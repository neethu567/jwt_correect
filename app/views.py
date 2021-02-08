from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework.permissions import IsAuthenticated #
from rest_framework.response import Response #
from rest_framework.views import APIView


class Sample_print(View):

    def get(self,request):
        return HttpResponse("Login to app")

class login(APIView):
    permission_classes = [IsAuthenticated] #
    def get(self,request):
        var1={"name":"neethu"}
        return Response(var1)



