from django.shortcuts import render
from django.contrib.auth.views import logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from chest_xray.forms import DocumentForm

def index(request):
    context = {'request': request,
                'user': request.user}
    return render(request, 'chest_xray/index.html', context)


def login(request):
    return render(request, 'chest_xray/login.html', {})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def start(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            upload = True
    else:
        form = DocumentForm()
        upload = False

    return render(request, 'chest_xray/start.html', {'form': form, 'upload': upload})