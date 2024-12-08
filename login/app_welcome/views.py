from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app_create_account.models import User, Animal, AnimalFood

# Create your views here.

def welcome(request):
    if request.method == "GET":
        return render(request, 'welcome_screen.html')
    else:
        return HttpResponse('Error getting welcome page')
    
# Mapeamento fixo de alimentos
ANIMAL_FOOD_MAP = {
    'boi': ['Capim', 'Silagem'],
    'vaca': ['Capim', 'Ração'],
    'cavalo': ['Feno', 'Aveia'],
    'porco': ['Milho', 'Farelo de Soja'],
    'galinha': ['Milho', 'Farelo de Trigo'],
    'peixe': ['Alga', 'Larvas'],
}

def add_animal(request):
    if request.method == 'POST':
        # Receber os dados do front-end
        specie_animal = request.POST.get('animal')
        color_animal = request.POST.get('color')
        owner_id = request.POST.get('owner_id')  # ID do usuário que será o dono

        # Validar dados obrigatórios
        if not specie_animal or not color_animal or not owner_id:
            return JsonResponse({'error': 'Dados incompletos.'}, status=400)

        try:
            # Obter o usuário
            owner = User.objects.get(id=owner_id)

            # Criar o animal
            animal = Animal.objects.create(
                specie_animal=specie_animal,
                color_animal=color_animal,
                owner=owner
            )

            # Adicionar os alimentos baseados na espécie do animal
            food_list = ANIMAL_FOOD_MAP.get(specie_animal.lower(), [])
            for food in food_list:
                AnimalFood.objects.create(animal=animal, food_name=food)

            return JsonResponse({'message': 'Animal e alimentos adicionados com sucesso!'}, status=201)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Usuário não encontrado.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Método não permitido.'}, status=405)