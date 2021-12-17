from django.urls import path 

from result.views  import GetResultView


urlpatterns = [ 
    path('',GetResultView.as_view(),name='result')
]

