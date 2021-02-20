from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.apisend),
    path('post/', views.apipost),
    path('formatted/',views.FormatList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)