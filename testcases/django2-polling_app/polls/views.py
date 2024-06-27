from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.contrib import messages
from .models import Choice, Question


# Attack.Payload curl 'http://127.0.0.1:8000/polls/'
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5] # Taint.DB

# Attack.Payload curl 'http://127.0.0.1:8000/polls/3/' --cookie "tainted_cookie=<scriptalert(1)</script>"
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now()) # Taint.DB

    def dispatch(self, request, *args, **kwargs):
        messages.add_message(request, messages.INFO, 'Hello Tainted World. ' + request.COOKIES.get('tainted_cookie'))
        messages.info(request,'Tainted Cookie Value is %s' % request.COOKIES.get('tainted_cookie') )
        return super(DetailView,self).dispatch(request)

class ResultsView(generic.DetailView):
    model = Question # Taint.DB
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
