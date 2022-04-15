from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import EditProfileForm, PasswordChangingForm, RegistrationForm
from django.contrib.auth.views import PasswordChangeView

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    success_url= reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class UserRegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url= reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url= reverse_lazy('home')

    def get_object(self):
        return self.request.user



