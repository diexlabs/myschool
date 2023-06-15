from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.Overview.as_view(), name='overview'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('school-fees/', views.SchoolFees.as_view(), name='school_fees'),
    path('hostel-allocation/', views.HostelAllocation.as_view(), name='hostel_allocation'),
    path('course-registration/', views.CourseRegistration.as_view(), name='course_registration'),
    path('results/', views.Results.as_view(), name='results'),
    path('e-learning/', views.ELearning.as_view(), name='elearning'),
    path('payments/', views.Payments.as_view(), name='payments'),
    path('clearance/', views.Clearance.as_view(), name='clearance'),
]
