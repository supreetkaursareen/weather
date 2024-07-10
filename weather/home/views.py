# views.py

from django.shortcuts import render, redirect
from .models import User
from .forms import UserLoginForm, WeatherInfoForm
import requests


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # Process login form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Authenticate user (dummy check for demonstration)
            user = User.objects.filter(username=username, password=password).first()
            if user:
                return redirect('weather_info')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password.'})
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


def weather_info(request):
    if request.method == 'POST':
        form = WeatherInfoForm(request.POST)
        if form.is_valid():
            # Process weather info form
            city = form.cleaned_data['city']
            api_key = '3477b60ff54f20f7c03c469bca562885'
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

            try:
                data = requests.get(url).json()

                if data['cod'] == 200:  # Successful API call
                    # Save weather info to database (optional)
                    # Display weather info
                    payload = {
                        'city': data['name'],
                        'weather': data['weather'][0]['main'],
                        'temperature': round(data['main']['temp'] - 273.15, 2),
                        'pressure': data['main']['pressure'],
                        'humidity': data['main']['humidity']
                    }
                    return render(request, 'weather_info.html', {'data': payload})
                else:
                    error = f'Error: {data["message"]}'
                    return render(request, 'weather_info.html', {'error': error})

            except Exception as e:
                error = f'Error fetching weather data: {str(e)}'
                return render(request, 'weather_info.html', {'error': error})
    else:
        form = WeatherInfoForm()

    return render(request, 'weather_info.html', {'form': form})
