from prime_gen import n_bit_prime
from keygens import get_keys
from hashlib import sha3_256
import base64

def sha3(msg):
  hash = sha3_256(msg)
  return hash.digest()

def read_input():
  file = open("input.txt", "r")
  data = file.read()
  file.close()
  return data

def write_output(msg,filetxt):
  file = open(filetxt, "w")
  file.write(msg)
  file.close()


#msg=input("Enter message to encrypt: ")
#msg ='광야 æ ç ℅ Ñ'
msg = read_input()
msg_hash = sha3(base64.b64encode(bytes(msg, 'utf-8')))

KEYS = get_keys()
PUBLIC = KEYS[0]
PRIVATE = KEYS[1]

def enc(msg):
  enc=[]
  for i in range(0,len(msg)):
     enc.append(pow(msg[i],PUBLIC[0],PUBLIC[1]))
  return enc

def dec(c):
    dec = []
    for i in range(0,len(c)):
        dec.append(pow(c[i],PRIVATE[0],PRIVATE[1]))
    return dec

def dec_str(enc_b64):
    dec = ''
    for i in range (0,len(enc_b64)):
        e =  pow(enc_b64[i],PRIVATE[0],PRIVATE[1])
        dec += chr(e)
    return dec


msg_b64=base64.b64encode(bytes(msg, 'utf-8'))
c = enc(msg_b64)
dec = dec_str(c)

dec_bytes =  base64.b64decode(bytes(dec, 'utf-8'))
dec_str =  dec_bytes.decode("utf-8")


print('mensagem original: '+str(msg))
print('mensagem decodificada: '+dec_str)

dec_hash = sha3(base64.b64encode(bytes(dec_str, 'utf-8')))
print("sha3 da mensagem original == sha3 da mensagem decodificada do rsa?")
print(msg_hash == dec_hash)
answ = "sha3 da mensagem original == sha3 da mensagem decodificada do rsa?" + str(msg_hash == dec_hash)
print(msg_hash)
print(dec_hash)
