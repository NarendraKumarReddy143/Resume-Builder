from django.shortcuts import render,redirect
from newresume.forms import UserForm,SigninForm,LoginForm
from django.http import HttpResponse
from newresume.models import SignIn,LogIn
from django.contrib.auth import authenticate
from reportlab.pdfgen import canvas


# Create your views here.

def newResume(request):
    form=UserForm
    values={'form':form}
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return homepage(request)

    return render(request,'newresume/newresume.html',values)


def signin(request):
    form1=SigninForm
    dict1={'form1':form1}
    if request.method=='POST':
        form1=SigninForm(request.POST)
        if form1.is_valid():
            na=form1.cleaned_data['name1']
            mail=form1.cleaned_data['mail']
            password3 = form1.cleaned_data['password']
            password4= form1.cleaned_data['password1']
            if SignIn.objects.filter(mail=mail).exists():
                return HttpResponse("Email already exists.Please click on log in to continue")
                
            if password3==password4:
                form1.save()
                return redirect('/newresume')

            else:
                return HttpResponse("password didnt match")
    return render(request,'newresume/signin.html',dict1)

def login(request):
    form2=LoginForm
    dict2={'form2':form2}
    if request.method=='POST':
        form2=LoginForm(request.POST)
        if form2.is_valid():
            mail=request.POST['user_mail']
            password3=request.POST['user_password']
            user = authenticate(request, mail=mail, password3=password3)
            a=f"Email: {mail}"
            b=f"Password: {password3}"
            print(a,b)
            if user is  not None:
                form2.save()
                return redirect('/newresume')
            else:
                return HttpResponse('You did not have any account in Resume Bilder.Please Sign In to continue')
            
    return render(request,'newresume/login.html',dict2)




def homepage(request):
    return render(request,"index.html")

def generatepdf(request):
         
    name = request.POST.get('name')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    school = request.POST.get('school')
    degree=request.POST.get('degree')
    skills = request.POST.get('skills')
    about_you = request.POST.get('about_you')
    experience = request.POST.get('experience')
    

        # Create a HttpResponse object with PDF headers
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

    # Create a canvas object and draw the resume content
    p = canvas.Canvas(response)
    p.setFont("Helvetica", 12)
    p.drawString(100, 800, "Name: {}".format(name))
    p.drawString(100, 780, "Email: {}".format(email))
    p.drawString(100, 760, "Phone: {}".format(contact))
    p.drawString(100, 740, "School: {}".format(school))
    p.drawString(100, 720, "Degree: {}".format(degree))
    p.drawString(100, 700, "Skills: {}".format(skills))
    p.drawString(100, 680, "About_you: {}".format(about_you))
    p.drawString(100, 660, "Experience: {}".format(experience))
    p.showPage()
    p.save()

    return response
