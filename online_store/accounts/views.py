from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import CreateView
from .models import User
from django.contrib.auth.hashers import make_password

# Create your views her
def profile_view(request):
    return render(request, 'accounts/profile.html')
class registerView(CreateView):
    model = User
    form_class = UserForm
    template_name = "registration/login.html"
    extra_context = {"signup":True}
    success_url = "/accounts/login/"

    def form_valid(self,form):
        user = form.save(commit=False)
        user.password=make_password(user.password)
        user.save()
        return redirect(self.success_url)
