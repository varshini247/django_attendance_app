import calendar
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpRequest
from django.utils.safestring import mark_safe
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from calculator.models import Day
from .forms import RegisterForm
from .utils import Calendar
from django.views import View
from datetime import date, datetime, timedelta
import json
# Create your views here.

def home_view(request):
    return render(request, 'home.html')

# def classes_view(request):
#     return render(request, 'classwise.html')

class Calendar_view(View):
    @method_decorator(login_required(login_url='login')) 
    def get(self,request):
# def calendar_view(request):
        # use today's date for the calendar
        print('hi')
        d = get_date(request.GET.get('month', None))
        print(request.GET)
        print(d)
        # d= get_date(month)
        print('date'+ str(d))
        # Instantiate our calendar class with today's year and date
        print(request.user)
        cal = Calendar(d.year, d.month, request.user)
        cal2=cal.formatmonth(withyear = True)
        # context['calendar'] = mark_safe(cal2)
        
        if request.headers.get('x-requested-with') == 'XMLHttpRequest': 
            print('hiyaaa')
            day_list = request.GET.getlist('hehe')
            print(day_list)
            # cal2 = cal.formatmonth(day_list,withyear=True)
            print('date after dumma'+ str(d))
            days=Day.objects.get_or_create(uid=request.user,year=d, month = d,abs_days=json.dumps(day_list))
            # days=Day.objects.bulk_create(abs_days=day_list)
            # days = Day(abs_days= json.dumps(day_list))
            # print('ennisarl')
            # days.save()
        context = {"calendar": mark_safe(cal2),
                "prev_month" :prev_month(d),
                "next_month" :next_month(d)}
        print(context)
        return render(request, 'calendar.html', context)
        # return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(day):
      first = day.replace(day=1)
      prev = first - timedelta(days=1)
      month = 'month=' + str(prev.year) + '-' + str(prev.month)
      return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def login_view(request):
    print('hi')
    if request.method == 'POST':
        print('heye')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('calendar')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    print('inside reg view')
    if request.method == 'POST':
        print('inside reg view req is post')
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            print('yoyo')
            form.save()
            return redirect('login')
        else:
            print('not valid')
            print(form.errors.as_data())
    context = {}
    
    context['form'] = RegisterForm()
    return render(request, 'register.html', context)