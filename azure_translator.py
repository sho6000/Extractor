import requests
import uuid


def translate_text(api_key, api_region, text, target_languages):
    endpoint = "https://api.cognitive.microsofttranslator.com/"
    path = '/translate'
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': api_key,
        'Ocp-Apim-Subscription-Region': api_region,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': text
    }]

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': target_languages
    }

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    print(response)
    return response

