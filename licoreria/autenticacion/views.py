from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from licoreriaapp.precio_bcv import*


# Create your views here.
def base3(request):
    x=valorDolar()
    a=x[0]
    b=x[1]
    c=x[2]
    template_name='registro/base3.html'
    context={'valordolar':a, 'valoreuro':b, 'fecha': c}   
    return render(request, template_name, context)


class registro_usuario(View):    
    def get(self, request):
        template_name='registro/usuario.html'
        form = UserCreationForm()
        #return render(request, "registro/usuario.html",{"form":form})
        return render(request, template_name, {"form":form})
    
    
        
    
    def post(self, request):
        x=valorDolar()
        a=x[0]
        b=x[1]
        c=x[2]
        #context={'valordolar':a, 'valoreuro':b, 'fecha': c}
        form = UserCreationForm(request.POST)       
        if form.is_valid():            
            usuario=form.save()
            login(request,usuario)
            context={'valordolar':a, 'valoreuro':b, 'fecha': c, 'usuario':str(usuario)}
            return render(request, "registro/base3.html", context)
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro/usuario.html", {'form':form})

def cerrar_sesion(request):
    logout(request)
    return redirect("Home")

def logear(request):
    x=valorDolar()
    a=x[0]
    b=x[1]
    c=x[2]
      
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=clave)
            if usuario is not None:
                context={'valordolar':a, 'valoreuro':b, 'fecha': c, 'usuario':str(usuario)}
                login=(request, usuario)
                usuario1=str(usuario)
                # print(usuario1, type(usuario1))
                return render(request,"registro/home_base3.html", context )
            
            else:
                messages.error(request,"Las credenciales ingresadas son incorrectas")
                #return render(request, "registro/login.html", {'form':form})
        else:
            messages.error(request,"Las credenciales ingresadas son incorrectas")
            return render(request, "registro/login.html", {'form':form})
    form=AuthenticationForm()
    return render(request, "registro/login.html", {'form':form})