from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from contact.forms import RegisterForm, RegisterUpdateFOrm
from django.contrib.auth.decorators import login_required


def register(request):
    form = RegisterForm()


    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario Registrado.')
            return redirect('contact:login')

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )

@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateFOrm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )
    form = RegisterUpdateFOrm(data=request.POST, instance=request.user)

    if not form.is_valid():
         return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )
    form.save()
    return redirect('contact:login')

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request,'Logado com sucesso.')
            return redirect('contact:index')
        messages.error(request, 'Login Invalido')

    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )
@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')