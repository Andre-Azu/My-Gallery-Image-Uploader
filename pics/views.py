from django.http.response import HttpResponse,Http404
from django.shortcuts import render
from .models import image
from django.conf import settings
from django.conf.urls.static import static
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def homepage(request):
    return render(request, 'base.html')

def search_results(request):

    if 'Image' in request.GET and request.GET["Image"]:
        search_term = request.GET.get("Image")
        searched_images = image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


def Image(request, image_id):
    try:
        Image = image.objects.get(id=image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'images.html', {"image":Image})
