from Crypto.Cipher import AES
from binascii import b2a_hex#, a2b_hex
import json

class aescrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC
    #加密函式，如果text不是16的倍數【加密文字text必須為16的倍數！】，那就補足為16的倍數
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        #這裡金鑰key 長度必須為16（AES-128）、24（AES-192）、或32（AES-256）Bytes 長度.目前AES-128足夠用
        length = 16
        count = len(text)
        if count % length != 0:
            add = length - (count % length)
        else:
            add = 0
        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        #因為AES加密時候得到的字串不一定是ascii字符集的，輸出到終端或者儲存時候可能存在問題
        #所以這裡統一把加密後的字串轉化為16進位制字串
        return str(b2a_hex(self.ciphertext),encoding='utf8')
    # def decrypt(self, text):
    #     cryptor = AES.new(self.key, self.mode, self.key)
    #     plain_text = cryptor.decrypt(a2b_hex(text))
    #     return plain_text.rstrip('\0')

def verify_key(phonenum, key):
    config = {}
    with open('./config.json') as f:
        config = json.load(f)
    pc = aescrypt(config['KEY'])
    real_key = pc.encrypt(phonenum)
    if real_key == key:
        return True
    return False

if __name__ == '__main__': #测试用例
    pc = aescrypt('keyskeyskeyskeys')   #初始化金鑰
    e = pc.encrypt("12345678901")
    # d = pc.decrypt(e)           
    print (e)