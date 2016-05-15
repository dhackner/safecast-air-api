from django.http import HttpResponse, JsonResponse
from django.views.generic import View


from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RawReadingForm


class UploadRawReadingView(View):

    def post(self, request, *args, **kwargs):
        print 'daniel'
        print request.POST
        form = RawReadingForm(request.POST)
        if not form.is_valid():
            return JsonResponse(status=400, data=form.errors)

        form.save()
        return HttpResponse(status=201)
