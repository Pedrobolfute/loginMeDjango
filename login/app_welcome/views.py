from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app_create_account.models import User, Animal, AnimalFood

# Create your views here.

def welcome(request):
    if request.method == "GET":
         # Obter o ID do usuário a partir do sessionStorage (passado pelo frontend)
        owner_id = request.session.get('user_name')
        print(owner_id)
        if owner_id:
            try:
                owner = User.objects.get(name_user=owner_id)
                animals = Animal.objects.filter(owner=owner)  # Filtrar animais do usuário
                print(animals)
            except User.DoesNotExist:
                return JsonResponse({'error': 'Usuário não encontrado.'}, status=404)
        return render(request, 'welcome_screen.html', {'animals': animals})
    
    elif request.method == "POST":
        # Mapeamento fixo de alimentos
        ANIMAL_FOOD_MAP = {
            'boi': ['Capim', 'Silagem'],
            'vaca': ['Capim', 'Ração'],
            'cavalo': ['Feno', 'Aveia'],
            'porco': ['Milho', 'Farelo de Soja'],
            'galinha': ['Milho', 'Farelo de Trigo'],
            'peixe': ['Alga', 'Larvas'],
        }
        # Receber os dados do front-end
        specie_animal = request.POST.get('animal')
        color_animal = request.POST.get('color')
        owner_id = request.POST.get('owner')  # ID do usuário que será o dono

        # Validar dados obrigatórios
        if not specie_animal or not color_animal or not owner_id:
            return JsonResponse({'error': 'Dados incompletos.'}, status=400)

        try:
            # Obter o usuário
            owner = User.objects.get(name_user=owner_id)
            owner.save()
            

            # Criar o animal
            animal = Animal.objects.create(
                specie_animal=specie_animal,
                color_animal=color_animal,
                owner=owner
            )
            animal.save()

            # Associar alimentos ao animal criado
            food_list = ANIMAL_FOOD_MAP.get(specie_animal.lower(), [])
            for food in food_list:
                animal_food = AnimalFood(animal=animal, food_name=food)
                animal_food.save()  # Salvando cada alimento no banco

            return JsonResponse({'message': 'Animal e alimentos adicionados com sucesso!'}, status=201)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Usuário não encontrado.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Método não permitido.'}, status=405)
    
