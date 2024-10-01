# payload_encoder/utils.py
import base64
import json

class PayloadEncoderDecoder:
    def __init__(self, salt_key, salt_index):
        self.salt_key = salt_key
        self.salt_index = salt_index

    def encode_payload(self, payload):
        # Convert payload to JSON string if it's a dictionary
        if isinstance(payload, dict):
            payload = json.dumps(payload)
        # Encode payload to base64
        encoded_payload = base64.b64encode(payload.encode()).decode()
        # Append salt key and salt index
        encoded_with_salt = f"{encoded_payload}_{self.salt_key}_{self.salt_index}"
        return encoded_with_salt

    def decode_payload(self, encoded_with_salt):
        # Split the encoded_with_salt string
        try:
            encoded_payload, salt_key, salt_index = encoded_with_salt.rsplit('_', 2)
        except ValueError:
            raise ValueError("Invalid encoded string format")
        
        # Verify salt key and salt index
        if salt_key != self.salt_key or salt_index != self.salt_index:
            raise ValueError("Invalid salt key or salt index")
        
        # Decode base64 payload
        decoded_payload = base64.b64decode(encoded_payload.encode()).decode()
        
        # Attempt to parse the decoded payload as JSON
        try:
            decoded_payload = json.loads(decoded_payload)
        except json.JSONDecodeError:
            pass
        
        return decoded_payload
