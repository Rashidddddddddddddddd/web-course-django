from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import Group
from .models import Choice, Question
from .forms import ChoiceForm

# Create your views here.
def savollar(request):
    #bu yerda question modeldagi barcha objectlar olinadi
    savollar = Question.objects.all()
    return render(
        request, 'questions/savollar.html', {'savollar': savollar})

def savol_detail(request, id):
    # buyerda Question modelardan id si parametrda kelyotgan
    # id ga teng bo'lgan object olinadi
    savol = get_object_or_404(Question, id=id)
    return render(request, 'questions/savol.html', {"savol": savol})



def check_answer(request, variant_id):
    # bu yerda Choice modelardan id si parametrda kelayotgan
    # variant_id ga teng bo'lgan object olinadi
    javob = get_object_or_404(Choice, id=variant_id)
    correct = javob.is_correct
    return render(request, 'questions/checked.html', {'correct': correct})

def create_question(request):
    if request.method == "POST":
        question = request.POST.get('question')
        Question.objects.create(question=question)
        return redirect('poll:savollar')
    return render(request, 'questions/create_question.html')

def create_group(request):
    if request.method == "POST":
        group = request.POST.get('group')
        Group.objects.create(name=group)

        return redirect("poll:groups")
    return render(request, 'questions/create_group.html')

def groups(request):
    gruppalar = Group.objects.all()
    return render(request, 'groups.html', {'gruppalar': gruppalar})

def deleteQuestion(request, id):
    question = Question.objects.get(id=id)
    question.delete()
    return redirect("poll:savollar")

def create_choice(request):
    form = ChoiceForm()
    if request.method == "POST":
        form = ChoiceForm(data=request.POST)
        if form.is_valid():
            choice = form.save()
            return redirect("poll:savollar")
    return render(request, 'questions/create_choice.html', {"form": form})

