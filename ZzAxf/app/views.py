from django.shortcuts import render
from app.models import Wheel,Nav,Mustbuy,Foodtype
# Create your views here.
def home(request):

    wheels = Wheel.objects.all()

    navs = Nav.objects.all()

    mustbuys = Mustbuy.objects.all()

    response_dir = {
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
    }



    return render(request,'home/home.html',context=response_dir)


def market(request, childid='0', sortid='0'):
    foodtypes = Foodtype.objects.all()
    index = int(request.COOKIES.get('index', '0'))
    categoryid = foodtypes[index].typeid

    response_dir = {
        'foodtypes': foodtypes,

    }

    return render(request, 'market/market.html', context=response_dir)



def cart(request):
    return render(request,'cart/cart.html')


def mine(request):
    return render(request,'mine/mine.html')