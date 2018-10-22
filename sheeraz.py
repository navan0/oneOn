from Crypto.Cipher import AES

def pad(s):
    s += chr(16 - len(s)%16)*(16 - len(s)%16)
    return s

key = "\xa2q\x8bu6Y\xa1\rT\xb7\xce\x86\x81S\xf2\xfc"
flag = open("flag.txt").read()
obj1 = AES.new(key, AES.MODE_ECB)
ct = obj1.encrypt(pad(flag))
open("ciphertext.txt",'w').write(ct)
