from django.shortcuts import render,redirect
from .models import Cu_User,CustomUser,EmailHistory,CFOhistory,CTOhistory,CPOhistory,CROhistory,BDEhistory,GMhistory,GMhistory1,Placehistory,Academichistory,Projecthistory,HRhistory,Students,Tutorhistory,Studenthistory,SHhistory,Accountshistory,Techhistory,CPOhistory1,Placeteamhistory,Projectcohistory,HREhistory,Inboundhistory
from django.contrib.auth import authenticate, logout, login
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
def reg(request):
    msg=""
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        uname=request.POST['uname']
        password=request.POST['password']
        department=request.POST['department']
        try:
            u=CustomUser.objects.create_user(username=uname,password=password)
            u.save()
            user=Cu_User.objects.create(Name=name,Phone=phone,Address=address,Email=email,Uname=uname,password=password,Department=department,user=u)
            user.save()
            return redirect("/login/")
        except:
            msg="Username already existed"
    return render(request,"reg.html",{"msg":msg})
def login(request):
    msg=""
    if request.POST:
        uName=request.POST['uname']
        password=request.POST['password']
        user=authenticate(username=uName,password=password)
        if user is None:
            msg="Invalid login"
        else:
          
            if user.userType=="admin":
                request.session["id"]=user.id
                return redirect("/adminhome/")
            
            else:
                try:
                    a = Cu_User.objects.get(Uname=uName)
                    department = a.Department
                    if department == "GM":
                        request.session["id"]=a.id
                        return redirect('/GMhome/')
                    elif department == "BDE":
                        request.session["id"]=a.id
                        return redirect('/BDEhome/')
                    elif department == "SH":  # Python is case-sensitive. Make sure these match exactly.
                        request.session["id"]=a.id
                        return redirect('/SHhome/')
                    elif department == "AGM":  # Same as above, watch your case sensitivity.
                        request.session["id"]=a.id
                        return redirect('/AGMhome/')
                    elif department == "R&D Dpt":  # Same as above, watch your case sensitivity.
                        request.session["id"]=a.id
                        return redirect('/RDhome/')
                    elif department == "CFO":  # Same as above, watch your case sensitivity.
                        request.session["id"]=a.id
                        return redirect('/CFOhome/')
                    elif department == "Accounts team":  # Same as above, watch your case sensitivity.
                        request.session["id"]=a.id
                        return redirect('/ACCteam/')
                    elif department == "CTO":  # Same as above, watch your case sensitivity.
                        request.session["id"]=a.id
                        return redirect('/CTOhome/')
                    elif department == "Technical team":  # Same as above, watch your case sensitivity.
                        request.session["id"]=a.id
                        return redirect('/Techteam/')
                    elif department == "CPO":  # Same as above, watch your case sensitivity.
                        request.session["id"]=a.id
                        return redirect('/CPOhome/')
                    elif department == "Product team":  # Same as above, watch your case sensitivity.
                        request.session["id"]=a.id
                        return redirect('/Proteam/')
                    elif department == "Placement head":  # Same as above, watch your case sensitivity.
                        request.session["id"]=a.id
                        return redirect('/Placehead/')
                    elif department == "Placement team":  # Same as above, watch your case sensitivity.
                        request.session["id"]=a.id
                        return redirect('/Placeteam/')
                    elif department == "Academic head":  # Same as above, watch your case sensitivity.
                        request.session["id"]=a.id
                        return redirect('/Academichead/')
                    elif department == "Full time tutor":  # Same as above, watch your case sensitivity.
                        request.session["id"]=a.id
                        return redirect('/Fulltutor/')
                    elif department == "Freelance tutor":  # Same as above, watch your case sensitivity.
                        request.session["id"]=a.id
                        return redirect('/Freetutor/')
                    elif department == "Project head":  # Same as above, watch your case sensitivity.
                        request.session["id"]=a.id
                        return redirect('/Prohead/')
                    elif department == "Project coordinator":  # Same as above, watch your case sensitivity.
                        request.session["id"]=a.id
                        return redirect('/Projectcoordinator/')
                    elif department == "HR":  # Same as above, watch your case sensitivity.
                        request.session["id"]=a.id
                        return redirect('/HRhome/')
                    elif department == "HRE":  # Same as above, watch your case sensitivity.
                        request.session["id"]=a.id
                        return redirect('/HREhome/')
                    elif department == "CRO":  # Same as above, watch your case sensitivity.
                        request.session["id"]=a.id
                        return redirect('/CROhome/')
                    elif department == "Inbound team":  # Same as above, watch your case sensitivity.
                        request.session["id"]=a.id
                        return redirect('/Inbteam/')

                except Cu_User.DoesNotExist:
                # Handle case where the user doesn't exist in your custom user table.
                    msg="Invalid login"
            
    return render(request,"login.html",{"msg":msg})
def adminhome(request):
    return render(request,"adminhome.html")
def GMhome(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"GMhome.html",{"cust":cust})
def BDEhome(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"BDEhome.html",{"cust":cust})
def SHhome(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"SHhome.html",{"cust":cust})
def AGMhome(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"AGMhome.html",{"cust":cust})
def RDhome(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"R&Dhome.html",{"cust":cust})
def CFOhome(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"CFOhome.html",{"cust":cust})
def ACCteam(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"ACCteam.html",{"cust":cust})
def CTOhome(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"CTOhome.html",{"cust":cust})
def Techteam(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"Techteam.html",{"cust":cust})
def CPOhome(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"CPOhome.html",{"cust":cust})
def Proteam(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"Productteam.html",{"cust":cust})
def Placehead(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"Placementhead.html",{"cust":cust})
def Placeteam(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"Placementteam.html",{"cust":cust})
def Academichead(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"Academichead.html",{"cust":cust})
def Fulltutor(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"Fulltimetutor.html",{"cust":cust})
def Freetutor(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"Freelancetutor.html",{"cust":cust})
def Prohead(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"Projecthead.html",{"cust":cust})
def Projectcoordinator(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"Projectcoordinator.html",{"cust":cust})
def HRhome(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"HRhome.html",{"cust":cust})
def HREhome(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"HREhome.html",{"cust":cust})
def CROhome(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"CROhome.html",{"cust":cust})
def Inbteam(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        customer=Cu_User.objects.get(id=custId)
        customer.Name=name
        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"Inboundteam.html",{"cust":cust})
def viewdetail1(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail1.html",{"cust":cust})
def viewusers1(request):
    cust=Cu_User.objects.exclude(Department="GM").order_by('-regDte')
    return render(request,"viewusers1.html",{"cust":cust})
def deleteuser(request,id):
    a=Cu_User.objects.get(id=id)
    a.delete()
    return redirect('/viewusers1/')
def update1(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail1/")
    return render(request,"update1.html",{"cust":cust})


def sendmailtoall1(request):
    users = Cu_User.objects.exclude(Department="GM")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: GM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            EmailHistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess3/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request, "sendmailtoall1.html")
def mailhistoryall(request):
    email_histories = EmailHistory.objects.all().order_by('-sent_at')
    return render(request,"mailhistoryall.html",{"email_histories":email_histories})
def mailtocfo(request):
    users = Cu_User.objects.filter(Department="CFO")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: GM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            CFOhistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess3/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"mailtocfo.html")
def cfohistory(request):
    email_histories =CFOhistory.objects.all().order_by('-sent_at')
    return render(request,"cfohistory.html",{"email_histories":email_histories})
def sendmailtocto(request):
    users = Cu_User.objects.filter(Department="CTO")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: GM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            CTOhistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess3/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailtocto.html")
def ctohistory(request):
    email_histories =CTOhistory.objects.all().order_by('-sent_at')
    return render(request,"ctohistory.html",{"email_histories":email_histories})
def sendmailtocpo(request):
    users = Cu_User.objects.filter(Department="CPO")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: GM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            CPOhistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess3/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailtocpo.html")
def cpohistory(request):
    email_histories =CPOhistory.objects.all().order_by('-sent_at')
    return render(request,"cpohistory.html",{"email_histories":email_histories})
def sendmailtobde(request):
    users = Cu_User.objects.filter(Department="BDE")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: GM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )
        

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            BDEhistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess3/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailtobde.html")
def bdehistory(request):
    email_histories =BDEhistory.objects.all().order_by('-sent_at')
    return render(request,"bdehistory.html",{"email_histories":email_histories})
def sendmailplacementhead(request):
    users = Cu_User.objects.filter(Department="Placement head")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: GM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            Placehistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess3/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailplacementhead.html")
def placementheadhistory(request):
    email_histories =Placehistory.objects.all().order_by('-sent_at')
    return render(request,"placementheadhistory.html",{"email_histories":email_histories})
def sendmailtoacademichead(request):
    users = Cu_User.objects.filter(Department="Academic head")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: GM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            Academichistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess3/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailtoacademichead.html")
def academicheadhistory(request):
    email_histories =Academichistory.objects.all().order_by('-sent_at')
    return render(request,"academicheadhistory.html",{"email_histories":email_histories})
def sendmailtoprojecthead(request):
    users = Cu_User.objects.filter(Department="Project head")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: GM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            Projecthistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess3/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailtoprojecthead.html")
def projectheadhistory(request):
    email_histories =Projecthistory.objects.all().order_by('-sent_at')
    return render(request,"projectheadhistory.html",{"email_histories":email_histories})
def sendmailtohr(request):
    users = Cu_User.objects.filter(Department="HR")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: GM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            HRhistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess3/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailtohr.html")
def hrhistory(request):
    email_histories =HRhistory.objects.all().order_by('-sent_at')
    return render(request,"hrhistory.html",{"email_histories":email_histories})
def deletebde(request,id):
    a=BDEhistory.objects.get(id=id)
    a.delete()
    return redirect('/bdehistory/')
def deleteall(request,id):
    a=EmailHistory.objects.get(id=id)
    a.delete()
    return redirect('/mailhistoryall/')
def deletecto(request,id):
    a=CTOhistory.objects.get(id=id)
    a.delete()
    return redirect('/ctohistory/')
def deletecfo(request,id):
    a=CFOhistory.objects.get(id=id)
    a.delete()
    return redirect('/cfohistory/')
def deletecpo(request,id):
    a=CPOhistory.objects.get(id=id)
    a.delete()
    return redirect('/cpohistory/')
def deleteplace(request,id):
    a=Placehistory.objects.get(id=id)
    a.delete()
    return redirect('/placementheadhistory/')
def deleteacademic(request,id):
    a=Academichistory.objects.get(id=id)
    a.delete()
    return redirect('/academicheadhistory/')
def deleteproject(request,id):
    a=Projecthistory.objects.get(id=id)
    a.delete()
    return redirect('/projectheadhistory/')
def deletehr(request,id):
    a=HRhistory.objects.get(id=id)
    a.delete()
    return redirect('/hrhistory/')
def forgotuser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
    
        email_exists = Cu_User.objects.filter(Email=email).first()
            
        if email_exists:
            name=email_exists.Name
            username = email_exists.Uname
            password = email_exists.password
            EmailTitle = "Recovery mail"
            email_body = f"Dear {name},\n\nYour username is: {username}\nYour password is: {password}\n\nPlease keep your login credentials secure and do not share them with anyone.\n\nBest regards,\nThe Mentorow Team"
            users = Cu_User.objects.filter(Email=email)
            email_addresses = [user.Email for user in users]
            # email_body = "from: Mentorow\n\n"  # Add your email body here
            email = EmailMessage(
                EmailTitle,
                email_body,
                'settings.EMAIL_HOST_USER',  # You should replace this with your actual email host user
                email_addresses,
            )
            email.send()  # Send the email
            return redirect('/login/')
        else:
            return HttpResponse("User doesn't exist")
    return render(request, "forgotuser.html")
def sendmailgm(request):
    users = Cu_User.objects.filter(Department="GM")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: BDE\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            GMhistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess2/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    return render(request,"sendmailgm.html")
def gmhistory(request):
    email_histories =GMhistory.objects.all().order_by('-sent_at')
    return render(request,"gmhistory.html",{"email_histories":email_histories})
def deletegm(request,id):
    a=GMhistory.objects.get(id=id)
    a.delete()
    return redirect('/gmhistory/')
def deletegm1(request,id):
    a=GMhistory1.objects.get(id=id)
    a.delete()
    return redirect('/gmhistory2/')
def viewdetail2(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail2.html",{"cust":cust})
def update2(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail2/")
    return render(request,"update2.html",{"cust":cust})
def sendmailtogm2(request):
    users = Cu_User.objects.filter(Department="GM")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername:ADMIN\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            GMhistory1.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess1/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    return render(request,"sendmailtogm2.html")
def gmhistory2(request):
    email_histories =GMhistory1.objects.all().order_by('-sent_at')
    return render(request,"gmhistory2.html",{"email_histories":email_histories})
def sendmailsuccess1(request):
    return render(request,"sendmailsuccess1.html")
def sendmailsuccess2(request):
    return render(request,"sendmailsuccess2.html")
def sendmailsuccess3(request):
    return render(request,"sendmailsuccess3.html")
def addstudents(request):
    msg=""
    if request.POST:
        name=request.POST['name']
        mob=request.POST['mob']
        address=request.POST['address']
        email=request.POST['email']
        course=request.POST['course']
        duration=request.POST['duration']
        student=Students.objects.create(Name=name,Mob=mob,Address=address,Email=email,Course=course,Duration=duration)
        student.save()
        msg="Student add successfully "
    return render(request,"addstudents.html",{"msg":msg})
def viewstudents(request):
    cust1=Students.objects.all().order_by('-regDte')
    
    return render(request,"viewstudents.html",{"cust1":cust1})
def deletestudent(request,id):
    a=Students.objects.get(id=id)
    a.delete()
    return redirect('/viewstudents/')
def sendmailtotutor(request):
    if request.method=='POST':
        sendmail=request.POST['sendmail']
        if sendmail=="Full time tutor":
            users = Cu_User.objects.filter(Department="Full time tutor")
            email_addresses = [user.Email for user in users]
    
            if request.method == 'POST':
                EmailTitle = request.POST['emailtitle'] 
                Message = request.POST['message']
                
                # Get list of files attached to the request
                files = request.FILES.getlist('files')
                
                email = EmailMessage(
                    EmailTitle,
                    f'sendername: Academic head\n\n{Message}',
                    'settings.EMAIL_HOST_USER',
                    email_addresses,
                )

                # Attach each file to the email
                for file in files:
                    email.attach(file.name, file.read(), file.content_type)

                try:
                    email.send()

                        # Save email to history
                    Tutorhistory.objects.create(
                    sender=settings.EMAIL_HOST_USER,
                    recipients=", ".join(email_addresses),
                    subject=EmailTitle,
                    message=Message,
                    tutortype=sendmail,
                    )
                    return redirect('/sendmailsuccess4/')
                except Exception as e:
                        # Handle email sending failure
                    return HttpResponse("Failed to send email", status=500)
        elif sendmail=="Freelance tutor":
            users = Cu_User.objects.filter(Department="Freelance tutor")
            email_addresses = [user.Email for user in users]
    
            if request.method == 'POST':
                EmailTitle = request.POST['emailtitle'] 
                Message = request.POST['message']
                
                # Get list of files attached to the request
                files = request.FILES.getlist('files')
                
                email = EmailMessage(
                    EmailTitle,
                    f'sendername: Academic head\n\n{Message}',
                    'settings.EMAIL_HOST_USER',
                    email_addresses,
                )

                # Attach each file to the email
                for file in files:
                    email.attach(file.name, file.read(), file.content_type)

                try:
                    email.send()

                        # Save email to history
                    Tutorhistory.objects.create(
                    sender=settings.EMAIL_HOST_USER,
                    recipients=", ".join(email_addresses),
                    subject=EmailTitle,
                    message=Message,
                    tutortype=sendmail,
                    )
                    return redirect('/sendmailsuccess4/')
                except Exception as e:
                        # Handle email sending failure
                    return HttpResponse("Failed to send email", status=500)

    return render(request,"sendmailtotutor.html")
def sendmailsuccess4(request):
    return render(request,"sendmailsuccess4.html")
def tutormailhistory(request):
    email_histories =Tutorhistory.objects.filter(tutortype="Full time tutor").order_by('-sent_at')
    return render(request,"tutormailhistory.html",{"email_histories":email_histories})
def tutormailhistory1(request):
    email_histories2 =Tutorhistory.objects.filter(tutortype="Freelance tutor").order_by('-sent_at')
    return render(request,"tutormailhistory1.html",{"email_histories2":email_histories2})
def deletetutorhistory(request,id):
    a=Tutorhistory.objects.get(id=id)
    a.delete()
    return redirect('/tutormailhistory/')
def deletetutorhistory1(request,id):
    a=Tutorhistory.objects.get(id=id)
    a.delete()
    return redirect('/tutormailhistory1/')
def viewdetail3(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail3.html",{"cust":cust})
def update3(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail3/")
    return render(request,"update3.html",{"cust":cust})
def viewstudent1(request):
    cust1=Students.objects.all().order_by('-regDte')
    
    return render(request,"viewstudent1.html",{"cust1":cust1})
def sendmailstudents(request):
    if request.method=='POST':
        sendmail=request.POST['sendmail']
        if sendmail=="Python":
            users =Students.objects.filter(Course="Python")
            email_addresses = [user.Email for user in users]
    
            if request.method == 'POST':
                EmailTitle = request.POST['emailtitle'] 
                Message = request.POST['message']
                
                # Get list of files attached to the request
                files = request.FILES.getlist('files')
                
                email = EmailMessage(
                    EmailTitle,
                    f'sendername: Tutor\n\n{Message}',
                    'settings.EMAIL_HOST_USER',
                    email_addresses,
                )

                # Attach each file to the email
                for file in files:
                    email.attach(file.name, file.read(), file.content_type)

                try:
                    email.send()

                        # Save email to history
                    Studenthistory.objects.create(
                    sender=settings.EMAIL_HOST_USER,
                    recipients=", ".join(email_addresses),
                    subject=EmailTitle,
                    message=Message,
                    Studentcourse=sendmail,
                    )
                    return redirect('/sendmailsuccess5/')
                except Exception as e:
                        # Handle email sending failure
                    return HttpResponse("Failed to send email", status=500)
        elif sendmail=="Data science":
            users =Students.objects.filter(Course="Data science")
            email_addresses = [user.Email for user in users]
    
            if request.method == 'POST':
                EmailTitle = request.POST['emailtitle'] 
                Message = request.POST['message']
                
                # Get list of files attached to the request
                files = request.FILES.getlist('files')
                
                email = EmailMessage(
                    EmailTitle,
                    f'sendername: Tutor\n\n{Message}',
                    'settings.EMAIL_HOST_USER',
                    email_addresses,
                )

                # Attach each file to the email
                for file in files:
                    email.attach(file.name, file.read(), file.content_type)

                try:
                    email.send()

                        # Save email to history
                    Studenthistory.objects.create(
                    sender=settings.EMAIL_HOST_USER,
                    recipients=", ".join(email_addresses),
                    subject=EmailTitle,
                    message=Message,
                    Studentcourse=sendmail,
                    )
                    return redirect('/sendmailsuccess5/')
                except Exception as e:
                        # Handle email sending failure
                    return HttpResponse("Failed to send email", status=500)

    
        elif sendmail=="MERN":
            users =Students.objects.filter(Course="MERN")
            email_addresses = [user.Email for user in users]
    
            if request.method == 'POST':
                EmailTitle = request.POST['emailtitle'] 
                Message = request.POST['message']
                
                # Get list of files attached to the request
                files = request.FILES.getlist('files')
                
                email = EmailMessage(
                    EmailTitle,
                    f'sendername: Tutor\n\n{Message}',
                    'settings.EMAIL_HOST_USER',
                    email_addresses,
                )

                # Attach each file to the email
                for file in files:
                    email.attach(file.name, file.read(), file.content_type)

                try:
                    email.send()

                        # Save email to history
                    Studenthistory.objects.create(
                    sender=settings.EMAIL_HOST_USER,
                    recipients=", ".join(email_addresses),
                    subject=EmailTitle,
                    message=Message,
                    Studentcourse=sendmail,
                    )
                    return redirect('/sendmailsuccess5/')
                except Exception as e:
                        # Handle email sending failure
                    return HttpResponse("Failed to send email", status=500)

    
        elif sendmail=="Digital marketing":
            users =Students.objects.filter(Course="Digital marketing")
            email_addresses = [user.Email for user in users]
    
            if request.method == 'POST':
                EmailTitle = request.POST['emailtitle'] 
                Message = request.POST['message']
                
                # Get list of files attached to the request
                files = request.FILES.getlist('files')
                
                email = EmailMessage(
                    EmailTitle,
                    f'sendername: Tutor\n\n{Message}',
                    'settings.EMAIL_HOST_USER',
                    email_addresses,
                )

                # Attach each file to the email
                for file in files:
                    email.attach(file.name, file.read(), file.content_type)

                try:
                    email.send()

                        # Save email to history
                    Studenthistory.objects.create(
                    sender=settings.EMAIL_HOST_USER,
                    recipients=", ".join(email_addresses),
                    subject=EmailTitle,
                    message=Message,
                    Studentcourse=sendmail,
                    )
                    return redirect('/sendmailsuccess5/')
                except Exception as e:
                        # Handle email sending failure
                    return HttpResponse("Failed to send email", status=500)

    
        
    return render(request,"sendmailstudents.html")
def studentmailhistory(request):
    email_histories =Studenthistory.objects.all().order_by('-sent_at')
    return render(request,"studentmailhistory.html",{"email_histories":email_histories})
def deletestudenthistory(request,id):
    a=Studenthistory.objects.get(id=id)
    a.delete()
    return redirect('/studentmailhistory/')
def sendmailsuccess5(request):
    return render(request,"sendmailsuccess5.html")
def viewusers2(request):
    cust=Cu_User.objects.exclude(Department="GM").exclude(Department="AGM").order_by('-regDte')
    return render(request,"viewusers2.html",{"cust":cust})
def deleteuser1(request,id):
    a=Cu_User.objects.get(id=id)
    a.delete()
    return redirect('/viewusers2/')
def sendmailtoall2(request):
    users = Cu_User.objects.exclude(Department="GM").exclude(Department="AGM")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: AGM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            EmailHistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess6/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request, "sendmailtoall2.html")
def mailhistoryall1(request):
    email_histories = EmailHistory.objects.all().order_by('-sent_at')
    return render(request,"mailhistoryall1.html",{"email_histories":email_histories})
def deleteall1(request,id):
    a=EmailHistory.objects.get(id=id)
    a.delete()
    return redirect('/mailhistoryall1/')
def sendmailtobde1(request):
    users = Cu_User.objects.filter(Department="BDE")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: AGM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )
        

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            BDEhistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess6/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailtobde1.html")
def bdehistory1(request):
    email_histories =BDEhistory.objects.all().order_by('-sent_at')
    return render(request,"bdehistory1.html",{"email_histories":email_histories})
def deletebde1(request,id):
    a=BDEhistory.objects.get(id=id)
    a.delete()
    return redirect('/bdehistory1/')
def mailtocfo1(request):
    users = Cu_User.objects.filter(Department="CFO")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: AGM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            CFOhistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess6/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"mailtocfo1.html")
def cfohistory1(request):
    email_histories =CFOhistory.objects.all().order_by('-sent_at')
    return render(request,"cfohistory1.html",{"email_histories":email_histories})
def deletecfo1(request,id):
    a=CFOhistory.objects.get(id=id)
    a.delete()
    return redirect('/cfohistory1/')
def sendmailtocto1(request):
    users = Cu_User.objects.filter(Department="CTO")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: AGM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            CTOhistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess6/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailtocto1.html")
def ctohistory1(request):
    email_histories =CTOhistory.objects.all().order_by('-sent_at')
    return render(request,"ctohistory1.html",{"email_histories":email_histories})
def deletecto1(request,id):
    a=CTOhistory.objects.get(id=id)
    a.delete()
    return redirect('/ctohistory1/')
def sendmailtocpo1(request):
    users = Cu_User.objects.filter(Department="CPO")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: AGM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            CPOhistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess6/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailtocpo1.html")
def cpohistory1(request):
    email_histories =CPOhistory.objects.all().order_by('-sent_at')
    return render(request,"cpohistory1.html",{"email_histories":email_histories})
def deletecpo1(request,id):
    a=CPOhistory.objects.get(id=id)
    a.delete()
    return redirect('/cpohistory1/')
def sendmailsuccess6(request):
    return render(request,"sendmailsuccess6.html")
def sendmailsuccess7(request):
    return render(request,"sendmailsuccess7.html")
def sendmailsuccess8(request):
    return render(request,"sendmailsuccess8.html")
def sendmailplacementhead1(request):
    users = Cu_User.objects.filter(Department="Placement head")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: AGM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            Placehistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess6/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailplacementhead1.html")
def placementheadhistory1(request):
    email_histories =Placehistory.objects.all().order_by('-sent_at')
    return render(request,"placementheadhistory1.html",{"email_histories":email_histories})
def deleteplace1(request,id):
    a=Placehistory.objects.get(id=id)
    a.delete()
    return redirect('/placementheadhistory1/')
def sendmailtoacademichead1(request):
    users = Cu_User.objects.filter(Department="Academic head")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: AGM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            Academichistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess6/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailtoacademichead1.html")
def academicheadhistory1(request):
    email_histories =Academichistory.objects.all().order_by('-sent_at')
    return render(request,"academicheadhistory1.html",{"email_histories":email_histories})
def deleteacademic1(request,id):
    a=Academichistory.objects.get(id=id)
    a.delete()
    return redirect('/academicheadhistory1/')
def sendmailtoprojecthead1(request):
    users = Cu_User.objects.filter(Department="Project head")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: AGM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            Projecthistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess6/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailtoprojecthead1.html")
def projectheadhistory1(request):
    email_histories =Projecthistory.objects.all().order_by('-sent_at')
    return render(request,"projectheadhistory1.html",{"email_histories":email_histories})
def deleteproject1(request,id):
    a=Projecthistory.objects.get(id=id)
    a.delete()
    return redirect('/projectheadhistory1/')
def sendmailtohr1(request):
    users = Cu_User.objects.filter(Department="HR")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: AGM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            HRhistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess6/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailtohr1.html")
def hrhistory1(request):
    email_histories =HRhistory.objects.all().order_by('-sent_at')
    return render(request,"hrhistory1.html",{"email_histories":email_histories})
def deletehr1(request,id):
    a=HRhistory.objects.get(id=id)
    a.delete()
    return redirect('/hrhistory1/')
def sendmailtosh(request):
    users = Cu_User.objects.filter(Department="SH")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: GM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            SHhistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess3/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailtosh.html")
def shhistory(request):
    email_histories =SHhistory.objects.all().order_by('-sent_at')
    return render(request,"shhistory.html",{"email_histories":email_histories})
def deletesh(request,id):
    a=SHhistory.objects.get(id=id)
    a.delete()
    return redirect('/shhistory/')
def sendmailtosh1(request):
    users = Cu_User.objects.filter(Department="SH")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: AGM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            SHhistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess6/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailtosh1.html")
def shhistory1(request):
    email_histories =SHhistory.objects.all().order_by('-sent_at')
    return render(request,"shhistory1.html",{"email_histories":email_histories})
def deletesh1(request,id):
    a=SHhistory.objects.get(id=id)
    a.delete()
    return redirect('/shhistory1/')
def viewdetail4(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail4.html",{"cust":cust})
def update4(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail4/")
    return render(request,"update4.html",{"cust":cust})
def sendmailtoaccountteam(request):
    users = Cu_User.objects.filter(Department="Accounts team")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: CFO\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            Accountshistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess7/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailtoaccountteam.html")
def accountsmailhistory(request):
    email_histories =Accountshistory.objects.all().order_by('-sent_at')
    return render(request,"accountsmailhistory.html",{"email_histories":email_histories})
def deleteaccountshistory(request,id):
    a=Accountshistory.objects.get(id=id)
    a.delete()
    return redirect('/accountsmailhistory/')
def viewdetail5(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail5.html",{"cust":cust})
def update5(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail5/")
    return render(request,"update5.html",{"cust":cust})
def sendmailtotechteam(request):
    users = Cu_User.objects.filter(Department="Technical team")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: CTO\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            Techhistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess8/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailtotechteam.html")
def techmailhistory(request):
    email_histories =Techhistory.objects.all().order_by('-sent_at')
    return render(request,"techmailhistory.html",{"email_histories":email_histories})
def deletetechhistory(request,id):
    a=Techhistory.objects.get(id=id)
    a.delete()
    return redirect('/techmailhistory/')
def sendmailcpo(request):
    if request.method=='POST':
        sendmail=request.POST['sendmail']
        if sendmail=="Product team":
            users = Cu_User.objects.filter(Department="Product team")
            email_addresses = [user.Email for user in users]
    
            if request.method == 'POST':
                EmailTitle = request.POST['emailtitle'] 
                Message = request.POST['message']
                
                # Get list of files attached to the request
                files = request.FILES.getlist('files')
                
                email = EmailMessage(
                    EmailTitle,
                    f'sendername: CPO\n\n{Message}',
                    'settings.EMAIL_HOST_USER',
                    email_addresses,
                )

                # Attach each file to the email
                for file in files:
                    email.attach(file.name, file.read(), file.content_type)

                try:
                    email.send()

                        # Save email to history
                    CPOhistory1.objects.create(
                    sender=settings.EMAIL_HOST_USER,
                    recipients=", ".join(email_addresses),
                    subject=EmailTitle,
                    message=Message,
                    Designation=sendmail,
                    )
                    return redirect('/sendmailsuccess9/')
                except Exception as e:
                        # Handle email sending failure
                    return HttpResponse("Failed to send email", status=500)
        elif sendmail=="R&D Dpt":
            users = Cu_User.objects.filter(Department="R&D Dpt")
            email_addresses = [user.Email for user in users]
    
            if request.method == 'POST':
                EmailTitle = request.POST['emailtitle'] 
                Message = request.POST['message']
                
                # Get list of files attached to the request
                files = request.FILES.getlist('files')
                
                email = EmailMessage(
                    EmailTitle,
                    f'sendername: CPO\n\n{Message}',
                    'settings.EMAIL_HOST_USER',
                    email_addresses,
                )

                # Attach each file to the email
                for file in files:
                    email.attach(file.name, file.read(), file.content_type)

                try:
                    email.send()

                        # Save email to history
                    CPOhistory1.objects.create(
                    sender=settings.EMAIL_HOST_USER,
                    recipients=", ".join(email_addresses),
                    subject=EmailTitle,
                    message=Message,
                    Designation=sendmail,
                    )
                    return redirect('/sendmailsuccess9/')
                except Exception as e:
                        # Handle email sending failure
                    return HttpResponse("Failed to send email", status=500)

    return render(request,"sendmailcpo.html")
def sendmailsuccess9(request):
    return render(request,"sendmailsuccess9.html")
def productteamhistory(request):
    email_histories =CPOhistory1.objects.filter(Designation="Product team").order_by('-sent_at')
    return render(request,"productteamhistory.html",{"email_histories":email_histories})
def deleteproducthistory(request,id):
    a=CPOhistory1.objects.get(id=id)
    a.delete()
    return redirect('/productteamhistory/')
def deleterdhistory(request,id):
    a=CPOhistory1.objects.get(id=id)
    a.delete()
    return redirect('/rdhistory/')
def rdhistory(request):
    email_histories2 =CPOhistory1.objects.filter(Designation="R&D Dpt").order_by('-sent_at')
    return render(request,"rdhistory.html",{"email_histories2":email_histories2})
def sendmailtostudents2(request):
    if request.method=='POST':
        sendmail=request.POST['sendmail']
        if sendmail=="Python":
            users =Students.objects.filter(Course="Python")
            email_addresses = [user.Email for user in users]
    
            if request.method == 'POST':
                EmailTitle = request.POST['emailtitle'] 
                Message = request.POST['message']
                
                # Get list of files attached to the request
                files = request.FILES.getlist('files')
                
                email = EmailMessage(
                    EmailTitle,
                    f'sendername: Tutor\n\n{Message}',
                    'settings.EMAIL_HOST_USER',
                    email_addresses,
                )

                # Attach each file to the email
                for file in files:
                    email.attach(file.name, file.read(), file.content_type)

                try:
                    email.send()

                        # Save email to history
                    Studenthistory.objects.create(
                    sender=settings.EMAIL_HOST_USER,
                    recipients=", ".join(email_addresses),
                    subject=EmailTitle,
                    message=Message,
                    Studentcourse=sendmail,
                    )
                    return redirect('/sendmailsuccess10/')
                except Exception as e:
                        # Handle email sending failure
                    return HttpResponse("Failed to send email", status=500)
        elif sendmail=="Data science":
            users =Students.objects.filter(Course="Data science")
            email_addresses = [user.Email for user in users]
    
            if request.method == 'POST':
                EmailTitle = request.POST['emailtitle'] 
                Message = request.POST['message']
                
                # Get list of files attached to the request
                files = request.FILES.getlist('files')
                
                email = EmailMessage(
                    EmailTitle,
                    f'sendername: Tutor\n\n{Message}',
                    'settings.EMAIL_HOST_USER',
                    email_addresses,
                )

                # Attach each file to the email
                for file in files:
                    email.attach(file.name, file.read(), file.content_type)

                try:
                    email.send()

                        # Save email to history
                    Studenthistory.objects.create(
                    sender=settings.EMAIL_HOST_USER,
                    recipients=", ".join(email_addresses),
                    subject=EmailTitle,
                    message=Message,
                    Studentcourse=sendmail,
                    )
                    return redirect('/sendmailsuccess10/')
                except Exception as e:
                        # Handle email sending failure
                    return HttpResponse("Failed to send email", status=500)

    
        elif sendmail=="MERN":
            users =Students.objects.filter(Course="MERN")
            email_addresses = [user.Email for user in users]
    
            if request.method == 'POST':
                EmailTitle = request.POST['emailtitle'] 
                Message = request.POST['message']
                
                # Get list of files attached to the request
                files = request.FILES.getlist('files')
                
                email = EmailMessage(
                    EmailTitle,
                    f'sendername: Tutor\n\n{Message}',
                    'settings.EMAIL_HOST_USER',
                    email_addresses,
                )

                # Attach each file to the email
                for file in files:
                    email.attach(file.name, file.read(), file.content_type)

                try:
                    email.send()

                        # Save email to history
                    Studenthistory.objects.create(
                    sender=settings.EMAIL_HOST_USER,
                    recipients=", ".join(email_addresses),
                    subject=EmailTitle,
                    message=Message,
                    Studentcourse=sendmail,
                    )
                    return redirect('/sendmailsuccess10/')
                except Exception as e:
                        # Handle email sending failure
                    return HttpResponse("Failed to send email", status=500)

    
        elif sendmail=="Digital marketing":
            users =Students.objects.filter(Course="Digital marketing")
            email_addresses = [user.Email for user in users]
    
            if request.method == 'POST':
                EmailTitle = request.POST['emailtitle'] 
                Message = request.POST['message']
                
                # Get list of files attached to the request
                files = request.FILES.getlist('files')
                
                email = EmailMessage(
                    EmailTitle,
                    f'sendername: Tutor\n\n{Message}',
                    'settings.EMAIL_HOST_USER',
                    email_addresses,
                )

                # Attach each file to the email
                for file in files:
                    email.attach(file.name, file.read(), file.content_type)

                try:
                    email.send()

                        # Save email to history
                    Studenthistory.objects.create(
                    sender=settings.EMAIL_HOST_USER,
                    recipients=", ".join(email_addresses),
                    subject=EmailTitle,
                    message=Message,
                    Studentcourse=sendmail,
                    )
                    return redirect('/sendmailsuccess10/')
                except Exception as e:
                        # Handle email sending failure
                    return HttpResponse("Failed to send email", status=500)

    
        
    return render(request,"sendmailtostudents2.html")
def sendmailsuccess10(request):
    return render(request,"sendmailsuccess10.html")
def studentmailhistory2(request):
    email_histories =Studenthistory.objects.all().order_by('-sent_at')
    return render(request,"studentmailhistory2.html",{"email_histories":email_histories})
def deletestudenthistory2(request,id):
    a=Studenthistory.objects.get(id=id)
    a.delete()
    return redirect('/studentmailhistory2/')
def sendmailtoplaceteam(request):
    users = Cu_User.objects.filter(Department="Placement team")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: Placement head\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            Placeteamhistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess11/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailtoplaceteam.html")
def sendmailsuccess11(request):
    return render(request,"sendmailsuccess11.html")
def placeteamhistory(request):
    email_histories =Placeteamhistory.objects.all().order_by('-sent_at')
    return render(request,"placeteamhistory.html",{"email_histories":email_histories})
def deleteplaceteamhistory(request,id):
    a=Placeteamhistory.objects.get(id=id)
    a.delete()
    return redirect('/placeteamhistory/')
def sendmailprojectco(request):
    users = Cu_User.objects.filter(Department="Project coordinator")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: Project head\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            Projectcohistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess12/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailprojectco.html")
def sendmailsuccess12(request):
    return render(request,"sendmailsuccess12.html")
def projectcohistory(request):
    email_histories =Projectcohistory.objects.all().order_by('-sent_at')
    return render(request,"projectcohistory.html",{"email_histories":email_histories})
def deleteprojectcohistory(request,id):
    a=Projectcohistory.objects.get(id=id)
    a.delete()
    return redirect('/projectcohistory/')
def sendmailtocro(request):
    users = Cu_User.objects.filter(Department="CRO")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: GM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            CROhistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess3/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailtocro.html")
def crohistory(request):
    email_histories =CROhistory.objects.all().order_by('-sent_at')
    return render(request,"crohistory.html",{"email_histories":email_histories})
def deletecro(request,id):
    a=CROhistory.objects.get(id=id)
    a.delete()
    return redirect('/crohistory/')
def sendmailtocro1(request):
    users = Cu_User.objects.filter(Department="CRO")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: AGM\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            CROhistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess6/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    
    return render(request,"sendmailtocro1.html")
def crohistory1(request):
    email_histories =CROhistory.objects.all().order_by('-sent_at')
    return render(request,"crohistory1.html",{"email_histories":email_histories})
def deletecro1(request,id):
    a=CROhistory.objects.get(id=id)
    a.delete()
    return redirect('/crohistory1/')
def sendmailsuccess13(request):
    return render(request,"sendmailsuccess13.html")
def sendmailtohre(request):
    users = Cu_User.objects.filter(Department="HRE")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: HR\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            HREhistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess13/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    return render(request,"sendmailtohre.html")
def hrehistory(request):
    email_histories =HREhistory.objects.all().order_by('-sent_at')
    return render(request,"hrehistory.html",{"email_histories":email_histories})
def deletehre(request,id):
    a=HREhistory.objects.get(id=id)
    a.delete()
    return redirect('/hrehistory/')
def sendmailtoinbound(request):
    users = Cu_User.objects.filter(Department="Inbound team")
    email_addresses = [user.Email for user in users]
    
    if request.method == 'POST':
        EmailTitle = request.POST['emailtitle'] 
        Message = request.POST['message']
        
        # Get list of files attached to the request
        files = request.FILES.getlist('files')
        
        email = EmailMessage(
            EmailTitle,
            f'sendername: CRO\n\n{Message}',
            'settings.EMAIL_HOST_USER',
            email_addresses,
        )

        # Attach each file to the email
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        try:
            email.send()

                # Save email to history
            Inboundhistory.objects.create(
            sender=settings.EMAIL_HOST_USER,
            recipients=", ".join(email_addresses),
            subject=EmailTitle,
            message=Message,
            )
            return redirect('/sendmailsuccess14/')
        except Exception as e:
                # Handle email sending failure
            return HttpResponse("Failed to send email", status=500)
    return render(request,"sendmailtoinbound.html")
def sendmailsuccess14(request):
    return render(request,"sendmailsuccess14.html")
def inboundhistory(request):
    email_histories =Inboundhistory.objects.all().order_by('-sent_at')
    return render(request,"inboundhistory.html",{"email_histories":email_histories})
def deleteinbound(request,id):
    a=Inboundhistory.objects.get(id=id)
    a.delete()
    return redirect('/inboundhistory/')
def updatestudent(request,id):
    a=Students.objects.get(id=id)
    if request.POST:
        name=request.POST['name']
        mob=request.POST['mob']
        address=request.POST['address']
        email=request.POST['email']
        course=request.POST['course']
        duration=request.POST['duration']
        a.Name=name
        a.Mob=mob
        a.Address=address
        a.Email=email
        a.Course=course
        a.Duration=duration

        
        a.save()
    
        return redirect('/viewstudents/')
    return render(request,"updatestudent.html",{"a":a})
def about(request):
    return render(request,"about.html")

def readmore1(request):
    return render(request,"readmore1.html")
def readmore2(request):
    return render(request,"readmore2.html")
def team(request):
    return render(request,"team.html")
def viewdetail6(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail6.html",{"cust":cust})
def update6(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail6/")
    return render(request,"update6.html",{"cust":cust})
def viewdetail7(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail7.html",{"cust":cust})
def update7(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail7/")
    return render(request,"update7.html",{"cust":cust})
def viewdetail8(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail8.html",{"cust":cust})
def update8(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail8/")
    return render(request,"update8.html",{"cust":cust})
def viewdetail9(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail9.html",{"cust":cust})
def update9(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail9/")
    return render(request,"update9.html",{"cust":cust})
def viewdetail10(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail10.html",{"cust":cust})
def update10(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail10/")
    return render(request,"update10.html",{"cust":cust})
def viewdetail11(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail11.html",{"cust":cust})
def update11(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail11/")
    return render(request,"update11.html",{"cust":cust})
def viewdetail12(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail12.html",{"cust":cust})
def update12(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail12/")
    return render(request,"update12.html",{"cust":cust})
def viewdetail13(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail13.html",{"cust":cust})
def update13(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail13/")
    return render(request,"update13.html",{"cust":cust})
def viewdetail14(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail14.html",{"cust":cust})
def update14(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail14/")
    return render(request,"update14.html",{"cust":cust})
def viewdetail15(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail15.html",{"cust":cust})
def update15(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail15/")
    return render(request,"update15.html",{"cust":cust})
def viewdetail16(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail16.html",{"cust":cust})
def update16(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail16/")
    return render(request,"update16.html",{"cust":cust})
def viewdetail17(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail17.html",{"cust":cust})
def update17(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail17/")
    return render(request,"update17.html",{"cust":cust})
def viewdetail18(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail18.html",{"cust":cust})
def update18(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail18/")
    return render(request,"update18.html",{"cust":cust})
def viewsubordinates(request):
    cust=Cu_User.objects.all().order_by('-regDte')
    return render(request,"viewsubordinates.html",{"cust":cust})
def deleteuser2(request,id):
    a=Cu_User.objects.get(id=id)
    a.delete()
    return redirect('/viewsubordinates/')
def editsubordinates(request,id):
    a=Cu_User.objects.get(id=id)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        a.Name=name
        a.Phone=phone
        a.Address=address
        a.Email=email
        a.Department=department
        
        a.save()
    
        return redirect('/viewsubordinates/')
    return render(request,"editsubordinates.html",{"a":a})
def viewdetail19(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail19.html",{"cust":cust})
def update19(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail19/")
    return render(request,"update19.html",{"cust":cust})
def viewdetail20(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail20.html",{"cust":cust})
def update20(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail20/")
    return render(request,"update20.html",{"cust":cust})
def viewdetail21(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail21.html",{"cust":cust})
def update21(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail21/")
    return render(request,"update21.html",{"cust":cust})
def viewdetail22(request):
    custId=request.session["id"]
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        
        customer=Cu_User.objects.get(id=custId)
        customer.Name = name
        customer.Phone = phone
        customer.Address= address
        customer.Email = email
        customer.Department = department
       

        customer.save()
    cust=Cu_User.objects.get(id=custId)
    return render(request,"viewdetail22.html",{"cust":cust})
def update22(request):
    custId=request.session["id"]
    cust = Cu_User.objects.get(id=custId)
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        cust.Name=name
        cust.Phone=phone
        cust.Address=address
        cust.Email=email
        
        cust.save()
        return redirect("/viewdetail22/")
    return render(request,"update22.html",{"cust":cust})
def logout_(request):
    if 'id' in request.session:
        request.session.flush()
    logout(request)
    return redirect('/')
