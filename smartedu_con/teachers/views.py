from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from courses.models import Course
from teachers.models import Teacher

# Create your views here.

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers.html'
    context_object_name = 'teachers'
    #paginate_by = 1 #sayfalama 
    #queryset = Teacher.objects.all()[:1] #Tek bir tane teacher getirir

class TeacherDetailView(DetailView):
    model = Teacher
    template_name='teacher.html'
    context_object_name = 'teacher'
    
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(avaliable=True, teacher = self.kwargs['pk'])
        return context