import requests
from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == 'GET':

        number_a = request.GET.get('a')
        number_b = request.GET.get('b')

        try:
            if number_a is None and number_b is None:
                return HttpResponse('<html>'
                                    '<h1>Welcome to simple calculator</h1>'
                                    'add these parameter to calculate<br>'
                                    '?a=integer&b=integer'
                                    '<h4>Example:</h4>'
                                    '<a href="?a=10&b=20">Click This</a>'
                                    '</html>', status=200)
            elif number_a is None:
                number_a = 0
            elif number_b is None:
                number_b = 0

            the_data = {
                'a': number_a, 'b': number_b
            }

            headers = {
                'Content-Type': 'application/json'
            }
            # Call api
            # LOCAL
            # response = requests.post(url='http://localhost:8000/',
            #                          headers=headers, json=the_data)

            # AZURE
            response = requests.post(
                'https://law-01-rest.azurewebsites.net/', headers=headers,
                json=the_data)

            json_response = response.json()

            return HttpResponse(
                f'<html>{json_response.get("hasil", "Error")}</html>')
            # return HttpResponse(f'<html>a</html>')

        except:
            return JsonResponse({
                'error': 'Incorrect parameter, must be integer'
            }, status=400)

    else:
        return HttpResponse('Method not allowed', status=405)
