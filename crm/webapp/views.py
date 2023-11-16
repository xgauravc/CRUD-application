from django.shortcuts import render
from .forms import CreateUserForm, LoginForm


# Home
def home(request):
    # return HttpResponse("Hi , working")
    return render(request, 'webapp/index.html')

# Register
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
    
    context = {'form':form}
    return render(request,'webapp/register.html',context)
