from django.shortcuts import render
from .forms import ContactForm,NewsletterForm
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib import messages


# Create your views here.
def home_view(request):
    return render(request,"website/index.html")




def contact_view(request):
    if request.method == 'POST':
        updated_request = request.POST.copy()
        if updated_request.get('subject') == ' ':
            updated_request.setNUll('subject')
            #updated_request.update({'subject': " "})
        Contact_Form = ContactForm(updated_request)
        #form = Contact_Form(request.POST)
        if Contact_Form.is_valid():
            action = Contact_Form.save(commit=False)
            action.name = 'unknown'
            action.save()
            messages.add_message(request,messages.SUCCESS,'OK!')
        else:
            messages.add_message(request,messages.ERROR,'NOK!')
    form = ContactForm()
    return render(request,"website/Contact.html",{'form':form})
    


def about_view(request):
    return render(request,'website/about.html')




def project_view(request):
    return render(request,'website/project.html')



def service_view(request):
    return render(request,'website/service.html')

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'OK!')
        else:
            messages.add_message(request,messages.ERROR,'NOK!')
        return HttpResponseRedirect('/')

            
    else:
        return HttpResponseRedirect('/')
        
            
   
    