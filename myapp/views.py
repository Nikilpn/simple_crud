from django.shortcuts import render,redirect

from myapp.models import StudentDb


# Create your views here.
def add_student_page(request):
    return render(request,"add_student.html")
def save_student_page(request):
    if request.method=="POST":
        na=request.POST.get('c-name')
        ag=request.POST.get('c-age')
        ge=request.POST.get('c-gender')
        mob=request.POST.get('c-mobile')
        tut=request.POST.get('c-tutor')
        obj=StudentDb(NAME=na,AGE=ag,MOBILE=mob,GENDER=ge,TUTOR=tut)
        obj.save()
        return redirect(add_student_page)
def display_student_page(request):

    data=StudentDb.objects.all()
    return render(request,"display_student.html", {'data': data})
def edit_student_page(request,stud_id):
    data=StudentDb.objects.get(id=stud_id)

    return render(request,"edit_student.html",{'data':data})

def update_student_page(request,up_id):
    if request.method == "POST":
        na = request.POST.get('c-name')
        ag = request.POST.get('c-age')
        ge = request.POST.get('c-gender')
        mob = request.POST.get('c-mobile')
        tut = request.POST.get('c-tutor')
        StudentDb.objects.filter(id=up_id).update(NAME=na,AGE=ag,MOBILE=mob,GENDER=ge,TUTOR=tut)
        return redirect(display_student_page)
def delete_page(request,del_id):
    x=StudentDb.objects.get(id=del_id).delete()

    return redirect(display_student_page)

