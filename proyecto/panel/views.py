from django.shortcuts import render, redirect
from .forms import FormularioRegistroUser
from django.contrib.auth.models import User

# Create your views here.


def registro(request):

    if request.method == 'GET':
        form = FormularioRegistroUser()
        return render(request, 'panel/usuario_registro.html', {'form':form})

    if request.method == 'POST':
        form = FormularioRegistroUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            User.objects.create_user(username=username,
                                    password=password,
                                    first_name=first_name,
                                    last_name=last_name)
            return redirect('servicio:principal')
            

