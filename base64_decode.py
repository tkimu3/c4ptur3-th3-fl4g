#!/usr/local/bin/python3
import base64
text = 'RWFjaCBCYXNlNjQgZGlnaXQgcmVwcmVzZW50cyBleGFjdGx5IDYgYml0cyBvZiBkYXRhLg=='
byte = text.encode()
b64_decoded_byte = base64.b64decode(byte)
b64_decoded_str = b64_decoded_byte.decode()
print(f"ans:\t{base64.b64decode(byte).decode()}\n")
print(f"byte:\t{byte}\n")
print(f"b64_decoded_byte:\t{b64_decoded_byte}\n")
print(f"b64_decoded_str:\t{b64_decoded_str}\n")

