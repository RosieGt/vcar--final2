from django.shortcuts import render, redirect
from .models import Carro, Aluguel, Cliente, Perfil
from django.contrib.auth.decorators import login_required
from .forms import AluguelForm, CarroForm, ClienteForm, MyUserCreationForm

# Create your views here.

def index(request):
    carros = Carro.objects.all()[:5]
    clientes = Cliente.objects.all()[:5]
    return render(request, 'index.html', { 'clientes':clientes, 'carros':carros})

def lista_carros(request):
    carros = Carro.objects.all()
    return render(request, 'carro/listar.html', {"carros":carros})
@login_required
def detalhar_carro(request, pk):
    carro = Carro.objects.get(pk=pk)
    return render(request, 'carro/detalhar.html', {"carro":carro})
@login_required
def cadastrar_carro(request):
    if request.method == "POST":
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = CarroForm()
            return render(request, "carro/cadastrar.html", {'form': form})
    else:
        form = CarroForm()
        return render(request, "carro/cadastrar.html", {'form': form})
@login_required    
def atualizar_carro(request, pk):
    carro = Carro.objects.get(pk=pk)
    form = CarroForm(instance=carro)
    
    if request.method == "POST":
        form = CarroForm(request.POST, request.FILES, instance= carro)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, "carro/atualizar.html", {'form': form})
    else:
        return render(request, "carro/atualizar.html", {'form': form})
@login_required
def deletar_carro(request, pk):
    carro = Carro.objects.get(pk=pk)

    if carro:
        carro.delete()
        return redirect("/")
    else:
        return render(request, "carro/detalhar.html", {'msg': "carro não encontrado"})    
@login_required
def realizar_aluguel(request):
    if request.method == "POST":
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AluguelForm()
            return render(request, "aluguel/cadastrar.html", {'form': form})
    else:
        form = AluguelForm()
        return render(request, "aluguel/cadastrar.html", {'form': form})

@login_required
def realizar_aluguel_carro(request, carro_pk):
    carro = Carro.objects.get(pk=carro_pk)
    aluguel = Aluguel()
    aluguel.carro = carro
    
    form = AluguelForm(instance=aluguel)
    if request.method == "POST":
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AluguelForm(instance=aluguel)
            return render(request, "aluguel/cadastrar.html", {'form': form})
    else:
        form = AluguelForm(instance=aluguel)
        return render(request, "aluguel/cadastrar.html", {'form': form})
@login_required    
def cadastrar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = ClienteForm()
            return render(request, "cliente/cadastrar.html", {'form': form})
    else:
        form = ClienteForm()
        return render(request, "cliente/cadastrar.html", {'form': form})
@login_required    
def detalhar_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    context = {"cliente": cliente}
    return render(request, "cliente/detalhar.html", context)
@login_required
def listar_cliente(request):
    clientes = Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request, "cliente/listar.html", context)
@login_required
def atualizar_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    form = ClienteForm(instance=cliente)
    
    if request.method == "POST":
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, "cliente/atualizar.html", {'form': form})
    else:
        return render(request, "cliente/atualizar.html", {'form': form})
@login_required    
def deletar_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)

    if cliente:
        cliente.delete()
        return redirect("/")
    else:
        return render(request, "cliente/listar.html", {'msg': "Cliente não encontrado"})
       
def registration(request):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = MyUserCreationForm()
            return render(request, "registration/registration.html", {'form': form})
    else:
        form = MyUserCreationForm()
        return render(request, "registration/registration.html", {'form': form})