from django.shortcuts import render


def menu(request, categories):
    return render(request, 'main.html', {
        'params': categories,
    })