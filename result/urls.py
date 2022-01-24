
from django.urls import path 

from result.views  import GetResultView, Home


urlpatterns = [ 
    path('',GetResultView.as_view(),name='result'),
    path('home/',Home, name='home')
]

