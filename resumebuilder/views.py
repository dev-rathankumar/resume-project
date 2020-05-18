from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Resume
from .forms import ResumeForm


# Create your views here.
def home(request):
    return render(request, 'resume/home.html')


def dashboard(request):
    return render(request, 'resume/dashboard.html')


class Signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        """Automatically login after signup"""
        view = super(Signup, self).form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view


# function based view
# def create_resume(request):
#     if request.method == 'POST':
#         get the form data
#         validate form data
#         create resume
#         save resume
#     else:
#         create a form for a resume
#         return the template

# class CreateResume(generic.CreateView):
#     """Class based view"""
#     model = Resume
#     fields = ['firstname', 'lastname', 'email', 'phone']
#     template_name = 'resume/create_resume.html'
#     success_url = reverse_lazy('home')
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         super(CreateResume, self).form_valid(form)
#         return redirect('dashboard')

@login_required(login_url='login')
def create_resume(request):
    current_user = request.user
    form = ResumeForm()
    if request.method == 'POST':
        # Create
        filled_form = ResumeForm(request.POST)
        if filled_form.is_valid():
            resume = Resume()
            resume.firstname = filled_form.cleaned_data['firstname']
            resume.lastname = filled_form.cleaned_data['lastname']
            resume.email = filled_form.cleaned_data['email']
            resume.phone = filled_form.cleaned_data['phone']
            resume.user = current_user
            resume.save()

    return render(request, 'resume/create_resume.html', {'form': form})


class DetailResume(generic.DetailView):
    model = Resume
    template_name = 'resume/detailresume.html'


class UpdateResume(generic.UpdateView):
    model = Resume
    template_name = 'resume/updateresume.html'
    fields = ['firstname', 'lastname', 'email', 'phone']
    success_url = reverse_lazy('dashboard')


class DeleteResume(generic.DeleteView):
    model = Resume
    template_name = 'resume/deleteresume.html'
    success_url = reverse_lazy('dashboard')
