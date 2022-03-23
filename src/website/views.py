import uuid

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, DetailView
from src.website.models import ScanImage
from . import ai_utils


@method_decorator(csrf_exempt, name='dispatch')
class HomeView(TemplateView):
    template_name = 'website/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name='website/home.html')

    def post(self, request, *args, **kwargs):
        from base64 import b64decode
        from core.settings import BASE_DIR, HOST_ADDRESS

        data_uri = request.POST['image']
        header, encoded = data_uri.split(",", 1)
        data = b64decode(encoded)

        name = str(str(uuid.uuid4()) + '.jpg')
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
            x = ai_utils.run(path)
            stress = 0
            if x == 'Fear':
                stress = 90
            if x == 'Angry':
                stress = 37
            if x == 'Disgust':
                stress = 52
            if x == 'Happy':
                stress = 95
            if x == 'Sad':
                stress = 65
            if x == 'Surprise':
                stress = 80
            if x == 'Neutral':
                stress = 20

            s = ScanImage.objects.create(image_url=address, stress_level=stress, status=x)
        return HttpResponse(s.pk)


class ImageListView(ListView):
    queryset = ScanImage.objects.all()
    template_name = 'website/scanimage_list.html'
    paginate_by = 20


class ImageDetailView(DetailView):
    model = ScanImage
    template_name = 'website/scanimage_detail.html'
