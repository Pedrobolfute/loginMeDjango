from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def loginMe(request):
    if request.method == "GET":
        return render(request, 'login_screen.html')
    elif request.method == "POST":
        user_name = request.POST.get('user_name')
        user_pass = request.POST.get('user_pass')
        if user_name and user_pass != '':
            return HttpResponse('Usuário: ' + user_name + ' , Senha: ' + user_pass)
        else:
            return HttpResponse("Error! Try again!")
        

