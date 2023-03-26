from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from link.models import Category, Link

@login_required
def dashboard(request):
    categories = Category.objects.filter(created_by=request.user)
    links = Link.objects.filter(created_by=request.user)
    return render(request, 'dashboard/dashboard.html', {'categories': categories, 'links': links})

