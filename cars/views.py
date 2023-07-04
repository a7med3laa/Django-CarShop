from django.shortcuts import render,redirect
from cars.models import Car, Driver
# Create your views here.
def home (request):
    return render(request, "home.html")


def car_detail(request, pk):
    owner_obj = Driver.objects.get(pk=pk)
    car_objs = Car.objects.filter(owner_id=owner_obj.id)
    context = {
        "vehicles": car_objs,
        "drivers": owner_obj,
    }
    print(car_objs)
    return render(request, "car_detail.html", context)

def allcars (request):
    car_objs = Car.objects.all()
    context = {
        "vehicles": car_objs
    }
    return render(request, "cars.html", context)

def alldrivers (request):
    owner_obj = Driver.objects.all()
    context = {
        "drivers": owner_obj
    }
    return render(request, "drivers.html", context)

def adddriver (request):
    if request.method== 'POST':
        name=request.POST['name']
        license=request.POST['license']
        print (name,license)
        driver=Driver.objects.create(
            name=name,
            license=license,
        )
        
        return redirect('alldrivers')

    return render(request, "adddriver.html")

def addcar (request):
    owner_obj = Driver.objects.all()
    context = {
        "drivers": owner_obj
    }

    if request.method== 'POST':
        make=request.POST['carmake']
        model=request.POST['carmodel']
        year=request.POST['caryear']
        vin=request.POST['carvin']
        ownerID=int(request.POST['cardriver'])
        owner=Driver.objects.get(pk=ownerID)
        car=Car.objects.create(
            make=make,
            model=model,
            year=year,
            vin=vin,
            owner=owner
        )
        
        return redirect('allcars')

    return render(request, "addcar.html",context)


