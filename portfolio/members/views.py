from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse_lazy
from .forms import EditProfileForm, PasswordChangingForm, ProfilePageForm, RegistrationForm
from django.contrib.auth.views import PasswordChangeView
from portfolio_app.models import Profile

""" Detail view class for Profile page """
class ShowProfilePageView(generic.DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    """ function to extract primary key for  page user Profile from url params """
    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context

""" Create view class for Profile page """
class CreateProfilePageView(generic.CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'

    """ custom function to intercept form and inject correct profile id into the formbefore processing"""
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

""" Update view class for Profile page """
class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['home_address', 'phone_number', 'gps_lat', 'gps_lng', 'profile_picture']
    success_url= reverse_lazy('home')

""" PasswordChangeView view class forPassword Change view"""
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url= reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

""" Create view class for User Registration page """
class UserRegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url= reverse_lazy('login')

""" Update view class for Edit User Settings page """
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url= reverse_lazy('home')

    """ function to apply object level permissions """
    def get_object(self):
        return self.request.user



