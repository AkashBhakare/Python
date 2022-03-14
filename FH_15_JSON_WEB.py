# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 06:31:42 2021

@author: Akash
"""


# Encoding and Decoding Simple Data Types
# import urllib
from urllib import request
import json
 # This module provides functions for encoding binary data to printable ASCII characters
import base64

def download_data(url):
    response = request.urlopen(url)
    json_data = response.read()
     # Deserialize s (a str, bytes or bytearray instance containing a JSON document) to a Python object.
    decoded = json.loads(json_data)
    # print(decoded)     
    indent_data(decoded)
    
def indent_data(decoded):
    # print('DATA:', repr(decoded))
    print( json.dumps(decoded, sort_keys=True, indent=5))
   
def image_demo(image_file_name, json_file_name):
   
    with open(image_file_name,"rb") as img_file:
        imagedata = img_file.read()
  
    data = {}
    # Encode the bytes-like object imagedata, 
    # which can contain arbitrary binary data, 
    # and return bytes containing the base64-encoded data
    encoded_byte_data = base64.encodebytes(imagedata)
    # Decode the contents of the binary input file and 
    # write the resulting binary data to the output file. 
    # input and output must be file objects.
    data['img'] = encoded_byte_data.decode('utf-8')
    
    #Alternatively : just one line
    # data['img'] = base64.encodebytes(imagedata).decode('utf-8')
    
    import datetime
    author_dict ={
        "native":"রবীন্দ্রনাথ ঠাকুর",
        "name" : "Robindronath Tagore",
        "born" : datetime.date(1861, 5, 7).__str__(),
        "children" :  5,
        "photo" : data
        }
    # Serialize object author_dict as a JSON string
    json_str = json.dumps(author_dict)
    
    output_file = open(json_file_name,"w")
    output_file.write(json_str)
    output_file.close()        

def parseJSON(json_file, image_file):
    file_object = open(json_file,"r")
    json_data = file_object.read()
     # Deserialize s (a str, bytes or bytearray instance containing a JSON document)
     # to a Python object.
    decoded = json.loads(json_data)
    print("Name of author : ",decoded["name"])
    print("Name Native : ",decoded["native"])
    print("Number of children : ",decoded["children"])
    print("Born : ",decoded["born"])
    
    img_data = decoded["photo"]
    # print(img_data['img'])
    encode_img = img_data['img'].encode("utf-8")
    # Decode the bytes-like object s, 
    # which must contain one or more lines of base64 encoded data, 
    # and return the decoded bytes.
    decode_img_data = base64.decodebytes(encode_img)
    img_file_object = open(image_file,'wb')
    img_file_object.write(decode_img_data)
    img_file_object.close()
    file_object.close()

if __name__ == '__main__':
    url = "https://api.nasa.gov/planetary/apod?api_key=mccLeBfvFkCCKS7CCDyIoxgykVruzZey8rhIZmMu"
    url = "https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=mccLeBfvFkCCKS7CCDyIoxgykVruzZey8rhIZmMu"
    url = "http://vocab.nic.in/rest.php/orgn/intr/im/json"
    
    url ="http://vocab.nic.in/rest.php/country/json"

    download_data(url)
  
    
    # Indian Mission data
    # http://vocab.nic.in/rest.php/orgn/intr/im/json
    
    
    image_file_name = "birthday.jpg" # tagore.jpg
    json_file_name = "author.txt"
    image_demo(image_file_name,json_file_name)
    parseJSON(json_file_name,"birth123.jpg")
    
    
