from django.shortcuts import get_object_or_404, render

from .models import Adjudication

# Create your views here.

def index(request):
    random_adjudication_list = Adjudication.objects.order_by('?')[:5]
    context = {'random_adjudication_list': random_adjudication_list}
    return render(request, 'decisions/index.html', context)

def detail(request, adjudication_id):
    adjudication = get_object_or_404(Adjudication, pk=adjudication_id)
    return render(request, 'decisions/detail.html', {'adjudication': adjudication})

