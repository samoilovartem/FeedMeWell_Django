from django.shortcuts import render

from main_app.forms import UserForm
from main_app.utils import find_restaurants


def index(request):
    title = 'Find restaurants'
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            result = find_restaurants(data)
            if result:
                context = {'result': result,
                           'title': title}
                return render(request, 'main_app/found_restaurants.html', context=context)
            else:
                return render(request, 'main_app/no_found_restaurants.html')
    else:
        form = UserForm()
        return render(request, 'main_app/index.html', {'form': form,
                                                       'title': title})


def about(request):
    return render(request, 'main_app/about.html', {'title': 'About project'})










