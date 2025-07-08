from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def recipes(request):
    recipes_book = {
        'Завтраки': {
            'Омлет': {
                'id': 1,
                'slug': 'eggs',
                'ingredients': {
                    'Яйцо': '2 шт',
                    'Сыр': '50 гр',
                    'Молоко': '100 мл'
                }
            },
            'Блинчики': {
                'id': 2,
                'slug': 'pancakes',
                'ingredients': {
                    'Мука': '200 гр',
                    'Яйцо': '1 шт',
                    'Молоко': '300 мл'
                }
            },
            'Гренки': {
                'id': 4,
                'slug': 'toasts',
                'ingredients': {
                    'Хлеб': '4 ломтика',
                    'Яйцо': '2 шт',
                    'Молоко': '100 мл',
                    'Сахар': '1 ст.л.'
                }
            },
            'Овсяная каша': {
                'id': 5,
                'slug': 'oatmeal',
                'ingredients': {
                    'Овсяные хлопья': '100 гр',
                    'Молоко': '300 мл',
                    'Мёд': '2 ч.л.',
                    'Орехи': 'горсть'
                }
            }
        },
        'Обеды': {
            'Суп': {
                'id': 3,
                'slug': 'soup',
                'ingredients': {
                    'Картофель': '3 шт',
                    'Морковь': '1 шт',
                    'Лук': '1 шт',
                    'Курица': '200 гр'
                }
            },
            'Плов': {
                'id': 6,
                'slug': 'pilaf',
                'ingredients': {
                    'Рис': '300 гр',
                    'Мясо': '400 гр',
                    'Морковь': '2 шт',
                    'Лук': '2 шт',
                    'Чеснок': '3 зубчика'
                }
            },
            'Греческий салат': {
                'id': 7,
                'slug': 'greek-salad',
                'ingredients': {
                    'Помидоры': '3 шт',
                    'Огурцы': '2 шт',
                    'Сыр Фета': '150 гр',
                    'Оливки': '50 гр',
                    'Оливковое масло': '3 ст.л.'
                }
            }
        },
        'Ужины': {
            'Картофельное пюре с котлетой': {
                'id': 8,
                'slug': 'mashed-potatoes',
                'ingredients': {
                    'Картофель': '5 шт',
                    'Молоко': '100 мл',
                    'Масло': '50 гр',
                    'Фарш': '400 гр',
                    'Лук': '1 шт'
                }
            },
            'Паста Карбонара': {
                'id': 9,
                'slug': 'carbonara',
                'ingredients': {
                    'Спагетти': '250 гр',
                    'Бекон': '150 гр',
                    'Яйцо': '2 шт',
                    'Сыр Пармезан': '50 гр',
                    'Сливки': '100 мл'
                }
            }
        },
        'Десерты': {
            'Шоколадный торт': {
                'id': 10,
                'slug': 'chocolate-cake',
                'ingredients': {
                    'Мука': '200 гр',
                    'Какао': '50 гр',
                    'Яйцо': '3 шт',
                    'Сахар': '150 гр',
                    'Сливочное масло': '100 гр'
                }
            },
            'Чизкейк': {
                'id': 11,
                'slug': 'cheesecake',
                'ingredients': {
                    'Творожный сыр': '500 гр',
                    'Печенье': '200 гр',
                    'Сахар': '100 гр',
                    'Сливочное масло': '100 гр',
                    'Яйцо': '2 шт'
                }
            },
            'Печенье': {
                'id': 12,
                'slug': 'cookies',
                'ingredients': {
                    'Мука': '300 гр',
                    'Сахар': '150 гр',
                    'Яйцо': '1 шт',
                    'Масло': '200 гр',
                    'Ванилин': '1 ч.л.'
                }
            }
        },
        'Напитки': {
            'Лимонад': {
                'id': 13,
                'slug': 'lemonade',
                'ingredients': {
                    'Лимон': '3 шт',
                    'Сахар': '100 гр',
                    'Вода': '1 л',
                    'Мята': '5 веточек'
                }
            },
            'Глинтвейн': {
                'id': 14,
                'slug': 'mulled-wine',
                'ingredients': {
                    'Красное вино': '750 мл',
                    'Мёд': '50 гр',
                    'Апельсин': '1 шт',
                    'Гвоздика': '5 шт',
                    'Корица': '1 палочка'
                }
            }
        }
    }


    all_recipes = []
    for category, recipes_in_category in recipes_book.items():
        for recipe_name, recipe_data in recipes_in_category.items():
            all_recipes.append({
                'category': category,
                'name': recipe_name,
                'data': recipe_data
            })


    paginator = Paginator(all_recipes, 10)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)


    paginated_recipes = {}
    for item in page_obj:
        category = item['category']
        if category not in paginated_recipes:
            paginated_recipes[category] = {}
        paginated_recipes[category][item['name']] = item['data']

    return render(request,
                  'recipes/recipes.html',
                  {'paginated_recipes': paginated_recipes, 'page_obj': page_obj})

def recipe_detail(request, slug):
    recipes_book = {
        'Завтраки': {
            'Омлет': {
                'id': 1,
                'slug': 'eggs',
                'ingredients': {
                    'Яйцо': '2 шт',
                    'Сыр': '50 гр',
                    'Молоко': '100 мл'
                }
            },
            'Блинчики': {
                'id': 2,
                'slug': 'pancakes',
                'ingredients': {
                    'Мука': '200 гр',
                    'Яйцо': '1 шт',
                    'Молоко': '300 мл'
                }
            },
            'Гренки': {
                'id': 4,
                'slug': 'toasts',
                'ingredients': {
                    'Хлеб': '4 ломтика',
                    'Яйцо': '2 шт',
                    'Молоко': '100 мл',
                    'Сахар': '1 ст.л.'
                }
            },
            'Овсяная каша': {
                'id': 5,
                'slug': 'oatmeal',
                'ingredients': {
                    'Овсяные хлопья': '100 гр',
                    'Молоко': '300 мл',
                    'Мёд': '2 ч.л.',
                    'Орехи': 'горсть'
                }
            }
        },
        'Обеды': {
            'Суп': {
                'id': 3,
                'slug': 'soup',
                'ingredients': {
                    'Картофель': '3 шт',
                    'Морковь': '1 шт',
                    'Лук': '1 шт',
                    'Курица': '200 гр'
                }
            },
            'Плов': {
                'id': 6,
                'slug': 'pilaf',
                'ingredients': {
                    'Рис': '300 гр',
                    'Мясо': '400 гр',
                    'Морковь': '2 шт',
                    'Лук': '2 шт',
                    'Чеснок': '3 зубчика'
                }
            },
            'Греческий салат': {
                'id': 7,
                'slug': 'greek-salad',
                'ingredients': {
                    'Помидоры': '3 шт',
                    'Огурцы': '2 шт',
                    'Сыр Фета': '150 гр',
                    'Оливки': '50 гр',
                    'Оливковое масло': '3 ст.л.'
                }
            }
        },
        'Ужины': {
            'Картофельное пюре с котлетой': {
                'id': 8,
                'slug': 'mashed-potatoes',
                'ingredients': {
                    'Картофель': '5 шт',
                    'Молоко': '100 мл',
                    'Масло': '50 гр',
                    'Фарш': '400 гр',
                    'Лук': '1 шт'
                }
            },
            'Паста Карбонара': {
                'id': 9,
                'slug': 'carbonara',
                'ingredients': {
                    'Спагетти': '250 гр',
                    'Бекон': '150 гр',
                    'Яйцо': '2 шт',
                    'Сыр Пармезан': '50 гр',
                    'Сливки': '100 мл'
                }
            }
        },
        'Десерты': {
            'Шоколадный торт': {
                'id': 10,
                'slug': 'chocolate-cake',
                'ingredients': {
                    'Мука': '200 гр',
                    'Какао': '50 гр',
                    'Яйцо': '3 шт',
                    'Сахар': '150 гр',
                    'Сливочное масло': '100 гр'
                }
            },
            'Чизкейк': {
                'id': 11,
                'slug': 'cheesecake',
                'ingredients': {
                    'Творожный сыр': '500 гр',
                    'Печенье': '200 гр',
                    'Сахар': '100 гр',
                    'Сливочное масло': '100 гр',
                    'Яйцо': '2 шт'
                }
            },
            'Печенье': {
                'id': 12,
                'slug': 'cookies',
                'ingredients': {
                    'Мука': '300 гр',
                    'Сахар': '150 гр',
                    'Яйцо': '1 шт',
                    'Масло': '200 гр',
                    'Ванилин': '1 ч.л.'
                }
            }
        },
        'Напитки': {
            'Лимонад': {
                'id': 13,
                'slug': 'lemonade',
                'ingredients': {
                    'Лимон': '3 шт',
                    'Сахар': '100 гр',
                    'Вода': '1 л',
                    'Мята': '5 веточек'
                }
            },
            'Глинтвейн': {
                'id': 14,
                'slug': 'mulled-wine',
                'ingredients': {
                    'Красное вино': '750 мл',
                    'Мёд': '50 гр',
                    'Апельсин': '1 шт',
                    'Гвоздика': '5 шт',
                    'Корица': '1 палочка'
                }
            }
        }
    }

    recipe = None
    for category in recipes_book.values():
        for name, data in category.items():
            if data['slug'] == slug:
                recipe = {'name': name, **data}

    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
