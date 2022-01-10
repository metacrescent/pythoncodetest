from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from bigpixel.forms import ShowPixelCodeForm, PixelTrackingCodeSiteForm
from bigpixel.selectors import pixel_tracking_code_exists, fetch_pixel_tracking_code
from bigpixel.services import create_user_pixel_tracking_code, validate_user_pixel_tracking_code


class HomeView(LoginRequiredMixin, View):
    template_name = 'bigpixel/generate_code.html'
    context = {}

    def get(self, request):
        # check if pixel tracking code is already generated
        self.context['pixel_tracking_code_exists'] = pixel_tracking_code_exists(user=request.user)

        # fetch pixel tracking code if already generated
        if self.context['pixel_tracking_code_exists']:
            self.context['pixel_tracking_code'] = fetch_pixel_tracking_code(user=request.user)
            self.context['pixel_code_preview'] = ShowPixelCodeForm(instance=self.context['pixel_tracking_code'])
            self.context['pixel_code_validation_form'] = PixelTrackingCodeSiteForm(initial={
                'tracking_code': self.context['pixel_tracking_code'],
                'website': 'https://demo.code.com'
            })
        return render(request, self.template_name, self.context)


class GeneratePixelCodeView(LoginRequiredMixin, View):
    def post(self, request):
        if pixel_tracking_code_exists(user=request.user):
            messages.warning(request, 'Code already generated')
        else:
            if create_user_pixel_tracking_code(user=request.user):
                messages.success(request, 'Code successfully generated')
            else:
                messages.warning(request, 'Something went wrong. Please try again')

        return redirect(reverse('home'))


class ValidatePixelCodeIntegrationView(LoginRequiredMixin, View):
    def post(self, request):
        # send a ping request user url and check if tracking code is available
        # ping can respond with status i.e valid, invalid, unreachable
        form = PixelTrackingCodeSiteForm(request.POST)
        if form.is_valid():

            # get ping result
            ping_result = 'valid'
            pixel_tracking_code = form.cleaned_data['tracking_code']
            website = form.cleaned_data['website']
            validate_user_pixel_tracking_code(pixel_tracking_code=pixel_tracking_code,
                                              website=website,
                                              ping_result=ping_result)
            messages.success(request, 'Website status updated successfully')
        else:
            messages.warning(request, form.errors)

        return redirect(reverse('home'))
