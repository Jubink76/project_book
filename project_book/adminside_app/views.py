from django.shortcuts import render,redirect,get_object_or_404
from log_reg_app.models import UserTable
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control,never_cache
# Create your views here.

@login_required(login_url='admin_login')
@never_cache
def admin_dashboard(request):
    return render(request,'admin_dashboard.html')


def admin_users(request):
    users = UserTable.objects.all().order_by('id')

    # search query
    search_query = request.GET.get('search','')

    if search_query:
        if search_query.isdigit():
            users = users.filter(id=search_query)
        else:
            users = UserTable.objects.filter(
                Q(first_name__icontains=search_query) | 
                Q(last_name__icontains=search_query) |
                Q(username__icontains=search_query) |
                Q(email__icontains=search_query)
            ).order_by('id')
    else:
        users = UserTable.objects.all().order_by('id')
    # implement pagination

    paginator = Paginator(users, 5)
    page_number = request.GET.get('page')
    users = paginator.get_page(page_number)

    

    return render(request,'admin_users.html',{
        'users':users,
        'search_query':search_query
    })

def add_users(request):
    return render(request,'add_users.html')


def view_users(request):
    return render(request,'view_users.html')

def admin_category(request):
    return render(request,'admin_category.html')

def add_category(request):
    return render(request,'add_users.html')

def edit_category(request):
    return render(request,'add_users.html')

def delete_category(request):
    return render(request,'add_users.html')

def admin_products(request):
    return render(request,'admin_products.html')

def add_products(request):
    return render(request,'add_users.html')