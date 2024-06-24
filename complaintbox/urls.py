"""
URL configuration for complaintbox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,),

    path('studentreg/', views.studentreg, name='studentreg'),
    path('studentlog/', views.studentlog, name='studentlog'),
    path('profilestudent/', views.profilestudent, name='profilestudent'),
    path('viewstudent/', views.viewstudent, name='viewstudent'),
    path('cmpltform/',views.cmpltform,name="cmpltform"),
    path('logout/',views.logout,name='logout'),
    path('facultyreg/',views.facultyreg,name='facultyreg'),
    path('facultylog/',views.facultylog,name='facultylog'),
    path('viewcomplaint',views.viewcomplaint,name='viewcomplaint'),
    path('cupdate/<int:id>',views.cupdate,name="cupdate"),
    path('cupdate/cmupdate/<int:id>', views.cmupdate, name='cmupdate'),
    path('ackform/',views.ackform,name='ackform'),
    path('profilefaculty/',views.profilefaculty,name='profilefaculty'),
    path('ackview/', views.ackview, name='ackview'),
    path('viewfaculty/', views.viewfaculty, name='viewfaculty'),
    path('viewadmin/', views.viewadmin, name='viewadmin'),
    path('cmpltviewadmin/', views.cmpltviewadmin, name='cmpltviewadmin'),
    path('ackfaculty/', views.ackfaculty, name='ackfaculty'),
    path('viewfacultyack/', views.viewfacultyack, name='viewfacultyack'),
    path('sdelete/<int:id>',views.sdelete,name="sdelete"),
    path('sdelete/<int:id>',views.sdelete,name="sdelete"),
    path('supdate/',views.supdate,name="supdate"),
    path('supdate/updatestudent/<int:id>',views.updatestudent,name="updatestudent"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



