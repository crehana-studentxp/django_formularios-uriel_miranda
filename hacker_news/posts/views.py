from django.shortcuts import render
from .models import Post,Job
# Create your views here.
def home(request):
    return render(request, 'posts/home.html',{
        "news": Post.objects.all()
    })

def jobs(request):
    return render(request,'posts/jobs.html',{
        "jobs": Job.objects.all()
    })