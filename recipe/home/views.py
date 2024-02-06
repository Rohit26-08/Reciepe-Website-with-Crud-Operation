from django.shortcuts import render,redirect
from django.contrib import messages
from insert.models import insertvalue
from account.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request): 
    try:
     if request.method=="POST":
            asa=request.POST.get('search')
            abc=insertvalue.objects.filter(recipe_name__icontains=asa)
            return render(request,'index.html',{'recipe':abc})
    
        
            
    except:
     print(Exception)
    abc=insertvalue.objects.all()
    return render(request,'index.html',{'recipe':abc})
    
   
@login_required(login_url='/login/')
def update(request,id):
    abc=insertvalue.objects.get(id=id)
    try:
        if request.method=="POST":
            recipe_name=request.POST.get('recipename')
            description=request.POST.get('description')
            image=request.FILES.get('img')
            print(image)
            abc.objects.create(recipe_name=recipe_name, recipe_description=description,image=image)
            
            
    except:
     print(Exception)
    return render(request,'update.html',{'recipe':abc})
@login_required(login_url='/login/')
def delete(request,id):
   abc=insertvalue.objects.get(id=id)
   print(abc)
   abc.delete()
   return redirect('/')
 
@login_required(login_url='/login/')
def insert(request):
    try:
        if request.method=="POST":
            recipe_name=request.POST.get('recipename')
            description=request.POST.get('description')
            img=request.FILES.get('image')
   
               
            print(img)
            ins=insertvalue(recipe_name=recipe_name, recipe_description=description, image1=img)
            ins.save()
            return redirect('/')
            
    except Exception as e:
     print(e)
    return render(request,'insert.html')

def login_page(request):
   try: 
    if request.method=="POST":
        username=request.POST.get('email')
        password=request.POST.get('pwd')
    else:
        print('ok')
    if not User.objects.filter(username=username):
       messages.error(request,'invalid user name') 
    user=authenticate(username=username,password=password)
    if user is None:
         messages.error(request,'Invalid') 
    else:
        login(request,user)
        return redirect('/')
   except Exception as e:
    print(e)
       
   return render(request,'login.html')
def logout_page(request):
    logout(request)
    return redirect('/login/')


def registration(request):
    if request.method=="POST":
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        email=request.POST.get('email')
        
        password=request.POST.get("pwd")
        password1=request.POST.get("pwd1")
        user =User.objects.filter(username=email)
        if  User.objects.filter(username=email):
            messages.error(request,"user already exists")
            return redirect('/registration/')
        if  password!=password1:
            messages.error(request,"Both Password are not same")
            return redirect('/registration/')
        else:
          user =User.objects.create(first_name=first_name,
                                  last_name=last_name,
                                  email=email,
                                  username=email)
          user.set_password(password)
          user.save()
          return redirect('/')
        

    else:
        print("nothing happend")

    return render(request,'registration.html')

