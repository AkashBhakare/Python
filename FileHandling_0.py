# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 08:27:08 2021

@author: Akash
"""

# understand the encoding
string = "resume"
encoded_str = string.encode("utf-8")
print(encoded_str)


string = "résumé"
encoded_str = string.encode("utf-8")
print(encoded_str)

original_str = encoded_str.decode("utf-8")
print(original_str  )


# default encoding to the built-in open() is platform-dependent ( Unix : utf-8, Windows : cp1215 or utf-16    )

jap_string = "ひらがな"
print(f"Original Japanese String : {jap_string}\nLength : {len(jap_string)}")
encoded_str = jap_string.encode("utf-8")
print("Encoded Japanese String  :", encoded_str)
print(f"Encoded Japanese String :{len(encoded_str)}")

original_str = encoded_str.decode("utf-8")
print("Decoded jap String ",original_str)


original_str = encoded_str.decode("utf-16")
print("Decoded jap String ",original_str)

mar_string = "नमस्कार"

print(f"Original Marathi String : {mar_string}\nLength : {len(mar_string)}")
encoded_str = mar_string.encode("utf-8")
print(f"Encoded Marathi String : {encoded_str}\nLength : {len(encoded_str)}")

original_str = encoded_str.decode("utf-8")
print(original_str)

# Error UnicodeDecodeError
# original_str = encoded_str.decode("utf-32")
# print(original_str)


import locale
default_encoding = locale.getpreferredencoding()     
print("Default Encoding :",default_encoding)     

locale.setlocale(locale.LC_ALL, 'en_US')
print(locale.currency(1200))

locale.setlocale(locale.LC_ALL, 'de_DE')
print(locale.currency(1200))

locale.setlocale(locale.LC_ALL, 'mr_IN')
print(locale.currency(1200))

locale.setlocale(locale.LC_ALL, 'jp_JP')
print(locale.currency(1200))


# The length of a single Unicode character as a Python str will always be 1, 
# no matter how many bytes it occupies.

char = '😍'
print("length of 😍 :",len(char))
print("Code point of 😍 :",ord(char))

encoded_char = char.encode("utf-8")
print("encoded 😍 :",encoded_char)
print("length of encoded 😍 :",len(encoded_char))
print(f"Decoded Character :{encoded_char.decode('utf-8')}")

string = "अबकड"
print(string)
print("Length : ",len(string))
encoded_str = string.encode("utf-8")
print(f"Encoded String : {encoded_str}")
print("Length (encoded) :",len(encoded_str))





