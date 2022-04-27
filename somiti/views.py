import pyrebase
from django.shortcuts import render,get_object_or_404, redirect
from django.template.context import RequestContext

from django.shortcuts import render
import pyrebase
import firebase_admin
from django.shortcuts import render

config = {

  "apiKey": "AIzaSyA2HSXH9xoof2fJjk16EC2p4KSVFlXTlvI",
  "authDomain": "somiti-7d7f4.firebaseapp.com",
  "databaseURL": "https://somiti-7d7f4-default-rtdb.firebaseio.com",
  "projectId": "somiti-7d7f4",
  "storageBucket": "somiti-7d7f4.appspot.com",
  "messagingSenderId": "781927986234",
  "appId": "1:781927986234:web:eabb230971ade04ca0b103",
  "measurementId": "G-4ZDS537WRE"
};

# Initialising database,auth and firebase for further use
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
storage=firebase.storage()


def signIn(request):
  return render(request, "sign-in.html")


def dashboard(request):
  return render(request, "dashboard.html")


def postsignIn(request):
  email = request.POST.get('email')
  pasw = request.POST.get('pass')
  try:
    # if there is no error then signin the user with given email and password
    authe.sign_in_with_email_and_password(email, pasw)
  except:
    message = "Invalid Credentials!!Please ChecK your Data"
    return render(request, "sign-in.html", {"message": message})
  return render(request, "dashboard.html")


def logout(request):
  try:
    del request.session['uid']
  except:
    pass
  return render(request, "Login.html")


def signUp(request):
  return render(request, "sign-up.html")

def createacc(request):
  url=None
  from django.core.files.storage import FileSystemStorage
  firstname = request.POST.get('first-name')
  lastname = request.POST.get('lastname')
  shopname = request.POST.get('shopname')
  refname = request.POST.get('refname')
  nidnumber = request.POST.get('nidnumber')
  banknumber = request.POST.get('banknumber')
  amount = request.POST.get('amount')
  installment = request.POST.get('installment')
  interest = request.POST.get('interest')
  adress = request.POST.get('adress')
  datevalue = request.POST.get('datevalue')
  age = request.POST.get('age')
  radiobtn = request.POST.get('radiobtn')
  email = request.POST.get('email')
  phoneNum = request.POST.get('phoneNum')
  active= request.POST.get('form_type')
  try:
    upload = request.FILES['upload']
    fss = FileSystemStorage()
    file = fss.save(upload.name, upload)
    file_url = fss.url(file)
    imagename=str(nidnumber)+".jpg"
    storage.child(file).put(file)
    userid=firebase.auth()
    url=storage.child(file).get_url(userid['idToken'])
    print(userid)
  except:
    None

  #storage.child("image").put(image)

  data = {
    "firstname": firstname,
    "lastname": lastname,
    "shopname": shopname,
    "refname": refname,
    "nidnumber": nidnumber,
    "banknumber": banknumber,
    "amount": amount,
    "installment": installment,
    "interest": interest,
    "adress": adress,
    "age": age,
    "radiobtn": radiobtn,
    "datevalue":datevalue,
    "email":email,
    "phoneNum":phoneNum,
    "status":active
  }
  database.child("somiti").child("createacc").push(data)
  totalloan=database.child("somiti").child("dashboarddata").get().val()
  totalloan=float(totalloan['totalloan'])+float(amount)
  database.child("somiti").child("dashboarddata").update({"totalloan":totalloan})
  print(totalloan)
  return render(request,"createaccount.html")

def userdata(request):
  data=database.child("somiti").get().val()
  return render(request,"user-data.html",data)

def deleteuser(request, docid):
    print(docid)

    test = database.child("somiti").child("createacc").get().val()
    for key, value in test.items():
      if value['firstname'] == docid:
        database.child("somiti").child("createacc").child(key).remove()
    return redirect('userdata')


def viewacc(request, docid1):
  print(docid1)
  test = database.child("somiti").child("createacc").get().val()
  for key, value in test.items():
      if value['firstname'] == docid1:
        data1=database.child("somiti").child("installmentData").child(key).child("allloansaving").get().val()

        data = {
          "firstname": value['firstname'],
          "lastname": value['lastname'],
          "shopname": value['shopname'],
          "refname": value['refname'],
          "nidnumber": value['nidnumber'],
          "banknumber": value['banknumber'],
          "amount": value['amount'],
          "installment": value['installment'],
          "interest": value['interest'],
          "adress": value['adress'],
          "age": value['age'],
          "radiobtn": value['radiobtn'],
          "imagefile": value['imagefile'],
          "datevalue": value['datevalue'],
          "email": value['email'],
          "phoneNum": value['phoneNum'],
          "status": "Active",
          "allloansaving":data1

        }

  return render(request,"profile.html",data)

# profile
def profile(request):
  data=database.child("somiti").child("createacc").get().val()
  return render(request,"profile.html")

def supply(request,data):
  return render(request, "installment-form.html", data)

def installment(request):
  userid=request.POST.get('myCountry')
  date = request.POST.get('date')
  print(date,userid)
  test = database.child("somiti").child("createacc").get().val()
  for key, value in test.items():
    if value['firstname'] ==userid:
      firstname=value['firstname']
      lastname = value['lastname']
      nidnumber = value['nidnumber']
      phoneNum = value['phoneNum']
      import json

      with open('id.json', 'r') as f:
        data = json.load(f)
        data['uid'] =key
      with open('id.json', 'w') as json_file:
        json.dump(data, json_file)
      print(data)
      data={
        "firstname":firstname,
        "lastname":lastname,
        "nidnumber":nidnumber,
        "phoneNum":phoneNum,
      }
      return render(request, "installment-form.html", data)

  savings = request.POST.get('savings')
  elevation = request.POST.get('elevation')
  status = request.POST.get('status')
  collection = request.POST.get('collection')
  loanStatus = request.POST.get('loanStatus')
  datevalue = request.POST.get('datevalue')
  import time

  named_tuple = time.localtime()  # get struct_time
  time_string = time.strftime("%m/%d/%Y", named_tuple)
  loansavingdata = {
    "savings": savings,
    "elevation": elevation,
    "status": status,
    "collection": collection,
    "loanStatus": loanStatus,
    "datevalue": datevalue,
    "date":time_string
  }

  import json

  with open('id.json', 'r') as f:
    data = json.load(f)
    data['uid']

  database.child("somiti").child("installmentData").child(data['uid']).child("allloansaving").child('loansavings').push(loansavingdata)

  import json

  with open('id.json', 'r') as f:
    data = json.load(f)
    data['uid'] = 0
  with open('id.json', 'w') as json_file:
    json.dump(data, json_file)
  print(data)
  return render(request, "installment-form.html")
def addemployee(request):
  return render(request,"add-employee.html")
def addemployeepost(request):
  employee_name=request.POST.get('employee_name','')
  employee_type = request.POST.get('employee_type')
  designation_id = request.POST.get('designation_id')
  mobile_number = request.POST.get('mobile_number')
  email_address = request.POST.get('email_address')
  mother_name = request.POST.get('mother_name')
  father_name = request.POST.get('father_name')
  employee_images = request.POST.get('employee_images')
  permanent_address = request.POST.get('permanent_address')
  nid_number = request.POST.get('nid_number')
  basic_salary = request.POST.get('basic_salary')
  washing_cost = request.POST.get('washing_cost')
  deposit_amount = request.POST.get('deposit_amount')
  overtime_rate = request.POST.get('overtime_rate')
  joining_date = request.POST.get('joining_date')
  house_rent = request.POST.get('house_rent')
  cng_cost = request.POST.get('cng_cost')
  perDaySalery = request.POST.get('perDaySalery')
  mobile_cost = request.POST.get('mobile_cost')
  status = request.POST.get('status')
  if status == "1":
    status1 = "new patient"
  elif status == "2":
    status1 = "old patient"
  else:
    None
  data={
    "employee_name": employee_name,
    "employee_type":employee_type,
    "status":status1,
    "mobile_cost":mobile_cost,
    "perDaySalery":perDaySalery,
    "cng_cost":cng_cost,
    "house_rent":house_rent,
    "joining_date":joining_date,
    "overtime_rate":overtime_rate,
    "deposit_amount":deposit_amount,
    "washing_cost":washing_cost,
    "basic_salary":basic_salary,
    "nid_number":nid_number,
    "permanent_address":permanent_address,
    "employee_images":employee_images,
    "father_name":father_name,
    "mother_name":mother_name,
    "email_address":email_address,
    "mobile_number":mobile_number,
    "designation_id":designation_id
  }
  print(data)
  database.child("somiti").child("employee").push(data)
  return redirect('employee')
def employee(request):
  context=database.child("somiti").get().val()
  return render(request,"employee.html",context)
def expense(request):
  return render(request,"expense.html")

def expensepost(request):
  employee_type = request.POST.get('employee_type', '')
  designation_id = request.POST.get('designation_id')
  mobile_number = request.POST.get('mobile_number')
  designation_id1 = request.POST.get('designation_id1')
  father_name = request.POST.get('father_name')
  employee_images = request.POST.get('employee_images')
  designation_id2 = request.POST.get('designation_id2')
  house_rent = request.POST.get('house_rent')
  data = {
    "designation_id": designation_id,
    "employee_type": employee_type,
    "mobile_number": mobile_number,
    "designation_id1": designation_id1,
    "father_name": father_name,
    "employee_images": employee_images,
    "house_rent": house_rent,
    "designation_id2": designation_id2,
  }
  database.child("somiti").child("expense").push(data)
  return redirect('expensedetails')

def expensedetails(request):
  context = database.child("somiti").get().val()
  return render(request,"expenseDetails.html",context)
def dashboard(request):
  return render(request,"dashboard.html",)