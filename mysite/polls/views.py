from django.http import HttpResponse

from .models import Question
from .serializers import QuestionListSerializer, QuestionDetailsSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    
    
class QuestionDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionDetailsSerializer
    
    def get_object(self):
        return get_object_or_404(Question, pk=self.kwargs.get('question_id'))

    
def index(request):

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)    

        
        
def detail(request, question_id):
    return HttpResponse("You're looking at question {} {}".format(question_id, 'asasdasd'))

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
