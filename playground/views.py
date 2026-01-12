from django.shortcuts import render
from rest_framework.views import APIView
import logging
import requests


logger = logging.getLogger(__name__)


class HelloView(APIView):
    def get(self, request):
        try:
            logger.info('Calling Httpbin ')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httbin is offline')

        return render(request, 'hello.html', {'name': 'Shery'})