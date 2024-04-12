from django.shortcuts import render


def menu(request, categories=""):
    categories_list = categories.split("/")
    print("categories_list: ", categories_list)
    return render(request, 'main.html', {
        'params': categories,
    })