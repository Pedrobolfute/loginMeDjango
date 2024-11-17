from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *


# Create your views here.

def registerMe(request):
    if request.method == "GET":
        return render(request, 'create_account_screen.html')
    elif request.method == "POST":
        user_name = request.POST.get('user_name')
        user_pass = request.POST.get('user_pass')
        user_confirm_pass = request.POST.get('user_confirm_pass')
        user_animal = request.POST.get('my_animal') or None
        user_animal_color = request.POST.get('my_animal_color') or None
        user_vehicle = request.POST.get('my_vehicle_mark') or None
        user_vehicle_model = request.POST.get('my_vehicle_model') or None
        user_vehicle_year = request.POST.get('my_vehicle_year') or None
        user_vehicle_color = request.POST.get('my_vehicle_color') or None
        user_job = request.POST.get('my_job') or None
        user_job_position = request.POST.get('my_job_position') or None
        user_job_salary = request.POST.get('my_job_salary') or None
        user_document = request.POST.get('my_document_type') or None
        user_document_number = request.POST.get('my_document_number') or None

        if user_name and user_pass and user_confirm_pass != '':
            if user_pass != user_confirm_pass:
                return JsonResponse({"message": "Senhas não coincidem!", "status": "ok"})
            else:
                user = User(name_user=user_name, password_user=user_pass)
                user.save()

                animal = Animal(specie_animal=user_animal, color_animal=user_animal_color, owner=user)
                animal.save()

                vehicle = Vehicle(mark_vehicle=user_vehicle, model_vehicle=user_vehicle_model, year_vehicle=user_vehicle_year, color_vehicle=user_vehicle_color, owner=user)
                vehicle.save()

                job = Job(company_job=user_job, position_job=user_job_position, salary_job=user_job_salary, owner=user)
                job.save()

                document = Document(type_document=user_document, number_document=user_document_number, owner=user)
                document.save()

                return JsonResponse({"message": f"Usuário {user_name} criado com sucesso!", "status": "created"})
        else:
            return JsonResponse({"message": "Preencha campos de Login, senha e confirmação da senha", "status": "ok"})

            ## quando salva user sem passar um animal, tabela animal da BO