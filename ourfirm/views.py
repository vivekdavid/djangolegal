from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.core.mail import EmailMessage

from django.template import Context
from django.template.loader import get_template

from . forms import CallMeForm


def google(request):
    return render(request,'oufrim/google.html')

def home(request):

    head = "647 409 2741"
    return render(request, 'ourfirm/home.html', {'head':head,})

def about(request):
    form_class = CallMeForm
    contact_name = request.POST.get('contact_name','')
    contact_phone = request.POST.get('contact_phone','')
    if request.method =='POST':
        form = form_class(data=request.POST)
        if form.is_valid():       
            contact_name = request.POST.get('contact_name','')
            contact_phone = request.POST.get('contact_phone','')
            
            context =({
                'contact_name':contact_name,
                'contact_phone':contact_phone,
                })

            content= get_template('ourfirm/call_me.txt').render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                'vivekdavidv@gmail.com',
                ['vivekdavidv@gmail.com'],
                
            )
            email.send()
            template_name = 'sent.html'
            return render(request, 'ourfirm/contact.html', { 'form': form_class,  'template_name':template_name })

    template_name = "about.html"
    return render(request, "ourfirm/main.html", {'form': form_class, 'template_name':template_name})

def sent(request):
    template_name='sent.html'
    return render (request, 'ourfirm/contact.html', {'template_name':template_name,})


def callme(request):
    form_class = CallMeForm
    contact_name = request.POST.get('contact_name','')
    contact_phone = request.POST.get('contact_phone','')
    if request.method =='POST':
        form = form_class(data=request.POST)
        if form.is_valid():       
            contact_name = request.POST.get('contact_name','')
            contact_phone = request.POST.get('contact_phone','')
            
            context =({
                'contact_name':contact_name,
                'contact_phone':contact_phone,
                })

            content= get_template('ourfirm/call_me.txt').render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                'vivekdavidv@gmail.com',
                ['vivekdavidv@gmail.com'],
                
            )
            email.send()
            template_name = 'sent.html'
            return render(request, 'ourfirm/contact.html', { 'form': form_class,  'template_name':template_name })
    template_name ="call-me.html"
    return render(request, 'ourfirm/contact.html', {'form': form_class, 'template_name':template_name })
	
def assault(request):
    form_class = CallMeForm
    contact_name = request.POST.get('contact_name','')
    contact_phone = request.POST.get('contact_phone','')
    if request.method =='POST':
        form = form_class(data=request.POST)
        if form.is_valid():       
            contact_name = request.POST.get('contact_name','')
            contact_phone = request.POST.get('contact_phone','')
            
            context =({
                'contact_name':contact_name,
                'contact_phone':contact_phone,
                })

            content= get_template('ourfirm/call_me.txt').render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                'vivekdavidv@gmail.com',
                ['vivekdavidv@gmail.com'],
                
            )
            email.send()
            template_name = 'sent.html'
            return render(request, 'ourfirm/contact.html', { 'form': form_class,  'template_name':template_name })

    template_name = "assaultlawyer.html"
    return render(request, "ourfirm/main.html", {'form': form_class, 'template_name':template_name})

	
def theft(request):
    form_class = CallMeForm
    contact_name = request.POST.get('contact_name','')
    contact_phone = request.POST.get('contact_phone','')
    if request.method =='POST':
        form = form_class(data=request.POST)
        if form.is_valid():       
            contact_name = request.POST.get('contact_name','')
            contact_phone = request.POST.get('contact_phone','')
            
            context =({
                'contact_name':contact_name,
                'contact_phone':contact_phone,
                })

            content= get_template('ourfirm/call_me.txt').render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                'vivekdavidv@gmail.com',
                ['vivekdavidv@gmail.com'],
                
            )
            email.send()
            template_name = 'sent.html'
            return render(request, 'ourfirm/contact.html', { 'form': form_class,  'template_name':template_name })

    template_name = "theftlawyer.html"
    return render(request, "ourfirm/main.html", {'form': form_class, 'template_name':template_name})

	
def legalaid(request):
    form_class = CallMeForm
    contact_name = request.POST.get('contact_name','')
    contact_phone = request.POST.get('contact_phone','')
    if request.method =='POST':
        form = form_class(data=request.POST)
        if form.is_valid():       
            contact_name = request.POST.get('contact_name','')
            contact_phone = request.POST.get('contact_phone','')
            
            context =({
                'contact_name':contact_name,
                'contact_phone':contact_phone,
                })

            content= get_template('ourfirm/call_me.txt').render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                'vivekdavidv@gmail.com',
                ['vivekdavidv@gmail.com'],
                
            )
            email.send()
            template_name = 'sent.html'
            return render(request, 'ourfirm/contact.html', { 'form': form_class,  'template_name':template_name })

    template_name = "legalaid.html"
    return render(request, "ourfirm/main.html", {'form': form_class, 'template_name':template_name})