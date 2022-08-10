import email
from urllib import request
from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate, login,logout,models
from homeApp.models import Customer

# Create your views here.
def profile(request):
    data = Customer.objects.filter(email=request.user)
    return render(request,'ProfilePage.html',{'data':data})

def AccountNumber():
    file = open("AccountNumber.txt","r")
    accountNum = int(file.readline())+1
    file.close()
    print(accountNum)

    file = open("AccountNumber.txt","w")
    file.write(str(accountNum))
    file.close()
    return str(accountNum)


def index(request):
    if request.method == "POST":
        print("working")
        fName = request.POST.get("fname")
        lName = request.POST.get("lname")
        email = request.POST.get("email")
        account = request.POST.get("account")
        amount = float(request.POST.get("amount"))
        password = request.POST.get("password")
        accountNumber = AccountNumber()+account
        print(accountNumber)
        user =  models.User.objects.create_user(password=password,username=email)
        
        customer = Customer(fname=fName,lname=lName,account=account,amount=amount,password=password,email=email,accountNumber=accountNumber)
        
        customer.save()
        user.save()
        
        return redirect('/')
    if request.user.is_anonymous:
        return redirect('login')

    data = Customer.objects.filter(email=request.user)
    return render(request,'HomePage.html',{'data':data})

def getAmount(request,amount=0,oper=True):
    data = Customer.objects.filter(email=request.user)
    for i in data:
        if oper:
            print(f"witdraw = {amount}")
            i.amount-=amount
        else:    
            print(f"deposite = {amount}")
            i.amount+=amount
        i.save()
        print(f"Total Amount = {i.amount}")

def getAmount(request,amount=0,oper=True):
    data = Customer.objects.filter(email=request.user)
    for i in data:
        if oper:
            print(f"witdraw = {amount}")
            i.amount-=amount
        else:    
            print(f"deposite = {amount}")
            i.amount+=amount
        i.save()
        print(f"Total Amount = {i.amount}")



def depositeMoney(request):    
    if request.method == "POST":
        depositeAmount = float(request.POST.get("depositeAmount")) if (request.POST.get("depositeAmount")!="") else 0
        getAmount(request,depositeAmount,oper=False)
        return redirect("/")

    data = Customer.objects.filter(email=request.user)    

    return render(request,"DepositePage.html",{'data':data,'title':'Deposite Amount','path':'deposite'})

def withdrawMoney(request):
    if request.method == "POST":
        withdrawAmount = float(request.POST.get("depositeAmount")) if (request.POST.get("depositeAmount")!="") else 0
        getAmount(request,withdrawAmount,oper=True)
        return redirect("/")

    data = Customer.objects.filter(email=request.user)    

    return render(request,"DepositePage.html",{'data':data,'title':'Withdraw Amount','path':'withdraw'})


def test(request):
    return HttpResponse("Test Passed")

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        authUser = authenticate(username=username,password=password)
        if authUser is not None:
            print("User Auth")
            login(request,authUser)
            return redirect('/')
            
    print("not auth")
    return render(request,"LoginPage.html")

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerNewUser(request):

    return render(request,'RegisterPage.html')