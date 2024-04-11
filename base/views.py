from django.shortcuts import render


def menu(request, categories):
    print('\ncategories: ', categories)
    return render(request, 'main.html', {
        'params': categories,
    })