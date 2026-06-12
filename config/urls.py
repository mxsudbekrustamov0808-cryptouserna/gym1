"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <html>
    <head>
        <title>API Control Panel</title>
    </head>
    <body style="
        background:#0d0d0d;
        display:flex;
        justify-content:center;
        align-items:center;
        height:100vh;
        margin:0;
        font-family:Segoe UI;
    ">
        <div style="
            width:700px;
            text-align:center;
            padding:40px;
            border:3px solid #ff6a00;
            border-radius:20px;
            background:#171717;
            box-shadow:0 0 30px rgba(255,106,0,.5);
        ">
            <h1 style="color:#ff6a00;">
                 API CONTROL PANEL
            </h1>

            <p style="color:white;">
                #Server muvaffaqiyatli ishga tushdi
            </p>

            <div style="margin-top:30px;">

                <a href="/swagger/" style="
                    display:inline-block;
                    padding:15px 25px;
                    margin:10px;
                    background:#ff6a00;
                    color:white;
                    text-decoration:none;
                    border-radius:10px;
                ">Swagger UI</a>

                <a href="/redoc/" style="
                    display:inline-block;
                    padding:15px 25px;
                    margin:10px;
                    background:#ffffff;
                    color:black;
                    text-decoration:none;
                    border-radius:10px;
                ">ReDoc</a>

                <a href="/dashboard/" style="
                    display:inline-block;
                    padding:15px 25px;
                    margin:10px;
                    background:#444;
                    color:white;
                    text-decoration:none;
                    border-radius:10px;
                ">Dashboard</a>

                <a href="/check-in/" style="
                    display:inline-block;
                    padding:15px 25px;
                    margin:10px;
                    background:#28a745;
                    color:white;
                    text-decoration:none;
                    border-radius:10px;
                ">Check-In</a>

                <a href="/admin/" style="
                    display:inline-block;
                    padding:15px 25px;
                    margin:10px;
                    background:#dc3545;
                    color:white;
                    text-decoration:none;
                    border-radius:10px;
                ">Admin Panel</a>

            </div>
        </div>
    </body>
    </html>
    """)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('subscriptions.urls')),
    path('', home, name='home'),
]
