from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'website/index.html')


def contact_view():
    pass


def about_view():
    pass




def licenses_view():
    pass