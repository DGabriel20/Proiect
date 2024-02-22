from django.shortcuts import render, redirect
from django.contrib.auth import login
from App_Marketplace.forms import ProductForm
def home_view(request):
    return render(request, 'App_Marketplace/home.html')

def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('home')
    else:
        form = ProductForm

    return render(request, 'App_Marketplace/upload_product.html', {'form': form})
