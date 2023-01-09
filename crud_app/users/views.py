from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Both GET and POST routes for user registration
def register(request):
    if request.method == 'POST':
        # create a form object with the inputs that the user entered
        form = UserCreationForm(request.POST)

        # if everything is valid, show a message and redirect to the home page
        if form.is_valid():
            form.save()  # save user
            messages.success(request, 'Your account has been created!')
            return redirect('blog-home')
    else:
        # if it's not a post request, start the form empty
        form = UserCreationForm()
    # this either renders an empty form for GET requests, or a formed filled with previous entries for invalid POST requests
    return render(request, 'users/register.html', {'form': form})