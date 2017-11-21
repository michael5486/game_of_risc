from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone

from .models import Adjudication

from .forms import DecisionForm

# Create your views here.

def index(request):
    random_adjudication_list = Adjudication.objects.order_by('?')[:5]
    context = {'random_adjudication_list': random_adjudication_list}
    return render(request, 'decisions/index.html', context)

# def detail(request, adjudication_id):
#     adjudication = get_object_or_404(Adjudication, pk=adjudication_id)
#     return render(request, 'decisions/detail.html', {'adjudication': adjudication})


def detail(request, adjudication_id):
    # if request.method == "POST":
    #     form = DecisionForm()
    #     if form.is_valid():
    #         newDecision = form.save(commit=False)
    #         newDecision.save()
    #         return render(request, 'decisions/result.html', {'form': form})
    # else:
    #     form = DecisionForm()
    adjudication = get_object_or_404(Adjudication, pk=adjudication_id)
    return render(request, 'decisions/detail.html', {'adjudication': adjudication})

def result(request):
    if request.method == "POST":
        form = DecisionForm(request.POST)
        if form.is_valid():
            newDecision = form.save(commit=False)
            newDecision.save()
            return redirect('decisions/result.html', pk=adjudication_id)
        else:
            form = DecisionForm()
    return render(request, 'decisions/result.html', {'form': form})

def decision_new(request):
    if request.method == "POST":
        form = DecisionForm(request.POST)
        if form.is_valid():
            decision = form.save(commit=False)
            decision.timestamp = timezone.now()
            decision.save()
            return redirect('https://www.google.com')
    else:
        form=DecisionForm()
    return render(request, 'decisions/decision_edit.html', {'form': form})




