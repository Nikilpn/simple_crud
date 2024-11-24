
from django.urls import path,include
from myapp import views

urlpatterns=[
    path('',views.add_student_page,name="add_student_page"),
    path('save_student_page/', views.save_student_page, name="save_student_page"),
    path('display_student_page/', views.display_student_page, name="display_student_page"),
    path('edit_student_page/<int:stud_id>/', views.edit_student_page, name="edit_student_page"),
    path('update_student_page/<int:up_id>/', views.update_student_page, name="update_student_page"),
    path('delete_page/<int:del_id>/', views.delete_page, name="delete_page"),


]