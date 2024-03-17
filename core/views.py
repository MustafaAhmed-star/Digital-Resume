from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib import messages
from django.views import generic

from .models import (Skill,UserProfile
,ContactProfile,Media
,Testimonial,Portfolio
,Blog,Certificate
)
from .forms import ContactForm

class IndexView(generic.TemplateView):
    template_name  = 'core/index.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        tesetimonial = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        pvortfolio = Portfolio.objects.filter(is_active=True)
        
        context['tesetimonial']=tesetimonial
        context['certificates']=certificates
        context['blogs']=blogs
        context['pvortfolio']=pvortfolio
        
        return context


class ContactView(generic.FormView):
    template_name = 'core/cotact.html'
    form_class = ContactForm
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request,'Thank you , we will be in touch soon !')
        return super().form_valid(form)


class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = 'core/portfolio.html'
    paginate_by = 10
    
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(is_active = True)
        
class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = 'core/portfolio-detail.html'
    
    
class BlogView(generic.ListView):
    model = Blog
    template_name ='core/blog.html'
    paginate_by = 10
    
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(is_active = True)
        
class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'core/blog-detail.html'