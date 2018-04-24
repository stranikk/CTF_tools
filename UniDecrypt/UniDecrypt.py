import sys
from ExecuteClass import *

def main(): 

    get_exe = Execute()
    if (str(sys.argv[1]) == "-h"):
        print("-h - help")
        print("[-be input_string] - encode string to base64")
        print("[-bd input_string] - decode base64 to string")
        print("[-strhex input_string]- string to hex")
        print("[-hexstr input_string]- hex to string")
        print("[-md5 input_string]- encode string to md5")
        print("[-xorhex str1 str2] - xor two hex")
        print("[-xorstrhex str1 str2] - xor two string in hex")
		
    if (str(sys.argv[1]) == "-be"):
        get_exe.base64_encode(str(sys.argv[2]))
		
    if (str(sys.argv[1]) == "-bd"):
        get_exe.base64_decode(str(sys.argv[2]))
   
    if (str(sys.argv[1]) == "-strhex"):
        get_exe.str_to_hex(str(sys.argv[2]))
		
    if (str(sys.argv[1]) == "-hexstr"):
        get_exe.hex_to_str(str(sys.argv[2]))
		
    if (str(sys.argv[1]) == "-md5"):
        get_exe.md5_encode(str(sys.argv[2]))
		
    if (str(sys.argv[1]) == "-xorhex"):
        get_exe.xor_two_hex(str(sys.argv[2]), str(sys.argv[3]))
	
    if (str(sys.argv[1]) == "-xorstrhex"):
        get_exe.xor_two_strings_in_hex(str(sys.argv[2]), str(sys.argv[3]))
		
if __name__ == "__main__":
    main()