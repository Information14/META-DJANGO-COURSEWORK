from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Menu, Booking
from .forms import Bookingform
from .serializers import Menuserializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from django.http import HttpResponse
from rest_framework.response import Response


def home(request): 
    return render(request, "index.html")

def about(request): 
    return render(request, "about.html")

def book(request):
    form = Bookingform()
    if request.method == "POST": 
        form = Bookingform(request.POST)
        if form.is_valid(): 
            form.save()
    context = {'form': form} 
    return render(request, "book.html", context)


@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer])
def menu(request):
    if request.method == "GET": 
        try: 
            menuserial = Menu.objects.all()
            menu = Menuserializer(menuserial, many=True)
            context = {'menu': menu.data}
            return Response(context, template_name="menu.html")
        except Exception as e: 
            return HttpResponse({"Invalid": str(e)})
    


@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer])
def item(request, pk):
    try: 
        menuserial = Menu.objects.get(pk=pk)
        menu = Menuserializer(menuserial)
        context = {'menu': menu.data}
        return Response(context, template_name="item.html")
    except Exception as e: 
        return HttpResponse({"Invalid": str(e)})