from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages


from .models import Adjudication, UserProfile
from .forms import DecisionForm
from django.contrib.auth.forms import UserCreationForm



# Create your views here.

def index(request):
    random_adjudication_list = Adjudication.objects.order_by('?')[:5]
    if request.user.is_authenticated():
        current_user = request.user
        user_profile = UserProfile.objects.get(id=current_user.id)
        return render(request, 'decisions/index.html', {'random_adjudication_list':random_adjudication_list, 'user_profile':user_profile})
    return render(request, 'decisions/index.html', {'random_adjudication_list': random_adjudication_list})


def detail(request, adjudication_id):
    correct_response = -1
    adjudication = get_object_or_404(Adjudication, pk=adjudication_id)
    if request.method == "POST":
        form = DecisionForm(request.POST)
        if form.is_valid():
            decision = form.save(commit=False)
            decision.user_id = request.user
            decision.adjudication_id = adjudication
            decision.timestamp = timezone.now()
            decision.save()
            if decision.answer == adjudication.outcome:
                correct_response = 1
            else:
                correct_response = 0
    else:
        form=DecisionForm()

    if request.user.is_authenticated():
        current_user = request.user
        user_profile = UserProfile.objects.get(id=current_user.id)
        return render(request, 'decisions/detail.html', {'adjudication': adjudication, 'form': form, 'correct_response':correct_response, 'user_profile':user_profile})
    

    return render(request, 'decisions/detail.html', {'adjudication': adjudication, 'form': form, 'correct_response':correct_response})

def random(request):
    random_adjudication = Adjudication.objects.order_by('?')[:2]
    # adjudication = get_object_or_404(Adjudication, pk=adjudication_id)
    return redirect('/decisions/{}'.format(random_adjudication[0].id))

def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            username = f.cleaned_data.get('username')
            user = User.objects.get(username = username)
            new_user_profile = UserProfile(user_id = user.id, num_guesses = 0, num_correct_guesses = 0)
            new_user_profile.save()
            messages.success(request, 'Account created successfully')
            return redirect('/decisions')

    else:
        f = UserCreationForm()

    return render(request, 'cadmin/register.html', {'form': f})


