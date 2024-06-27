from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

from django.http import HttpResponseBadRequest
from django.http.response import HttpResponseForbidden, HttpResponseGone, HttpResponseNotFound, HttpResponseServerError, JsonResponse
from .forms import ArticleModelForm
from .models import Article


import logging

# Payload: curl -X POST 'http://localhost:8000/blog/create/' -d "title=blog997&content=blog 997 content"
class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all() # <blog>/<modelname>_create.html
    logger = logging.getLogger(__name__)

    #success_url = '/'

    def form_valid(self, form):
        #print(form.cleaned_data)
        self.logger.debug("ArticleCreateView: form_valid " + form.cleaned_data["title"])
        return super().form_valid(form)

    def form_invalid(self, form):
        #print(form.cleaned_data)
        return super().form_invalid(form)


    def get_success_url(self):
        self.logger.debug("ArticleCreateView: get_success_url " , self.object.title ) # CWEID 117
        return  '/blog/' + self.object.title + "/" # CWEID 601

# Attack.Payload curl -X GET 'http://localhost:8000/blog/'
class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all() # <blog>/<modelname>_list.html
    logger = logging.getLogger(__name__)

    context_object_name = 'articles'

    extra_context = ''

    # Attack.payload curl -X trace 'http://localhost:8000/blog/'  --cookie "tainted_cookie=<script>alert(1)</script>"
    def trace(self, request, *args, **kwargs):
        self.logger.debug("ArticleListView: trace " + request.COOKIES.get('tainted_cookie')) # CWEID 117
        return HttpResponseGone("ArticleListView: trace " + request.COOKIES.get('tainted_cookie')) # CWEID 80


    # Attack.Payload curl -X POST 'http://localhost:8000/blog/'  --cookie "tainted_cookie=<script>alert(1)</script>"
    def http_method_not_allowed(self, request, *args, **kwargs):
        self.logger.debug("ArticleListView: http_method_not_allowed " + request.COOKIES.get('tainted_cookie'))
        return HttpResponseForbidden( request.COOKIES.get('tainted_cookie')) # CWEID 80

# Attack.Payload curl -X GET 'http://localhost:8000/blog/<script>/article_starts_with/' --cookie "tainted_cookie=<script>alert(1)</script>"
class ArticleListViewStartsWith(ListView):
    logger = logging.getLogger(__name__)

    template_name = ''

    extra_context = ''


    # Attack.Payload curl -X POST 'http://localhost:8000/blog/<script>/article_starts_with/' --cookie "tainted_cookie=<script>alert(1)</script>"
    def post(self, request, *args, **kwargs):
        return JsonResponse(self.extra_context) # CWEID 80

    def get_context_data(self, *, object_list=None, **kwargs):
        self.logger.debug("ArticleListViewStartsWith: get_context_data " + self.kwargs["title"]) # CWEID 117
        self.extra_context = {'tainted_data' : self.kwargs['title']}
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.logger.debug("ArticleListViewStartsWith:get_queryset " + self.kwargs["title"]) # CWEID 117
        self.extra_context = {'tainted_data':self.kwargs["title"]}
        # Due to Taint.DB on Article model.object
        return Article.objects.filter(title__startswith=self.kwargs["title"]) # CWEID 80

    # Attack.Payload curl -X trace 'http://localhost:8000/blog/<script>/article_starts_with/' --cookie "tainted_cookie=<script>alert(1)</script>"
    def http_method_not_allowed(self, request, *args, **kwargs):
        self.logger.debug("ArticleListViewStartsWith: http_method_not_allowed " + request.COOKIES.get('tainted_cookie')) # CWEID 117
        return HttpResponseNotFound( request.COOKIES.get('tainted_cookie')) # CWEID 80

    def get_context_object_name(self, object_list):
        return "articles"

    def get_template_names(self):
        return "articles/article_list.html"

# Attack.Payload curl -X GET 'http://localhost:8000/blog/blog1/'
class ArticleDetailView(DetailView):
    logger = logging.getLogger(__name__)

    template_name = 'articles/article_detail.html'
    #queryset = Article.objects.all()

    def get_object(self):
        title_ = self.kwargs.get("title") #self.kwargs == Tainted Source
        self.logger.debug("In ArticleDetailView:get_object: " + title_) # CWEID 117
        return get_object_or_404(Article, title=title_) # Article object should be Taint.DB


    # Attack.Payload curl -X POST "http://localhost:8000/blog/blog1/" --cookie "tainted_cookie=<script>alert(1)</script>"
    def http_method_not_allowed(self, request, *args, **kwargs):
        self.logger.debug("ArticleDetailView: http_method_not_allowed " + request.get_full_path())
        return HttpResponseServerError( request.COOKIES.get('tainted_cookie')) # CWEID 80

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm

    new_title = ''
    new_content = ''

    logger = logging.getLogger(__name__)

    def get_object(self):
        title_ = self.kwargs.get("title")
        self.logger.debug("ArticleUpdateView:ArticleUpdateView " + title_) # CWEID 117
        #id_ = self.kwargs.get("id")
        return get_object_or_404(Article, title=title_)


    def form_valid(self, form):
        self.logger.debug("ArticleUpdateView:form_valid " + form.instance.title)
        self.new_title = form.instance.title
        self.new_content = form.instance.content
        return super().form_valid(form)

    def get_success_url(self):
        self.logger.debug("ArticleUpdateView: get_success_url " + mark_safe(self.new_title)) # CWEID 117
        return "/blog/" + mark_safe(self.new_title)+ "/" # CWEID 601

class ArticleUpdateContextDataView(UpdateView):
    template_name = 'articles/article_update_context_data.html'
    logger = logging.getLogger(__name__)

    def get_object(self, queryset=None):
        return get_object_or_404(Article,title=self.kwargs['title'])

    def get_queryset(self):
        self.logger.debug('ArticleUpdateContextDataView:get_queryset ' + self.kwargs['title'])
        return Article.objects.get(title__startswith=self.kwargs['title'])

    def get_context_data(self, **kwargs):
        self.logger.debug('ArticleUpdateContextDataView:get_context_data' + self.kwargs['title'])
        return {'tainted_data':self.kwargs['title']}

# Add data: curl -X POST 'http://localhost:8000/blog/create/' -d "title=<script>alert(1)<script>&content=blog 996 <script>alert(1)<script>"
# Attack.Payload curl -X POST "http://localhost:8000/blog/<script>alert(1)<script>/delete/"
class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    logger = logging.getLogger(__name__)

    # Attack.Payload curl -X trace "http://localhost:8000/blog/<script>alert(1)<script>/delete/"
    def http_method_not_allowed(self, request, *args, **kwargs):
        self.logger.debug("ArticleDeleteView:http_method_not_allowed " +  kwargs["title"]) # CWEID 117
        return HttpResponseServerError( kwargs["title"]) # CWEID 80

    def get_object(self):
        title_ = self.kwargs.get("title")
        self.logger.debug("ArticleDeleteView:get_object " + title_) # CWEID 117
        #id_ = self.kwargs.get("id")
        return get_object_or_404(Article, title=title_)

    def get_success_url(self):
        return  '/blog/'









