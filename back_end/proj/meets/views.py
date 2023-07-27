from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from .serialize import ThemeSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response

class UserLogin(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        user = authenticate(request, phone_number=phone_number, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Ви успішно увійшли!"})
        else:
            return Response({"message": "Помилка автентифікації."}, status=401)
class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'
class EventSerializer(serializers.ModelSerializer):
    theme = ThemeSerializer()  # Використання ThemeSerializer для поля theme

    class Meta:
        model = Event
        fields = ['title', 'description', 'date_time', 'theme']

class AllThemes(APIView):
    def get(self, request, *args, **kwargs):
        all_themes = Theme.objects.all()
        serialized_theme = ThemeSerializer(all_themes, many=True)
        return Response(serialized_theme.data)
class AllEvents(APIView):
    def get(self, *args, **kwargs):
        all_events = Event.objects.all()
        serialized_event = EventSerializer(all_events, many=True)
        return Response(serialized_event.data)
