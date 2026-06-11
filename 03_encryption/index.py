import base64
# 
# def encrypt_pass(password):
    # encoded_bytes = base64.b64encode(password.encode())
    # print(encoded_bytes)
# 
# user_pass = input("Enter your password: ")
# encrypt_pass(user_pass)
# 

def decode_pass(password):
    decoded_bytes = base64.b64decode(password)
    decoded_data = decoded_bytes.decode()
    print(f"Decoded data: {decoded_data}")

encode_string = input("Enter the base 64 string: ")
decode_pass(encode_string)
