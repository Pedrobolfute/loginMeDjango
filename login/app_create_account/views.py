from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def registerMe(request):
    if request.method == "GET":
        return render(request, 'create_account_screen.html')
    elif request.method == "POST":
        user_name = request.POST.get('user_name')
        user_pass = request.POST.get('user_pass')
        user_confirm_pass = request.POST.get('user_confirm_pass')
        if user_name and user_pass and user_confirm_pass != '':
            if user_pass != user_confirm_pass:
                return HttpResponse('Senhas não coincidem!')
            else:
                return HttpResponse('Usuario: ' + user_name + ' criado com sucesso!')      
        else:
            return HttpResponse('Preencha todos os campos!')