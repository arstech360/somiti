"""somiti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from  .views import  signIn,postsignIn,createacc,userdata,deleteuser,profile,viewacc,installment,employee,addemployee,addemployeepost,\
    expense,expensedetails,expensepost,dashboard,depositor,addDepositor,addDepositorpost,adminprofile,deleteemployee,deleteexpense,deletedepositor
from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', signIn, name='signIn'),
path('postsignIn',postsignIn,name="postsignIn"),
path('createacc',createacc,name="createacc"),
path('userdata',userdata,name="userdata"),
path('deleteuser<docid>',deleteuser,name="deleteuser"),
path('profile',profile,name="profile"),
path('viewacc<docid1>',viewacc,name="viewacc"),
path('installment',installment,name="installment"),
path('addemployee',addemployee,name="addemployee"),
path('employee',employee,name="employee"),
path('addemployeepost',addemployeepost,name="addemployeepost"),
path('expense',expense,name="expense"),
path('expensepost',expensepost,name="expensepost"),
path('expensedetails',expensedetails,name="expensedetails"),
path('depositor',depositor,name="depositor"),
path('addDepositor',addDepositor,name="addDepositor"),
path('addDepositorpost',addDepositorpost,name="addDepositorpost"),
path('dashboard',dashboard,name="dashboard"),
path('adminprofile',adminprofile,name="adminprofile"),
path('deleteemployee<docid2>',deleteemployee,name="deleteemployee"),
path('deleteexpense<docid3>',deleteexpense,name="deleteexpense"),
path('deletedepositor<docid4>',deletedepositor,name="deletedepositor"),
]
