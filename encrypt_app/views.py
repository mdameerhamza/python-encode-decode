from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import PayloadEncoderDecoder
from .models import EncodedPayload

salt_key = "wajid"  
salt_index = "123" 

@csrf_exempt
def encode_payload(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        payload = data.get('payload', '')
        encoder_decoder = PayloadEncoderDecoder(salt_key, salt_index)
        encoded_payload = encoder_decoder.encode_payload(payload)
        
        # Store encoded payload in the database
        encoded_payload_entry = EncodedPayload(payload=encoded_payload)
        encoded_payload_entry.save()
        
        return JsonResponse({'encoded_payload': encoded_payload}, status=200)
    return JsonResponse({'error': 'POST method required.'}, status=400)

@csrf_exempt
def decode_payload(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        encoded_payload = data.get('encoded_payload', '')
        encoder_decoder = PayloadEncoderDecoder(salt_key, salt_index)
        try:
            decoded_payload = encoder_decoder.decode_payload(encoded_payload)
            return JsonResponse({'decoded_payload': decoded_payload}, status=200)
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'POST method required.'}, status=400)
