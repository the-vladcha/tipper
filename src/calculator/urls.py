from django.urls import path
from calculator.views import Calculator

urlpatterns = [
    path('', Calculator.as_view(), name='calculator'),
    # path('', Result.as_view(), name='calculator'),
]
