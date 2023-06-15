from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Overview(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dashboard/overview.html')
    
class Profile(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dashboard/profile.html')
    

class SchoolFees(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dashboard/school-fees.html')
    

class HostelAllocation(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dashboard/hostel-allocation.html')
    

class CourseRegistration(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dashboard/course-registration.html')
    

class Results(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dashboard/results.html')
    

class ELearning(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dashboard/e-learning.html')
    

class Payments(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dashboard/payments.html')
    

class Clearance(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dashboard/clearance.html')