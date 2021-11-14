from django.db.models import Sum
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from transacciones.models import Person, Transaction
from datetime import datetime

def index(request):
    return HttpResponse("Hello, world.")


@csrf_exempt
def create_person(request):
    if request.method == "POST":
        name = request.POST.get("name", None)
        if name is not None:
            if Person.objects.filter(name=name).exists():
                return HttpResponse("El usuario ya existe", status=403)
            else:
                Person.objects.create(name=name)
                return HttpResponse(f"{name} se creo satisfactoriamente")
        else:
            return HttpResponse("None")


@csrf_exempt
def create_transaction(request):
    if request.method == "POST":
        person_name = request.POST.get("name", None)
        if person_name:
            description = request.POST.get("description", "")
            amount = float(request.POST.get("amount", 0.0))

            person = Person.objects.filter(name=person_name).first()
            Transaction.objects.create(
                person=person,
                amount=amount,
                description=description
            )
            return HttpResponse("Transaccion Creada")
        else:
            return HttpResponse("Persona no especificada")


@csrf_exempt
def get_balance(request):
    if request.method == "GET":
        name = request.GET.get("name", "")

        person = Person.objects.filter(name=name).first()
        balance = person.transaction_set.aggregate(Sum('amount'))
        return HttpResponse(f'balance: {balance["amount__sum"]}')
