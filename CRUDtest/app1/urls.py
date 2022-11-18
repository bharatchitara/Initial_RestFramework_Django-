from django.contrib import admin
from django.urls import path
from app1 import views
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('docs', include_docs_urls(title='My API title')),
    path('first',views.firstRequest)
    
]
