from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import CategoryForm, LinkForm

from .models import Link, Category
from accounts.models import User

#create a category
@login_required
def create_category(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()
            return redirect('dashboard:dashboard')
    else:
        form = CategoryForm()
  

    return render(request, 'link/create_category.html',{
        'form':form,
        'title':'Create Category',
    })


#create a link
@login_required
def create_link(request):

    if request.method == 'POST':
        form = LinkForm(request.POST)

        if form.is_valid():
            link = form.save(commit=False)
            link.created_by = request.user
            link.save()
            return redirect('dashboard:dashboard')
    else:
        form = LinkForm()
        form.fields['category'].queryset= Category.objects.filter(created_by=request.user)
  

    return render(request, 'link/create_link.html',{
        'form':form,
        'title':'Create Link',
    })

#Edit Link

@login_required
def edit_link(request, pk):
    link = get_object_or_404(Link, created_by=request.user, pk=pk)
    if request.method =='POST':
        form = LinkForm(request.POST,instance=link)
        if form.is_valid():
            form.save()

            return redirect('dashboard:dashboard')
    else:
        form = LinkForm(instance=link)
    
    return render(request, 'link/create_link.html',{
        'form':form,
        'title':'Edit Link',
    })

# Delete Link
@login_required
def delete_link(request, pk):
    link = get_object_or_404(Link, created_by=request.user, pk=pk)
    link.delete()
    return redirect('dashboard:dashboard')
    

#Edit the category

@login_required
def edit_category(request, pk):
    category = get_object_or_404(Category, created_by=request.user, pk=pk)
    if request.method =='POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()

            return redirect('dashboard:dashboard')
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'link/create_category.html',{
        'form':form,
        'title':'Edit Category'
    })

# Delete category
@login_required
def delete_category(request, pk):
    print('In delete_category function, pk=', pk)
    category = get_object_or_404(Link, created_by=request.user, pk=pk)
    category.delete()
    return redirect('dashboard/dashboard.html')
    


    
