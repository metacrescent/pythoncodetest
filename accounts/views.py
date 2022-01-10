from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from accounts.forms import LoginForm


class LoginView(View):
    template_name = 'accounts/login.html'
    context = {}

    def get(self, request):
        user = request.user

        # if request.user.is_authenticated and user is not None and validate_user_tenant(user, tenant):
        #     return redirect(reverse('surveys'))

        self.context['form'] = LoginForm()

        return render(request, self.template_name, self.context)

    def post(self, request):
        form = LoginForm(request.POST)

        self.context['form'] = form

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'])

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect(reverse('home'))
            else:
                messages.warning(request, 'Invalid login credentials')
        else:
            messages.warning(request, form.errors)

        return render(request, self.template_name, self.context)
