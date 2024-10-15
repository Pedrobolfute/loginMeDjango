from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def changeMe(request):
    if request.method == "GET":
        return render(request, 'change_account_screen.html')
    elif request.method == "POST":
        user_name = request.POST.get('user_name')
        user_pass = request.POST.get('user_pass')
        user_new_pass = request.POST.get('user_new_pass')
        if user_name and user_pass and user_new_pass != '':
            user_pass = user_new_pass
            return HttpResponse('Usuario: ' + user_name + '; Nova senha: ' + user_new_pass)      
        else:
            return HttpResponse('Preencha todos os campos!')
