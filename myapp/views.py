from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import ImageModel


# Create your views here.

def upload_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")
            form.save()
            print("Image saved")
        else:
            print("Form errors:", form.errors)
    else:
        form = ImageForm()

    images = ImageModel.objects.all()    

    context = {
            'form':form , 
            'images' : images
        }
    return render(request, 'upload_image.html', context=context)


