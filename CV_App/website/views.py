from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from .forms import EditUser
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    if request.method == "POST":
        return render(request, "index.html")
    else:
        cv = CVInfo.objects.filter(user=request.user.id)
        return render(request, "index.html", {"cv": cv})


def Login(request):
    if request.method == "POST":
        userName = request.POST.get("userName")
        password = request.POST.get("password")
        fUserName = userName.split("@")
        user = authenticate(request, username=userName, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Wellcome " + request.user.username)
            return redirect("home")
        else:
            print("something went wrong")
            return render(request, "login&register.html", {"username": fUserName[0], "user": request.user})
    else:
        return render(request, "login&register.html")
@login_required(redirect_field_name="home")
def Logout(request):
    logout(request)
    return redirect("home")


def registerUser(request):
    if request.method == "POST":
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        userEmail = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        suserEmail = userEmail.split("@")[0]
        print(suserEmail)
        if password1 != password2:
            messages.warning(request, 'Your account expires in three days.')
        else:
            user = User.objects.create_user(
                email=userEmail, username=suserEmail)
            user.first_name = firstName
            user.last_name = lastName
            user.set_password(password1)
            user.save()
            USER = authenticate(username=suserEmail, password=password1)
            login(request, USER)
            messages.success(request, "Wellcome " + suserEmail)
            return redirect("home")
        return render(request, "login&register.html")

@login_required(redirect_field_name="home")
def CVView(request):
    template1 = request.POST.get("template1")
    template2 = request.POST.get("template2")
    templateColor = request.POST.get("templateColor")
    cvName = request.POST.get("cvName")
    cvAddress = request.POST.get("cvAddress")
    cvCity = request.POST.get("cvCity")
    cvZip = request.POST.get("cvZIP")
    cvEmail = request.POST.get("cvEmail")
    cvPhone = request.POST.get("cvPhone")
    objective = request.POST.get("objective")
    hobby = request.POST.get("hobby&Interests")
    reference = request.POST.get("references")
    personalAccom1 = request.POST.get("personalAccom1")
    personalAccom2 = request.POST.get("personalAccom2")
    personalAccom3 = request.POST.get("personalAccom2")
    personalAccom4 = request.POST.get("personalAccom4")
    personalAccom5 = request.POST.get("personalAccom5")
    professionalAccom1 = request.POST.get("professionalAccom1")
    professionalAccom2 = request.POST.get("professionalAccom2")
    professionalAccom3 = request.POST.get("professionalAccom3")
    professionalAccom4 = request.POST.get("professionalAccom4")
    professionalAccom5 = request.POST.get("professionalAccom5")
    school = request.POST.get("school/college")
    school1 = request.POST.get("school/college1")
    school2 = request.POST.get("school/college2")
    subject = request.POST.get("subject")
    subject1 = request.POST.get("subject1")
    subject2 = request.POST.get("subject2")
    grade = request.POST.get("grade")
    grade1 = request.POST.get("grade1")
    grade2 = request.POST.get("grade2")
    date = request.POST.get("gdate")
    date1 = request.POST.get("gdate1")
    date2 = request.POST.get("gdate2")
    jobTitle = request.POST.get("jobTitle")
    companyName = request.POST.get("companyName")
    edateStart = request.POST.get("edateStart")
    edateEnd = request.POST.get("edateEnd")
    
    if request.method == "POST" or "FILES":
        if template1 == "on":
            cvInfo = CVInfo(template1=True, template2=False, cvColor=templateColor, fullName=cvName, address=cvAddress, city=cvCity,
                            zip_code=cvZip, cvEmail=cvEmail, phoneNum=cvPhone, objective=objective, hobbyandinterest=hobby, reference=reference, user=request.user)
            cvInfo.save()
            pAccom = PersonalAccomplishment(
                paccomplishment1=personalAccom1,
                paccomplishment2=personalAccom2,
                paccomplishment3=personalAccom3,
                paccomplishment4=personalAccom4,
                paccomplishment5=personalAccom5,
                cvinfo=CVInfo.objects.filter(cvEmail=cvEmail).last()
            )
            prAccom = ProfessionalAccomplishment(
                praccomplishment1=professionalAccom1,
                praccomplishment2=professionalAccom2,
                praccomplishment3=professionalAccom3,
                praccomplishment4=professionalAccom4,
                praccomplishment5=professionalAccom5,
                cvinfo=CVInfo.objects.filter(cvEmail=cvEmail).last()
            )
            education = Education(
                schoolandcollege=school,
                subject=subject,
                grade=grade,
                date=date,
                cvinfo=CVInfo.objects.filter(cvEmail=cvEmail).last()
            )
            education1 = Education1(
                schoolandcollege=school1,
                subject=subject1,
                grade=grade1,
                date=date1,
                cvinfo=CVInfo.objects.filter(cvEmail=cvEmail).last()
            )
            education2 = Education2(
                schoolandcollege=school2,
                subject=subject2,
                grade=grade2,
                date=date2,
                cvinfo=CVInfo.objects.filter(cvEmail=cvEmail).last()
            )
            workHistory = WorkHistory(
                jobTitle=jobTitle,
                companyName=companyName,
                employmentDateStart=edateStart,
                employmentDateEnd=edateEnd,
                cvinfo=CVInfo.objects.filter(cvEmail=cvEmail).last()
            )
            workHistory.save()
            pAccom.save()
            prAccom.save()
            education.save()
            education1.save()
            education2.save()
            return redirect("home")
        elif template2 == "on":
            cimg = request.FILES["cvimage"]
            cvInfo = CVInfo(template1=False, template2=True, cvColor=templateColor, fullName=cvName, address=cvAddress,
                            zip_code=cvZip, cvEmail=cvEmail, phoneNum=cvPhone, objective=objective, hobbyandinterest=hobby, reference=reference,user=request.user)
            cvInfo.save()
            pAccom = PersonalAccomplishment(
                paccomplishment1=personalAccom1,
                paccomplishment2=personalAccom2,
                paccomplishment3=personalAccom3,
                paccomplishment4=personalAccom4,
                paccomplishment5=personalAccom5,
                cvinfo=CVInfo.objects.filter(cvEmail=cvEmail).last()
            )
            prAccom = ProfessionalAccomplishment(
                praccomplishment1=professionalAccom1,
                praccomplishment2=professionalAccom2,
                praccomplishment3=professionalAccom3,
                praccomplishment4=professionalAccom4,
                praccomplishment5=professionalAccom5,
                cvinfo=CVInfo.objects.filter(cvEmail=cvEmail).last()
            )
            education = Education(
                schoolandcollege=school,
                subject=subject,
                grade=grade,
                date=date,
                cvinfo=CVInfo.objects.filter(cvEmail=cvEmail).last()
            )
            education1 = Education1(
                schoolandcollege=school1,
                subject=subject1,
                grade=grade1,
                date=date1,
                cvinfo=CVInfo.objects.filter(cvEmail=cvEmail).last()
            )
            education2 = Education2(
                schoolandcollege=school2,
                subject=subject2,
                grade=grade2,
                date=date2,
                cvinfo=CVInfo.objects.filter(cvEmail=cvEmail).last()
            )
            workHistory = WorkHistory(
                jobTitle=jobTitle,
                companyName=companyName,
                employmentDateStart=edateStart,
                employmentDateEnd=edateEnd,
                cvinfo=CVInfo.objects.filter(cvEmail=cvEmail).last()
            )
            cvimg = CVImg(
                img=cimg,
                cvinfo=CVInfo.objects.filter(cvEmail=cvEmail).last()
            )
            workHistory.save()
            pAccom.save()
            prAccom.save()
            education.save()
            education1.save()
            education2.save()
            cvimg.save()
            return redirect("home")

@login_required(redirect_field_name="home")
def FullView(request, pk):
    if request.method == "GET":
        cv = CVInfo.objects.get(id=pk, user=request.user.id)
        cvEducation = cv.education_set.all()
        cvEducation1 = cv.education1_set.all()
        cvEducation2 = cv.education2_set.all()
        cvWorkHistory = cv.workhistory_set.all()
        cvPersonalAccom = cv.personalaccomplishment_set.all()
        cvProfessionalAccom = cv.professionalaccomplishment_set.all()
        cvImg = cv.cvimg_set.all()
        if cv.template1 == True:
            return render(request, "CV-template-01.html", {"cv": cv, "education": cvEducation, "education2": cvEducation2, "education1": cvEducation1, "workhistory": cvWorkHistory, "paccom": cvPersonalAccom, "praccom": cvProfessionalAccom})
        else:
            return render(request, "CV-template-02.html", {"cv": cv, "education": cvEducation, "education2": cvEducation2, "education1": cvEducation1, "workhistory": cvWorkHistory, "paccom": cvPersonalAccom, "praccom": cvProfessionalAccom, "cvimg": cvImg})

@login_required(redirect_field_name="home")
def userChange(request):
    if request.method == "POST":
        form = EditUser(request.POST, instance=request.user)
        form.save()
        return redirect("home")
    else:
        form = EditUser(instance=request.user)
    return render(request, "edit.html", {"form": form})

@login_required(redirect_field_name="home")
def passwordChange(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, "passwordChange.html", {"form": form})
    

@login_required(redirect_field_name="home")
def userPreview(request):
    count = request.user.cvinfo_set.all().count()
    return render(request, "user.html", {"count": count})

def AboutPage(request):
    return render(request, "AboutUs.html")