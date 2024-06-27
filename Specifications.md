# Django 2.x Research

## Introduction

This research specification is based on Django version 2.2. Lot of functionality discussed below have been part of previous versions, but are now becoming de-facto ways of writing Django MVC applications. This specification is based on the assumption all aspect of [Django 1.x Research](https://wiki.veracode.local/display/RES/Django+1.x+Research) is fully supported.


## Modeling Information

Our main effort to support Django 2.x, would be around how we:

1. Identifying view classes/functions and capture taint flow relevant information.
2. Identifying templates which would be mapped to view classes alongwith corresponding tainted information being passed for rendering.


## Identifying Views:

Views can be written either as functions or as class based views. 

###1. **View Functions:** 

In addition to what we currently support, below 4 variables can be configured to point to view functions to write custom exception handlers. These callable view functions should be treated as entry points, which takes first argument as Taint.Web [django.http.Request](https://docs.djangoproject.com/en/2.1/ref/request-response/#django.http.HttpRequest) object and returns a [django.http.Response](https://docs.djangoproject.com/en/2.1/ref/request-response/#django.http.HttpResponse) object.


```
from . import views

handler404 = 'simpleapp.views.my_custom_page_not_found_view'
handler500 = 'simpleapp.views.my_custom_error_view'
handler403 = 'simpleapp.views.my_custom_permission_denied_view'
handler400 = 'simpleapp.views.my_custom_bad_request_view'

View Function:
---------------
# Attack.Payload curl 'http://localhost:8000/abc/' --cookie "tainted_cookie=<script>alert(1)</script>"
def my_custom_page_not_found_view(request):
	logger.debug("my_custom_page_not_found_view " + request.COOKIES.get('tainted_cookie')) # CWEID 117
	return render(request, '404.html', status=404)

```
**Testcase:** [view file](https://gitlab.laputa.veracode.io/research-roadmap/python-django2/blob/master/testcases/django2-simpleapp/simpleapp/simpleapp_urls.py) and corresponding [view functions](https://gitlab.laputa.veracode.io/research-roadmap/python-django2/blob/master/testcases/django2-simpleapp/simpleapp/views.py).


###2. **Class Based Views:**

Django ships with [hierarchy of built-in class based views](https://docs.djangoproject.com/en/2.1/ref/class-based-views/) which would be used in customer view classes. 

These built-in classes can either be directly used in URLConf or extended and included from python view files. 

Views are configured as the 2nd parameter of [django.urls.path](https://docs.djangoproject.com/en/2.1/ref/urls/#path) [django.urls.url](https://docs.djangoproject.com/en/2.1/ref/urls/#url) functions. We can differentiate between a Django function view and class based view, by looking for second parameter with ```as_view()``` method call in URLConf as shown below:
 


```
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
	path('about/', TemplateView.as_view(template_name="about.html")), # Base View class directly configured in URLConf
	path('',views.IndexView.as_view(),name='index'), # IndexView would be configured in views.py file
]
```
**How to pass tainted Arguments from URLConf to view classes?**

**Path Converters:** To capture a value from route URL, angular brackets are used. This captured value can also contain an optional converter type. Only, if the converter type is explicitly set to "str", or no converter type is used, consider corresponding keyword argument (**kwargs) as tainted:

```
urlpatterns = [
	# tainted tag_slug can be access in corresponding View Entry Point function as kwargs["tag_slug"]
	path('path_converter/<str:tag_slug>/',views.TaintedDataPathConverter.as_view(),name='tainted_data_path_converter'),
	
	# tainted_arg, tainted_arg_1 are tainted, but tag_id is not tainted
	path('fp_path_converter/<str:tainted_arg>/<tainted_arg_1>/<int:tag_id>/',views.FPTaintedDataPathConverter.as_view(),name='tainted_data_path_converter'), 
	
	## One more way to pass tainted data from path converters to views.
	path('taint_source_args/<tainted_args>/', RedirectView.as_view(
		url='http://%(tainted_args)s') # CWEID 601
		 ),
	
]
```
**Testcase:** [URLConf of testcase](https://gitlab.laputa.veracode.io/research-roadmap/python-django2/blob/master/testcases/django2-simpleapp/simple_class_based_view/simple_cbv_urls.py)

In view entry point methods, keyword arguments ```**kwargs```, is considered tainted, only if path converter parameter matches above condition. We don't consider ```*args``` parameter as tainted. Thus, 

```
class TaintedDataPathConverter(View):
    logger = logging.getLogger(__name__)

    # Attach.Payload curl -X GET 'http://localhost:8000/class_based_view/view_class_tainted_data/path_converter/<script>alert(1)<script>/'
    def get(self, request, *args, **kwargs):
        self.logger.debug("TaintedDataPathConverter:get with args " , args ) # FP CWEID 117
        self.logger.debug("TaintedDataPathConverter:get with kwargs" + kwargs['tag_slug'] ) # CWEID 117
        return HttpResponse("TaintedDataPathConverter:get with kwargs " + kwargs['tag_slug'])  # CWEID 80

class FPTaintedDataPathConverter(View):
    logger = logging.getLogger(__name__)

    # Attach.Payload curl -X GET 'http://localhost:8000/class_based_view/view_class_tainted_data/fp_path_converter/<script>alert(tainted_arg)/<script>alert(tainted_arg_1)/2/'
    def get(self, request, *args, **kwargs):
        self.logger.debug("FPTaintedDataPathConverter:get " + kwargs['tainted_arg']) # CWEID 117
        self.logger.debug("FPTaintedDataPathConverter:get " + kwargs['tainted_arg_1']) # CWEID 117
        return HttpResponse("FPTaintedDataPathConverter:get " + str(kwargs['tag_id']))  # FP CWEID 80
```
**Testcase**: [view file](https://gitlab.laputa.veracode.io/research-roadmap/python-django2/blob/master/testcases/django2-simpleapp/simple_class_based_view/views.py)

**View class members relevant for Taint Analysis:**

Once, we identify a class based view is being used, it would be setting one of the member properties or implementing one of the member functions of the build in class it is using. 

Below is a list of built-in class members we would need for further taint analysis:

**Legends:**
P: == Property
F: == Function
M: == Method


**Entry Points:**

```
F: get(self,T,args,Conditional_T)
F: post(self,T,args,Conditional_T)
F: put(self,T,args,Conditional_T)
F: patch(self,T,args,Conditional_T)
F: delete(self,T,args,Conditional_T)
F: head(self,T,args,Conditional_T)
F: options(self,T,args,Conditional_T)
F: trace(self,T,args,Conditional_T)

F: dispatch(self,T,args,Conditional_T)
F: http_method_not_allowed(self,T,args,Conditional_T)
F: render_to_response(self,T,args,Conditional_T)
F: form_invalid(self,T)
F: form_valid(self,T)
```

**SOURCE**

```
T == Taint.DB

Below properties/functions returns Taint.DB, which gets passed to templates.

P: extra_context
P: model
P: queryset

F: get_queryset(self)
F: get_context_data(self,kwargs)
F: get_object(self,queryset)

```

**Sinks:**

```
CWEID 601 when T : Taint.Web or Taint.DB

P: url == T
P: success_url == T

If below functions return tainted data, flag at return statement.

F: get_redirect_url(self,args,conditional_T)
F: get_success_url(self)
F: render_to_response(self,T,response_kwargs)
```

**Plays a role in modeling:**

```

P: template_name : property will be set to point to template being used
P: template_name_field
P: template_name_suffix
F: get_template_names(self): function returns template being used by this view class.


P: context_object_name : property will be set to name of object being referenced in templates.
F: get_context_object_name(self,obj) : function returns, name of object being referenced in templates 

```

**Testcase**: All testcases will have some or all of the above, however most comprehensive is [urls file](https://gitlab.laputa.veracode.io/research-roadmap/python-django2/blob/master/testcases/django2-simpleapp/simple_class_based_view/simple_cbv_urls.py) and corresponding [view file](https://gitlab.laputa.veracode.io/research-roadmap/python-django2/blob/master/testcases/django2-simpleapp/simple_class_based_view/views.py).

**Custom Mixins:**

In an effort to employ more discrete DRY principles in modern web mvc applications, newer Django applications write custom Mixins. 

URLConf, would still be pointing to a view class. However, the view class, will be inheriting one (or a chain of custom mixins). Custom mixin, will define one of the taint analysis interesting methods/functions/properties we defined above. This would make all code defined in mixin, available in view class which inherits it as well.

For e.g:

```
urls.py
-------

urlpatterns = [
    path('mine/',
         views.ManageCourseListView.as_view(),
         name='manage_course_list'),
    ]
    
views.py
--------
         
class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OwnerEditMixin, self).form_valid(form)


class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin):
    model = Course
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')

# queryset being passed to below template, comes from OwnerMixin. This queryset, carries Taint.DB, which is passed to template as well 
class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = 'courses/manage/course/list.html'


```
**Testcase**: [view file](https://gitlab.laputa.veracode.io/research-roadmap/python-django2/blob/master/testcases/django2-non-basic-views/courses/views.py) and corresponding [url file](https://gitlab.laputa.veracode.io/research-roadmap/python-django2/blob/master/testcases/django2-non-basic-views/courses/urls.py)

## Identifying templates mapped to corresponding views:

1. template_name: 
2. get_template_names():
3. default convention: If none of above configured, default template is used which is picked from folder 

```templates/<app name>/<model name>_<view type>.html, where view_type == list/create/edit/delete.```

**Testcase:** [URLConf](https://gitlab.laputa.veracode.io/research-roadmap/python-django2/blob/master/testcases/django2-non-basic-views/blog/urls.py) 

### Within Templates:

In addition to context objects, `request` and `message` objects are also available within a template file:

1. By default, these templates have access to [`request`](https://docs.djangoproject.com/en/2.1/ref/templates/api/#django-template-context-processors-request) object which is current [HttpRequest](https://docs.djangoproject.com/en/2.1/ref/request-response/#django.http.HttpRequest) object. `HttpRequest` object is to be considered Tainted.Web. 

```
in template file
-----------------
request.META.QUERY_STRING : {{ request.META.QUERY_STRING | safe }} {# CWEID 80 #}
```
**Testcase:** [Template with request object resulting in CWEID 80](https://gitlab.laputa.veracode.io/research-roadmap/python-django2/blob/master/testcases/django2-simpleapp/simpleapp/templates/500.html)

2. [`django.contrib.messages`](https://docs.djangoproject.com/en/2.1/ref/contrib/messages/#using-messages-in-views-and-templates) object should be treated as taint propogators. Tainted data can be propogated into this object from python files using any of below methods:

- T = messages.add_message(request,T)
- T = messages.debug(request,T)
- T = messages.info(request,T)
- T = messages.success(request,T)
- T = messages.warning(request,T)
- T = messages.error(request,T)

```
from django.contrib import messages


messages.add_message(request, messages.INFO, 'Hello Tainted World. ' + request.COOKIES.get('tainted_cookie'))
messages.info(request,'Tainted Cookie Value is %s' % request.COOKIES.get('tainted_cookie') )

Template file:
--------------

<ul>
    {% for message in messages %}
	    <li>{{ message | safe }}</li> {# CWEID 80 #}
    {% endfor %}
</ul>
        
```
**Testcase:** [View file](https://gitlab.laputa.veracode.io/research-roadmap/python-django2/blob/master/testcases/django2-polling_app/polls/views.py) and [template file](https://gitlab.laputa.veracode.io/research-roadmap/python-django2/blob/master/testcases/django2-polling_app/polls/templates/polls/detail.html)

3. Context Data: Context data is passed into templates, and referenced in templates using any of the below features: (refer **"View class members relevant for Taint Analysis"** Section)
	- object: **Testcase** [template](https://gitlab.laputa.veracode.io/research-roadmap/python-django2/blob/master/testcases/django2-educa/students/templates/students/course/detail.html)
	- model_name: **Testcase**: All testcases.
	- object_list: **Testcase** [template](https://gitlab.laputa.veracode.io/research-roadmap/python-django2/blob/master/testcases/django2-educa/courses/templates/courses/manage/course/list.html)
	- context_object_name or get_context_object_name() method: **Testcase** [view file](https://gitlab.laputa.veracode.io/research-roadmap/python-django2/blob/master/testcases/django2-polling_app/polls/views.py) & [template file](https://gitlab.laputa.veracode.io/research-roadmap/python-django2/blob/master/testcases/django2-polling_app/polls/templates/polls/index.html)

#### XSS
1. **Safe Filter:** safe filter explicitly marks corresponding data "safe from any injection", which basically means it won't escape any special character unlike defaults. Whenever tainted data is rendered thru such a safe filter, we need to flag it as XSS 80.

```
 <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text | safe }}</a></li> <!-- CWEID 80 -->
```
**Testcase**: All testcases

**Normalized Version**
```
__vc_output_raw(__vc_template_filter({'controller':'polls/templates/polls/index.html','filter': 'safe'},__vc_template_scope({'controller':'polls/templates/polls/index.html'}).question.question_text))
```

2. Irrespective of default escaping setting, if tainted data is rendered in an HTML attribute without being enclosed in quotes, it should be flagged as XSS.

```
  <!-- When setting question_text == class1 onload=javascript:alert(1) -->
    <style class={{ question.question_text }}></style> <!-- CWEID 80 -->
    <style class="{{ question.question_text }}"></style> <!-- FP 80 -->

```
**Testcase:**[Template file](https://gitlab.laputa.veracode.io/research-roadmap/python-django2/blob/master/testcases/django2-polling_app/polls/templates/polls/index.html)

**Normalized Version**
```
__vc_output_text(__vc_template_scope({'controller':'polls/templates/polls/index.html'}).question.question_text)
```

This would need updates to Normalizer. We currently don't seem to track if tainted data is being output in html attributes or within double quotes. 

If the expression is in double brackets and it's an unquoted attribute value, then use `__vc_output_raw`, otherwise use `__vc_output_text`

3. Tainted data being tagging within a block of autoescape tag set to off, should be flagged as XSS

```
{% autoescape off %}
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li> <!-- CWEID 80 -->
{% endfor %}
</ul>
{% endautoescape %}
```

**Normalized Version**

```
# VERA-COORDS: l 1  c 5  f polls/templates/polls/results.html
__vc_output_text(__vc_template_scope({'controller':'polls/templates/polls/results.html'}).question.question_text)
# VERA-COORDS: l 5  c 1  f polls/templates/polls/results.html
__vc_template_scope({'controller':'polls/templates/polls/results.html'}).choice = __vc_template_scope({'controller':'polls/templates/polls/results.html'}).question.choice_set.all

# VERA-COORDS: l 6  c 9  f polls/templates/polls/results.html
__vc_output_raw(__vc_template_scope({'controller':'polls/templates/polls/results.html'}).choice.choice_text)
# VERA-COORDS: l 6  c 37  f polls/templates/polls/results.html
__vc_output_raw(__vc_template_scope({'controller':'polls/templates/polls/results.html'}).choice.votes)
# VERA-COORDS: l 6  c 60  f polls/templates/polls/results.html
__vc_output_raw(__vc_template_filter({'controller':'polls/templates/polls/results.html','filter': 'pluralize'},__vc_template_scope({'controller':'polls/templates/polls/results.html'}).choice.votes))
```

 
###Model :

An object of a class extending [django.db.models.Model](https://docs.djangoproject.com/en/2.1/ref/models/fields/), would be configured with fields of [various types](https://docs.djangoproject.com/en/2.1/ref/models/fields/#field-types). Considering entire model object as Taint.DB, could lead to troves of false positives. 

Only fields configured as one of the below types should be considered Taint.DB:

- CharField
- TextField
- FileField: **Testcase** [File Upload Functionality](https://gitlab.laputa.veracode.io/research-roadmap/python-django2/tree/master/testcases/django2-simpleapp/file_upload)
- ImageField: **Testcase** [Image Upload Functionality](https://gitlab.laputa.veracode.io/research-roadmap/python-django2/tree/master/testcases/django2-simpleapp/file_upload)


```
class Article(models.Model):
	title   = models.CharField(max_length=120) # Carries Taint.DB
	content = models.TextField() # Carries Taint.DB
	active  = models.BooleanField(default=True) # Doesn't carry Taint.DB

```
##Miscellaneous findings:

####CSRF

If a template contains ```form``` html element, and its action submits the page within the application, and django ```csrf_token``` tag is missing, its a CWEID 352.

Application submitting to itself can be whitelisted with below values of ```action``` attribute:

```
<form action =""
<form action = "."
<form action = "{% url
```

```
form action="{% url 'polls:vote' question.id %}" method="post">
 {# CWEID 352 #}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
{% endfor %}
<input type="submit" value="Vote">
</form>

-----------------------------------------------------

<form action='.' method='POST'>{% csrf_token %} {# FP CWEID 352 #}
    <h1>Do you want to delete the product "{{ object.title }}"?</h1>
    <p><input type='submit' value='Yes' />  <a href='../'>Cancel</a></p>

</form>

```


#### Debug Mode set to True		
DEBUG shouldn't be enabled in production applications. We should flag any DEBUG property set to True, unless file name of the property contains any of below list of words indicating, its not a production settings file.

Blacklisted Keywords list: stage, staging, dev, test, qa, ci, jenkins, circle, travis

```
In settings.py
--------------

DEBUG = True # CWEID 215

In qa_settings.py:
------------------
DEBUG = True # FP CWEID 215
```	
 
#### Overly inclusive domains configuration
 
None of the entries of below property should be "*". 

```
ALLOWED_HOSTS = ['127.0.0.1','localhost', '*'] # CWEID 183
```

#### Hardcoded credentials:

```django.contrib.auth.authenticate``` method parameters username and password is set to string literals, they are hardcoded credential values. This should be flagged as CWEID 798

```
from django.contrib.auth import authenticate

cd = form.cleaned_data
user = authenticate(username=cd['username'], password=cd['password1']) # FP CWEID 798
```

## Taint Analysis:

SINKS:

```
CWE 80 (when T is Taint.Web or Taint.DB); CWE 201 (when T is Taint.Sensitive)
	* django.http.response.Http404(T)
```

## Testcases
All projects are packaged as per packaging requirements of a Python app. These would be all zip files under:
[Python - Django2 Testcases](https://maven.laputa.veracode.io/browse?list=snapshots/com/veracode/research/python-django2)

## Assumptions:

- We don't support kwargs coming from regular path based URLConf. This is because, we dont validate regular expressions... 


## Out of Scope

- Custom Context Processors
- Custom Path Converters
- Decorators


## References
- [Django 2.x Official Documentation](https://docs.djangoproject.com/en/2.1/)
- [Django 2.x Source Code Repository](https://github.com/django/django)
- [Django 1.x Research](https://wiki.veracode.local/display/RES/Django+1.x+Research)
- [Django 1.x Testcases](https://stash.veracode.local/projects/RES/repos/static-tests-python-preliminary-djangoex1/browse)
- [What's New - Django 2.x](https://docs.djangoproject.com/en/2.1/releases/2.0/)
- [Security in Django](https://docs.djangoproject.com/en/2.1/topics/security/)
- [Static analysis tool, to find Python Web App Vulnerabilities](https://github.com/python-security/pyt)
- [Classy Class-Based Views](https://ccbv.co.uk)
- [Difference Between Function Based Views and Class Based Views](https://www.youtube.com/watch?v=OYJ6gXykLtM&feature=youtu.be)
- [Try Django 2.x Testcase](https://github.com/codingforentrepreneurs/Try-Django)
- [How to upload files with Django](https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html)
- [Django FormView](https://www.youtube.com/watch?v=3HE5zrxfMi0)