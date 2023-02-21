from django.shortcuts import render, redirect
from question.forms import AskMeForm
from question.models import AskMe
# Create your views here.


def add_question(request):
    fm = AskMeForm()
    questions = AskMe.objects.all()
    if request.method == 'POST':
        fm = AskMeForm(request.POST)
        fm.is_valid()
        fm.save()
        return redirect('add_question')
    return render(request, 'add_question.html', {'form': fm, 'questions': questions})
