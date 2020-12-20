# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response

import json
from .functions import classify_passenger, load_model

class get_classification(APIView):
  def post(self, request):
    model = load_model('./api/titanic_model.sav')
    data = request.data
    prediction = classify_passenger(model = model, data = data)
    return Response(prediction)

# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse
# @csrf_exempt
# def a(request):
#     if request.method == "POST":
#         print('\n'*10)
#         print('p')
#         print('\n'*10)
#     return HttpResponse('Oh')
