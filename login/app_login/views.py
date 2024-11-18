from django.shortcuts import render 
from django.http import HttpResponse, JsonResponse
from app_create_account.models import User

# Create your views here.

def loginMe(request):
    if request.method == "GET":
        return render(request, 'login_screen.html')
    elif request.method == "POST":
        user_name = request.POST.get('user_name')
        user_pass = request.POST.get('user_pass')
        db_user_name = User.objects.filter(name_user=user_name)
        db_user_pass = User.objects.filter(password_user=user_pass)

        if user_name and user_pass != '':
            if db_user_name and db_user_pass:
                return JsonResponse({"message": f"Bem vindo, {user_name}", "status":"success"})
            else:
                return JsonResponse({"message": "credenciais inválidas!", "status":"invalid"})
        else:
            return JsonResponse({"message":"Preencha todos os campos!", "status":"empty"})
        
