from django.shortcuts import render
from .forms import MyForm
from .models import Destination


# Create your views here.


def about(request):
    if request.method == 'POST':
        form = MyForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            dests = Destination.objects.all()
            return render(request, 'res.html', {'dests': dests})
    else:
        form = MyForm()
    return render(request, 'about.html',  {'form': form})
