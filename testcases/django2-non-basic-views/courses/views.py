from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import CourseModelForm
from .models import Course

import logging
# BASE VIEW CLass = VIEW

class CourseObjectMixin(object):
    model = Course # Taint.DB
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj # Taint.DB



class CourseDeleteView(CourseObjectMixin, View):
    template_name = "courses/course_delete.html" # DetailView
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')
        return render(request, self.template_name, context)

# Attack Payload curl 'http://localhost:8000/courses/4/update/' -d "title=<script>alert(123)</script>"
class CourseUpdateView(CourseObjectMixin, View):
    template_name = "courses/course_update.html" # DetailView
    logger = logging.getLogger(__name__)

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object() # self.get_object == CourseObjectMixin:get_object, which return Taint.DB
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj # Taint.DB
            context['form'] = form # Taint.Web
            self.logger.debug("CourseUpdateView: get " + form.cleaned_data['title'] ) # CWEID 117
            self.logger.debug("CourseUpdateView: get " +  obj.title) # CWEID 117
        return render(request, self.template_name, context) # Taint passed to template_name


    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object() # self.get_object == CourseObjectMixin:get_object, which return Taint.DB
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj # Taint.DB
            context['form'] = form # Taint.Web
            self.logger.debug("CourseUpdateView: post " + form.cleaned_data['title'] ) # CWEID 117
            self.logger.debug("CourseUpdateView: post " +  obj.title) # CWEID 117
        return render(request, self.template_name, context) # Taint passed to template_name


class CourseCreateView(View):
    template_name = "courses/course_create.html" # DetailView

    logger = logging.getLogger(__name__)

    def get(self, request, *args, **kwargs):
        # GET method
        form = CourseModelForm()
        context = {"form": form}
        self.logger.debug("CourseCreateView : post " + form.instance.title)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST method
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)

# Attack.Payload curl 'http://localhost:8000/courses/'
class CourseListView(View):
    template_name = "courses/course_list.html"
    queryset = Course.objects.all()
    logger = logging.getLogger(__name__)

    def get_queryset(self):
        for data in self.queryset:
            self.logger.debug("CourseListView : get_queryset" + data.title) # CWEID 117
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)

# Attack.Payload curl 'http://localhost:8000/courses/4/'
class CourseView(CourseObjectMixin, View):
    template_name = "courses/course_detail.html" # DetailView
    logger = logging.getLogger(__name__)

    def get(self, request, id=None, *args, **kwargs):
        context = {'object': self.get_object()} # self.get_object passed Taint.DB from CourseObjectMixin.get_object
        self.logger.debug("CourseView: get " + str(context['object'].title)) # CWEID 117
        return render(request, self.template_name, context)


# HTTP METHODS
def my_fbv(request, *args, **kwargs):
    print(request.method)
    return render(request, 'about.html', {})