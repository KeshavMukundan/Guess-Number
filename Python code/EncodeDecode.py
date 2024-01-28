import base64

def encode(string: str) -> bytes:
    encoded = base64.b64encode(string.encode())
    return encoded

def decode(string: bytes) -> str:
    try:
        decoded = base64.b64decode(string)
        return decoded
    except Exception as e:
        print(e)

def choice() -> None:
    while True:
        print("Enter 1 to Encode\nEnter 2 to Decode\nEnter 0 to exit\n")
        try:
            choose = int(input())
            if choose == 0:
                break
            
            elif choose == 1:
                ask = input("Enter a string to be encoded: ")
                print(encode(ask))
            
            elif choose == 2:
                ask = input("Enter a string to be decoded: ")
                print(decode(ask))
            
            else:
                print("Just 1 or 2 not anything else")
        except ValueError as e:
            print(e)
        
        
choice()