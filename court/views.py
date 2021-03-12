from django.shortcuts import render

from ourfirm.forms import CallMeForm 

from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template


def toc(request):
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

    template_name = "court/toc.html"
    return render(request, "court/courtmain.html", {'form': form_class, 'template_name':template_name})

def expect(request):
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

    template_name = "court/expect.html"
    return render(request, "court/courtmain.html", {'form': form_class, 'template_name':template_name})

def fightthecharges(request):
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

    template_name = "court/trial.html"
    return render(request, "court/courtmain.html", {'form': form_class, 'template_name':template_name})

def evidence(request):
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

    template_name = "court/evidence.html"
    return render(request, "court/courtmain.html", {'form': form_class, 'template_name':template_name})

def delay(request):
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

    template_name = "court/delay.html"
    return render(request, "court/courtmain.html", {'form': form_class, 'template_name':template_name})

