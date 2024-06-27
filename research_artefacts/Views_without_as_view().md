```
C: django.views.generic.base.ContextMixin [ django.views.generic.base.ContextMixin , builtins.object]
			P: extra_context None
			F: get_context_data(self,kwargs)

C: django.views.generic.base.TemplateResponseMixin [ django.views.generic.base.TemplateResponseMixin , builtins.object]
			P: content_type None
			P: response_class <class 'django.template.response.TemplateResponse'>
			P: template_engine None
			P: template_name None
			F: get_template_names(self)
			F: render_to_response(self,context,response_kwargs)

C: django.views.generic.dates.DateMixin [ django.views.generic.dates.DateMixin , builtins.object]
			P: allow_future False
			P: date_field None
			F: get_allow_future(self)
			F: get_date_field(self)
C: django.views.generic.dates.DayMixin [ django.views.generic.dates.DayMixin , builtins.object]
			P: day None
			P: day_format %d
			F: get_day(self)
			F: get_day_format(self)
			F: get_next_day(self,date)
			F: get_previous_day(self,date)
C: django.views.generic.dates.MonthMixin [ django.views.generic.dates.MonthMixin , builtins.object]
			P: month None
			P: month_format %b
			F: get_month(self)
			F: get_month_format(self)
			F: get_next_month(self,date)
			F: get_previous_month(self,date)
C: django.views.generic.dates.YearMixin [ django.views.generic.dates.YearMixin , builtins.object]
			P: year None
			P: year_format %Y
			F: get_next_year(self,date)
			F: get_previous_year(self,date)
			F: get_year(self)
			F: get_year_format(self)
C: django.views.generic.detail.SingleObjectMixin [ django.views.generic.detail.SingleObjectMixin , django.views.generic.base.ContextMixin , builtins.object]
			P: context_object_name None
			P: extra_context None
			P: model None
			P: pk_url_kwarg pk
			P: query_pk_and_slug False
			P: queryset None
			P: slug_field slug
			P: slug_url_kwarg slug
			F: get_context_data(self,kwargs)
			F: get_context_object_name(self,obj)
			F: get_object(self,queryset)
			F: get_queryset(self)
			F: get_slug_field(self)
C: django.views.generic.detail.SingleObjectTemplateResponseMixin [ django.views.generic.detail.SingleObjectTemplateResponseMixin , django.views.generic.base.TemplateResponseMixin , builtins.object]
			P: content_type None
			P: response_class <class 'django.template.response.TemplateResponse'>
			P: template_engine None
			P: template_name None
			P: template_name_field None
			P: template_name_suffix _detail
			F: get_template_names(self)
			F: render_to_response(self,context,response_kwargs)
C: django.views.generic.edit.DeletionMixin [ django.views.generic.edit.DeletionMixin , builtins.object]
			P: success_url None
			F: delete(self,request,args,kwargs)
			F: get_success_url(self)
			F: post(self,request,args,kwargs)
C: django.views.generic.edit.FormMixin [ django.views.generic.edit.FormMixin , django.views.generic.base.ContextMixin , builtins.object]
			P: extra_context None
			P: form_class None
			P: initial {}
			P: prefix None
			P: success_url None
			F: form_invalid(self,form)
			F: form_valid(self,form)
			F: get_context_data(self,kwargs)
			F: get_form(self,form_class)
			F: get_form_class(self)
			F: get_form_kwargs(self)
			F: get_initial(self)
			F: get_prefix(self)
			F: get_success_url(self)		
C: django.views.generic.edit.ModelFormMixin [ django.views.generic.edit.ModelFormMixin , django.views.generic.edit.FormMixin , django.views.generic.detail.SingleObjectMixin , django.views.generic.base.ContextMixin , builtins.object]
			P: context_object_name None
			P: extra_context None
			P: fields None
			P: form_class None
			P: initial {}
			P: model None
			P: pk_url_kwarg pk
			P: prefix None
			P: query_pk_and_slug False
			P: queryset None
			P: slug_field slug
			P: slug_url_kwarg slug
			P: success_url None
			F: form_invalid(self,form)
			F: form_valid(self,form)
			F: get_context_data(self,kwargs)
			F: get_context_object_name(self,obj)
			F: get_form(self,form_class)
			F: get_form_class(self)
			F: get_form_kwargs(self)
			F: get_initial(self)
			F: get_object(self,queryset)
			F: get_prefix(self)
			F: get_queryset(self)
			F: get_slug_field(self)
			F: get_success_url(self)		
C: django.views.generic.list.MultipleObjectMixin [ django.views.generic.list.MultipleObjectMixin , django.views.generic.base.ContextMixin , builtins.object]
			P: allow_empty True
			P: context_object_name None
			P: extra_context None
			P: model None
			P: ordering None
			P: page_kwarg page
			P: paginate_by None
			P: paginate_orphans 0
			P: paginator_class <class 'django.core.paginator.Paginator'>
			P: queryset None
			F: get_allow_empty(self)
			F: get_context_data(self,object_list,kwargs)
			F: get_context_object_name(self,object_list)
			F: get_ordering(self)
			F: get_paginate_by(self,queryset)
			F: get_paginate_orphans(self)
			F: get_paginator(self,queryset,per_page,orphans,allow_empty_first_page,kwargs)
			F: get_queryset(self)
			F: paginate_queryset(self,queryset,page_size)

C: django.views.generic.list.MultipleObjectTemplateResponseMixin [ django.views.generic.list.MultipleObjectTemplateResponseMixin , django.views.generic.base.TemplateResponseMixin , builtins.object]
			P: content_type None
			P: response_class <class 'django.template.response.TemplateResponse'>
			P: template_engine None
			P: template_name None
			P: template_name_suffix _list
			F: get_template_names(self)
			F: render_to_response(self,context,response_kwargs)								


```