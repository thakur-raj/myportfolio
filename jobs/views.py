from django.shortcuts import render
from jobs.models import Job

# Create your views here.

def home(request):
    jobs = Job.objects
    print(jobs)
    return render(request,'jobs/home.html',{'jobs':jobs})
