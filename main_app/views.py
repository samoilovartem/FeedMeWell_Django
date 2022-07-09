from django.shortcuts import render, redirect

from main_app.forms import UserForm
from main_app.utils import find_restaurants, save_user_input


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # save_user_input(data)
            result = find_restaurants(data)
            if result:
                context = {'result': result}
                return render(request, 'main_app/found_restaurants.html', context=context)
            else:
                return render(request, 'main_app/no_found_restaurants.html')
    else:
        form = UserForm()
        return render(request, 'main_app/index.html', {'form': form})










