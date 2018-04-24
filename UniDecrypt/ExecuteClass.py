import base64
import binascii
import hashlib

class Execute(object):

    def base64_encode(self, str):
	    print(base64.b64encode(str.encode('utf8')))
        
    def base64_decode(self, str):
	    print(base64.b64decode(str.encode('utf8')))

    def str_to_hex(self, str):
        line = binascii.hexlify(str.encode('utf8'))
        print(line)

    def hex_to_str(self, str):
        line = binascii.unhexlify(str).decode('utf8')
        print(line)
		
    def md5_encode(self, str):
        line = hashlib.md5(str.encode('utf-8')).hexdigest()
        print(line)
		
    def xor_two_hex(self, str1, str2):
        print(hex(int(str1, 16) ^ int(str2, 16)))
		
    def xor_two_strings_in_hex(self, str1, str2):
        line1 = binascii.hexlify(str1.encode('utf8'))
        line2 = binascii.hexlify(str2.encode('utf8'))
        print(hex(int(line1, 16) ^ int(line2, 16)))
	