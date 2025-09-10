import base64

# The Base64-encoded string you want to decode
encoded_string = "R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT"


# Decode the Base64 string into bytes
decoded_bytes = base64.b64decode(encoded_string).decode()
print(decoded_bytes)

# If the original data was text, decode the bytes into a string
# using the appropriate encoding (e.g., 'utf-8', 'ascii')
decoded_string = decoded_bytes.decode('utf-8')

print(f"Original encoded string: {encoded_string}")
print(f"Decoded string: {decoded_string}")