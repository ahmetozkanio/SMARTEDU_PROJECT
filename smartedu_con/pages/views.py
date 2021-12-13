from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from courses.models import Course
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from teachers.models import Teacher
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(avaliable=True).order_by('-date')[:2]
        context['total_course'] = Course.objects.filter(avaliable=True).count() 
        context['total_students'] = User.objects.filter().count() 
        context['total_teachers'] = Teacher.objects.filter().count() 

        return context

# def index(request):
#     return render(request,'index.html')




class AboutView(TemplateView):
    template_name = 'about.html'

# def about(request):
#     return render(request,'about.html')

class ContactView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'we received your request'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


