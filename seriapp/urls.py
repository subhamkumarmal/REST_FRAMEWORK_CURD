from django.urls import path
from .views import StudentsDetails

urlpatterns=[
    # path('<int:pk>/',StudentsDetails,name='studentsdetials'),
    # path('',StudentsDetails,name='studentsdetials')

    path('<int:pk>/',StudentsDetails.as_view(),name="studentsdetails")
]