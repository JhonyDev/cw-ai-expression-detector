import uuid

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, DetailView
from src.website.models import ScanImage, Session
from . import ai_utils
from django.forms.models import model_to_dict
from rest_framework.response import Response

from .serializers import ScanImageSerializer


@method_decorator(csrf_exempt, name='dispatch')
class HomeView(TemplateView):
    template_name = 'website/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name='website/home.html')

    def post(self, request, *args, **kwargs):
        from base64 import b64decode
        from core.settings import BASE_DIR, HOST_ADDRESS

        data_uri = request.POST['image']
        session_pk = request.POST['session_pk']
        header, encoded = data_uri.split(",", 1)
        data = b64decode(encoded)

        name = str('static_image.jpg')
        path = f"{BASE_DIR}\\media\\images\\{name}"
        address = f"images\\{name}"
        with open(path, "wb") as f:
            f.write(data)
            '''
                Angry - 30 - 43
                Disgust - 44 - 58
                Fear - 87 - 100
                Happy - 0 - 14 
                Sad - 59 - 73
                Surprise - 74 - 86
                Neutral - 15 - 29
                '''
            x, new_address = ai_utils.run(path)
            if new_address is not None:
                address = new_address
            stress = 0
            if x == 'Fear':
                stress = 90
            if x == 'Angry':
                stress = 37
            if x == 'Disgust':
                stress = 52
            if x == 'Happy':
                stress = 5
            if x == 'Sad':
                stress = 65
            if x == 'Surprise':
                stress = 80
            if x == 'Neutral':
                stress = 20

        try:
            session = Session.objects.get(pk=session_pk)
        except Session.DoesNotExist:
            return JsonResponse({'error': 'session not found'})
        s = ScanImage.objects.create(session=session, image_url=address, stress_level=stress, status=x)
        return JsonResponse(ScanImageSerializer(s).data)


class ImageListView(ListView):
    queryset = ScanImage.objects.all()
    template_name = 'website/scanimage_list.html'
    paginate_by = 20

    def get_queryset(self):
        return ScanImage.objects.filter(session=self.kwargs['pk'])


class ImageDetailView(DetailView):
    model = ScanImage
    template_name = 'website/scanimage_detail.html'


class SessionListView(ListView):
    model = Session
    template_name = 'website/session_list.html'


class StartSession(View):

    def get(self, request):
        print('Creating session')
        session = Session.objects.create(user=self.request.user)
        response = {
            'session_pk': session.pk,
        }
        return JsonResponse(data=response, safe=False)
