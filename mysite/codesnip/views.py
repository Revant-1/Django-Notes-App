from django.shortcuts import render
from django.views.generic import CreateView,ListView, DetailView
from .models import Codesnip

# Create your views here.
# List view
class SnippetListView(ListView):
    model = Codesnip
    template_name = 'codesnips/codesnip_list.html'
    context_object_name = 'snip'

# Detail view
class SnippetDetailView(DetailView):
    model = Codesnip
    template_name = 'codesnips/codesnip_detail.html'
    context_object_name = 'snippet'


class SnipsCreateView(CreateView):
    model = Codesnip
    fields = ['title','text']
    template_name = 'codesnips/codesnip_form.html'
    success_url = '/smart/codesnips/'
##
# from django.shortcuts import render
# from django.views.generic import ListView, DetailView
# from .models import Codesnip

# # List view
# class SnippetListView(ListView):
#     model = Codesnip
#     template_name = 'codesnips/codesnip_list.html'
#     context_object_name = 'snip'

# # Detail view
# class SnippetDetailView(DetailView):
#     model = Codesnip
#     template_name = 'codesnips/codesnip_detail.html'
#     context_object_name = 'snippet'
