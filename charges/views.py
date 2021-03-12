from django.shortcuts import render

from ourfirm.forms import CallMeForm 

from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template


def charges(request):
    return render(request, "menu.html")

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

    template_name='charges/assault.html'

    return render(request, "ourfirm/main.html", {'form': form_class, 'template_name':template_name })

def assaultwin(request):
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

    template_name='charges/assaultwin.html'
    return render(request, "ourfirm/main.html", {'form': form_class, 'template_name':template_name})

def failtocomply(request):
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

    template_name='charges/failtocomply.html'

    return render(request, "ourfirm/main.html", {'form': form_class, 'template_name':template_name})

def impaired(request):
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

    template_name='charges/impaired.html'

    return render(request, "ourfirm/main.html", {'form': form_class, 'template_name':template_name })


def impairedwin(request):
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

    template_name='charges/impairedwin.html' 
    return render(request, "ourfirm/main.html", {'form': form_class, 'template_name':template_name })

def mischief(request):
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
    
    template_name='charges/mischief.html'
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
   
    template_name='charges/theft.html'
    return render(request, "ourfirm/main.html", { 'form': form_class, 'template_name':template_name})

def theftwin(request):
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
    
    template_name='charges/theftwin.html'
    return render(request, "ourfirm/main.html", { 'form': form_class, 'template_name':template_name})

def utteringthreats(request):
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

    template_name='charges/utteringthreats.html'
    
    return render(request, "ourfirm/main.html", { 'form': form_class, 'template_name':template_name})