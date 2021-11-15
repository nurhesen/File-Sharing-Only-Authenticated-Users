from django.shortcuts import render
from django.http import HttpResponseRedirect, request
from django.urls import reverse
from .models import Fayl, Paylas, Serh
from .forms import FaylForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.http import JsonResponse
from django import forms
from django.forms.utils import ErrorList
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.shortcuts import resolve_url
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect



class LoginView(auth_views.LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        return resolve_url('taskapp:home')

def RegisterView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('taskapp:login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/user_form.html', {'form': form})

@login_required(login_url='/login')
def Home(request):
    if request.method == 'POST':
        form = FaylForm(request.POST, request.FILES)
        if form.is_valid():
            res=form.save(commit=True, user=request.user)
            Paylas.objects.create(kimle=request.user, fayl=res,serh_yaza_biler=True)
            return HttpResponseRedirect(reverse('taskapp:detail', kwargs={'pk': res.id}))
    else:
        form = FaylForm()

    Fayls = Fayl.objects.all()

    return render(request,
        'taskapp/home.html',
        {'Fayls': Fayls, 'form': form},
    )




class FaylDetail(DetailView):

    model = Fayl

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gore_biler=Paylas.objects.filter(kimle=self.request.user, fayl=context['fayl'])

        if gore_biler:
            if context['fayl'].muellif==self.request.user:
                context['muellifdir']=True
                context['userler']=User.objects.all()
            context['yaza_biler']=gore_biler[0].serh_yaza_biler
            return context


class FaylCreateView(CreateView):
    model = Serh
    fields = ['fayl', 'komment']

    def form_valid(self, form):
        serh=form.save(commit=False)
        serh.user=self.request.user
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def post(self, request, *args, **kwargs):
        yaza_biler=Paylas.objects.filter(kimle=self.request.user, fayl=request.POST['fayl'])[0].serh_yaza_biler
        if not yaza_biler:
            return HttpResponse('Serh yaza bilmezsiniz')
        self.object = None
        return super().post(request, *args, **kwargs)


    def get_success_url(self):
        return reverse('taskapp:detail', kwargs={'pk': self.object.fayl.pk})



class PaylasView(CreateView):
    model = Paylas
    fields = ['kimle', 'fayl', 'serh_yaza_biler']

    def post(self, request, *args, **kwargs):
        curr_fayl=Fayl.objects.filter(id=request.POST['fayl'])[0]
        if not curr_fayl.muellif==request.user:
            return HttpResponse('Siz muellif deyilsiniz')
        self.object = None
        return super().post(request, *args, **kwargs)



    def get_success_url(self):
        return reverse('taskapp:detail', kwargs={'pk': self.object.fayl.pk})
