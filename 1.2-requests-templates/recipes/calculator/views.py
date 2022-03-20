from multiprocessing import context
from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def home_view(request):
    pages = {
        'Главная страница': reverse('home'),
        # 'Рецепт Омлета': get_current_site('omlet'),
        # 'Рецепт Пасты': reverse('pasta'),
        # 'Рецепт Бутерброда': reverse('buter'),
    }
    context = {'pages': pages}
    return render(request, 'calculator/home.html', context)


def dish_view(request, dish_name):
    amount = int(request.GET.get("servings", 1))
    context = {}
    if dish_name in DATA:
        for ingrs, qty in DATA[dish_name].items():
            if 'recipe' not in context:
                context['recipe'] = {ingrs: float(qty) * float(amount)}
            else:
                context['recipe'].update({ingrs: float(qty) * float(amount)})
    return render(request, 'calculator/index.html', context)
