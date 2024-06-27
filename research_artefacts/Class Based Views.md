# Class Based Views:

## Base Views:

```
>>> from django.views.generic.base import View
>>> dir(View)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_allowed_methods', 'as_view', 'dispatch', 'http_method_names', 'http_method_not_allowed', 'options']
>>> View.__bases__
(<class 'object'>,)
>>> from django.views.generic.base import TemplateView
>>> dir(TemplateView)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_allowed_methods', 'as_view', 'content_type', 'dispatch', 'extra_context', 'get', 'get_context_data', 'get_template_names', 'http_method_names', 'http_method_not_allowed', 'options', 'render_to_response', 'response_class', 'template_engine', 'template_name']
>>> TemplateView.__bases__
(<class 'django.views.generic.base.TemplateResponseMixin'>, <class 'django.views.generic.base.ContextMixin'>, <class 'django.views.generic.base.View'>)
>>> from django.views.generic.base import RedirectView
>>> dir(RedirectView)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_allowed_methods', 'as_view', 'delete', 'dispatch', 'get', 'get_redirect_url', 'head', 'http_method_names', 'http_method_not_allowed', 'options', 'patch', 'pattern_name', 'permanent', 'post', 'put', 'query_string', 'url']
>>> RedirectView.__bases__
(<class 'django.views.generic.base.View'>,)
```

## Generic Display Views
```
>>> from django.views.generic.detail import DetailView
>>> dir(DetailView)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_allowed_methods', 'as_view', 'content_type', 'context_object_name', 'dispatch', 'extra_context', 'get', 'get_context_data', 'get_context_object_name', 'get_object', 'get_queryset', 'get_slug_field', 'get_template_names', 'http_method_names', 'http_method_not_allowed', 'model', 'options', 'pk_url_kwarg', 'query_pk_and_slug', 'queryset', 'render_to_response', 'response_class', 'slug_field', 'slug_url_kwarg', 'template_engine', 'template_name', 'template_name_field', 'template_name_suffix']
>>> DetailView.__bases__
(<class 'django.views.generic.detail.SingleObjectTemplateResponseMixin'>, <class 'django.views.generic.detail.BaseDetailView'>)
>>> from django.views.generic.list import ListView
>>> dir(ListView)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_allowed_methods', 'allow_empty', 'as_view', 'content_type', 'context_object_name', 'dispatch', 'extra_context', 'get', 'get_allow_empty', 'get_context_data', 'get_context_object_name', 'get_ordering', 'get_paginate_by', 'get_paginate_orphans', 'get_paginator', 'get_queryset', 'get_template_names', 'http_method_names', 'http_method_not_allowed', 'model', 'options', 'ordering', 'page_kwarg', 'paginate_by', 'paginate_orphans', 'paginate_queryset', 'paginator_class', 'queryset', 'render_to_response', 'response_class', 'template_engine', 'template_name', 'template_name_suffix']
>>> ListView.__bases__
(<class 'django.views.generic.list.MultipleObjectTemplateResponseMixin'>, <class 'django.views.generic.list.BaseListView'>)
>>> from  django.views.generic.list import BaseListView
>>> dir(BaseListView)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_allowed_methods', 'allow_empty', 'as_view', 'context_object_name', 'dispatch', 'extra_context', 'get', 'get_allow_empty', 'get_context_data', 'get_context_object_name', 'get_ordering', 'get_paginate_by', 'get_paginate_orphans', 'get_paginator', 'get_queryset', 'http_method_names', 'http_method_not_allowed', 'model', 'options', 'ordering', 'page_kwarg', 'paginate_by', 'paginate_orphans', 'paginate_queryset', 'paginator_class', 'queryset']
>>> BaseListView.__bases__
(<class 'django.views.generic.list.MultipleObjectMixin'>, <class 'django.views.generic.base.View'>)
```
## Generic Editing Views
```
>>> from django.views.generic.edit import FormView
>>> dir(FormView)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_allowed_methods', 'as_view', 'content_type', 'dispatch', 'extra_context', 'form_class', 'form_invalid', 'form_valid', 'get', 'get_context_data', 'get_form', 'get_form_class', 'get_form_kwargs', 'get_initial', 'get_prefix', 'get_success_url', 'get_template_names', 'http_method_names', 'http_method_not_allowed', 'initial', 'options', 'post', 'prefix', 'put', 'render_to_response', 'response_class', 'success_url', 'template_engine', 'template_name']
>>> FormView.__bases__
(<class 'django.views.generic.base.TemplateResponseMixin'>, <class 'django.views.generic.edit.BaseFormView'>)
>>> from django.views.generic.edit import CreateView
>>> dir(CreateView)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_allowed_methods', 'as_view', 'content_type', 'context_object_name', 'dispatch', 'extra_context', 'fields', 'form_class', 'form_invalid', 'form_valid', 'get', 'get_context_data', 'get_context_object_name', 'get_form', 'get_form_class', 'get_form_kwargs', 'get_initial', 'get_object', 'get_prefix', 'get_queryset', 'get_slug_field', 'get_success_url', 'get_template_names', 'http_method_names', 'http_method_not_allowed', 'initial', 'model', 'options', 'pk_url_kwarg', 'post', 'prefix', 'put', 'query_pk_and_slug', 'queryset', 'render_to_response', 'response_class', 'slug_field', 'slug_url_kwarg', 'success_url', 'template_engine', 'template_name', 'template_name_field', 'template_name_suffix']
>>> CreateView.__bases__
(<class 'django.views.generic.detail.SingleObjectTemplateResponseMixin'>, <class 'django.views.generic.edit.BaseCreateView'>)
>>> from django.views.generic.edit import UpdateView
>>> dir(UpdateView)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_allowed_methods', 'as_view', 'content_type', 'context_object_name', 'dispatch', 'extra_context', 'fields', 'form_class', 'form_invalid', 'form_valid', 'get', 'get_context_data', 'get_context_object_name', 'get_form', 'get_form_class', 'get_form_kwargs', 'get_initial', 'get_object', 'get_prefix', 'get_queryset', 'get_slug_field', 'get_success_url', 'get_template_names', 'http_method_names', 'http_method_not_allowed', 'initial', 'model', 'options', 'pk_url_kwarg', 'post', 'prefix', 'put', 'query_pk_and_slug', 'queryset', 'render_to_response', 'response_class', 'slug_field', 'slug_url_kwarg', 'success_url', 'template_engine', 'template_name', 'template_name_field', 'template_name_suffix']
>>> UpdateView.__bases__
(<class 'django.views.generic.detail.SingleObjectTemplateResponseMixin'>, <class 'django.views.generic.edit.BaseUpdateView'>)
>>> from django.views.generic.edit import DeleteView
>>> dir(DeleteView)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_allowed_methods', 'as_view', 'content_type', 'context_object_name', 'delete', 'dispatch', 'extra_context', 'get', 'get_context_data', 'get_context_object_name', 'get_object', 'get_queryset', 'get_slug_field', 'get_success_url', 'get_template_names', 'http_method_names', 'http_method_not_allowed', 'model', 'options', 'pk_url_kwarg', 'post', 'query_pk_and_slug', 'queryset', 'render_to_response', 'response_class', 'slug_field', 'slug_url_kwarg', 'success_url', 'template_engine', 'template_name', 'template_name_field', 'template_name_suffix']
>>> DeleteView.__bases__
(<class 'django.views.generic.detail.SingleObjectTemplateResponseMixin'>, <class 'django.views.generic.edit.BaseDeleteView'>)
```

## Generic Date Views
Go thru if needed... 



