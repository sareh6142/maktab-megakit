from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'website/index.html')


def contact_view(request):
    return render(request,'website/contact.html')


def about_view(request):
    return render(request,'website/about.html')




def project_view(request):
    return render(request,'website/project.html')



def service_view(request):
    return render(request,'website/service.html')