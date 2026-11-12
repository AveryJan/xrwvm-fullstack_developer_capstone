import json,urllib.request,urllib.error
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings

API='http://localhost:3030'
def fetch(path,default):
    try:
        with urllib.request.urlopen(API+path,timeout=3) as r: return json.load(r)
    except (OSError,ValueError): return default

def home(request,state=None):
    chosen=state or request.GET.get('state','')
    dealers=fetch('/fetchDealers/'+urllib.parse.quote(chosen) if chosen else '/fetchDealers',[])
    return render(request,'index.html',{'dealers':dealers,'state':chosen,'error':None if dealers else 'Dealer API unavailable or no matches. Start node server/backend/server.js.'})

def about(request):return render(request,'About.html')
def contact(request):return render(request,'Contact.html')
def dealer_detail(request,dealer_id):
    dealer=fetch(f'/fetchDealer/{dealer_id}',{})
    reviews=fetch(f'/fetchReviews/dealer/{dealer_id}',[])
    return render(request,'dealer.html',{'dealer':dealer,'reviews':reviews,'dealer_id':dealer_id})

def post_review(request,dealer_id):
    if not request.user.is_authenticated: return redirect('/?login=required')
    dealer=fetch(f'/fetchDealer/{dealer_id}',{})
    error=None
    if request.method=='POST':
        data={'dealerId':dealer_id,'name':request.user.username,'review':request.POST.get('review','').strip(),
              'purchase':request.POST.get('purchase')=='yes','car_make':request.POST.get('car_make',''),
              'car_model':request.POST.get('car_model',''),'car_year':request.POST.get('car_year','')}
        if not data['review']:error='Please enter a review.'
        else:
            try:
                req=urllib.request.Request(API+'/postReview',data=json.dumps(data).encode(),headers={'Content-Type':'application/json'},method='POST')
                with urllib.request.urlopen(req,timeout=3) as response:response.read()
                return redirect(f'/dealers/{dealer_id}/?posted=1')
            except OSError:error='Review service is unavailable.'
    return render(request,'review.html',{'dealer':dealer,'dealer_id':dealer_id,'error':error})

def payload(request):
    try:return json.loads(request.body or b'{}')
    except (json.JSONDecodeError,UnicodeDecodeError):return {}

@csrf_exempt
@require_http_methods(['POST'])
def register_user(request):
    data=payload(request)
    username=data.get('userName') or data.get('username')
    password=data.get('password','')
    if not username or len(password)<8:return JsonResponse({'error':'Username and password of at least 8 characters required'},status=400)
    if User.objects.filter(username=username).exists():return JsonResponse({'error':'Username already exists'},status=409)
    user=User.objects.create_user(username=username,password=password,email=data.get('email',''),first_name=data.get('firstName',''),last_name=data.get('lastName',''))
    return JsonResponse({'userName':user.username,'status':'Registered'},status=201)

@csrf_exempt
@require_http_methods(['POST'])
def login_user(request):
    data=payload(request)
    username=data.get('userName','')
    user=authenticate(request,username=username,password=data.get('password',''))
    if user is None:return JsonResponse({'error':'Invalid credentials'},status=401)
    login(request,user)
    return JsonResponse({'userName':username,'status':'Authenticated'})

@require_http_methods(['GET','POST'])
def logout_user(request):
    logout(request)
    return JsonResponse({'userName':''})

@require_http_methods(['GET'])
def get_cars(request):
    cars=[('Toyota','Camry'),('Toyota','Corolla'),('Toyota','RAV4'),('Honda','Civic'),('Honda','Accord'),('Honda','CR-V'),('Ford','Mustang'),('Ford','F-150'),('Ford','Explorer'),('Chevrolet','Malibu'),('Chevrolet','Silverado'),('Nissan','Altima'),('Nissan','Rogue'),('Hyundai','Elantra'),('Subaru','Outback')]
    return JsonResponse({'CarModels':[{'CarMake':make,'CarModel':model} for make,model in cars]})
