# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 19:47:02 2021

@author: Akash
"""


# The so-called CSV (Comma Separated Values) format is the most common 
# import and export format for spreadsheets and databases.
import csv

# Python CSV reader with defaul delimiter
def  simpleReaderExample():
    # file = open('numberdata1.csv', 'r')

    with open('Marks.csv', 'r') as fileObject:
        # Return a reader object (iterator) which will iterate over lines 
        # in the given csvfile.
        csv_reader = csv.reader(fileObject) #default delimiter ','
        for row in csv_reader:
            # print(row)  #List
            for field in row:
                print(field,end=", ")
            print()

# Python CSV reader with different delimiter
def  simpleReaderDelimiter():
   
    with  open('namedata.csv', 'r') as file:
        reader = csv.reader(file,delimiter='|')
        dash_line = f"\n{'-'*55}"
        for record in reader:
            # print("No. of fields :",len(record))
            print(dash_line)
            for field in record:
                print(f"{field:15}",end=" ")
    print(dash_line)
            
# Every row that is read is a List
def csvReader():
    
    with open('employeeBD.csv') as input_file:
        csv_reader = csv.reader(input_file)
        line_count = 0
        
        for row in csv_reader: # Row is List
            # print("type of row : ",type(row))
            if line_count == 0:
                # print(type(row))
                print(f'Column names are {", ".join(row)}')
            else:
                print(f'\t{line_count:>3}. {row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
            
        print(f'Processed {line_count-1} records.')

def list_all_dialects():
    # Return the names of all registered dialects.
    dialects_list = csv.list_dialects()
    print("Supported Dialects are as follows:")
    for dialect in dialects_list:
        print(f"\t{dialect}")


# The csv.writer() method returns a writer object which converts the user's data into delimited strings on the given file-like object.
def csv_writer(dataList, fileName):
    """
    Write data to a CSV file path
    """
    # if newline is specified as '' or '\n' while 
    # opening the file then no translation will occur
    with open(fileName, mode="w",newline='') as output_file:
        # dialect = excel
        writer = csv.writer(output_file, 
                            dialect='excel',  
                            delimiter=',',
                            lineterminator='\n')
        # dialect = unix
        # writer = csv.writer(output_file, dialect='unix',  delimiter=',')
        # dialect = excel-tab
        # writer = csv.writer(output_file, dialect='excel-tab')
        line_counter = 0
        for alist in dataList:
            line_counter += 1
            writer.writerow(alist)
            
    print(f'Wrote {line_counter} lines.')
  

# The csv.DictReader class operates like a regular reader but maps the information read into a dictionary. The keys for the dictionary can be passed in with the fieldnames parameter or inferred from the first row of the CSV file.
        
def csvDictReader():
    with open('employeeBD.csv', mode='r') as input_file:
        csv_dict_reader = csv.DictReader(input_file, dialect='excel')
        print(type(csv_dict_reader))  # csv.DictReader
        print(csv_dict_reader)
        row = csv_dict_reader.__next__()
        print(type(row))  # collections.OrderedDict
        
        print(row)   # OrderedDict
        # print(f'Column names are {", ".join(row)}')
        line_count = 1
        for row in csv_dict_reader: # row : OrderedDict
            print(f'\t{row["Name"]} works in the {row["Department Name"]}\
 department, and was born in {row["Birthday month"]}.')
            line_count += 1
            
        print(f'Processed {line_count} records.')

        
def csvDictReader_search():
    with open('employeeBD.csv', mode='r') as input_file:
        csv_dict_reader = csv.DictReader(input_file, dialect='excel')
        name = input('Please enter the employees name : ')
       
        for record_dict in csv_dict_reader: 
            if(record_dict['Name'].upper()==name.upper()):
                print(f'\t{record_dict["Name"]} works in the \
 {record_dict["Department Name"]} department, \
 and was born in {record_dict["Birthday month"]}.')
                return
        else:
            print(f'{name} not found' )
        
        
def csvDictWriter(filename, columnNames, my_list):
    """
    Writes a CSV file using DictWriter
    """
    import os.path
    path = os.path.realpath(filename)
    with open(path, "w",newline='') as out_file:
#        print(fieldnames)
        writer = csv.DictWriter(out_file,delimiter=',', fieldnames=columnNames)
        writer.writeheader( )
        # write_one_row_at_time(writer,my_list)
        write_all_rows_at_once(writer,my_list)
      
    
def write_one_row_at_time(writer, mydata_list):
    for row in mydata_list:
        writer.writerow(row)   
    
def  write_all_rows_at_once(writer,my_list):
    writer.writerows(my_list)
    
    
def readWithPandas():
    import pandas
    df = pandas.read_csv('dict_output.csv')
    # print(type(df))
    print(df)
    print()
    
 
def readWithPandas_withindex():
    import pandas
    df = pandas.read_csv('dict_output.csv', index_col='city')
    print(df)   
    print()
    
   
def readExcelfile():
    import pandas
    
    print(".xls files require xlrd to be installed" )
    data = pandas.read_excel('d:/python/programs/registration1.xls', sheet_name='Sheet2',index_col='Email')
    print(data)
    
    print(".xlsx files require openpyxl to be installed" )
    data = pandas.read_excel('d:/python/programs/registration.xlsx', sheet_name='Sheet2',index_col='Email')
    print(data)
    print("\n************")

    
if __name__ == "__main__":    
    # simpleReaderExample()   
    # simpleReaderDelimiter()
    # csvReader()
    # list_all_dialects()
  # 
    #Write data to a CSV file path
     # data = ["first_name:last_name:city:0".split(":"),
     #            'amit\'s:shinde:pune:13'.split(":"),
     #            "sushant:pailwal:sangli:14".split(":"),
     #            "trishant:nimsankar:nasik:15".split(":"),
     #            "chetan:pujari:baramati:16".split(":"),
     #            "saikrashna:vittanala:tumkur:17".split(":"),
     #            "abhishek:kamble:nagar:18".split(":")
     #            ]
     # filename = "output.csv"
     # csv_writer(data, filename)
  
#     csvDictReader()
#     csvDictReader_search()
# #  Writes a CSV file using DictWriter  
#     data = ["first_name,last_name,city".split(","),
#             "Amit,Shinde,Pune".split(","),
#             "Sushant,Pailwal,Sangli".split(","),
#             "Trishant,Nimsankar,Nasik".split(","),
#             "Chetan,Pujari,Baramati".split(","),
#             "Saikrashna,Vittanala,Tumkur".split(","),
#             "Abhishek,Kamble,Nagar".split(",")
#             ] 
#     my_list = []
#     columnNames = data[0]
#     for values in data[1:]:
#         inner_dict = dict(zip(columnNames, values))
#         # print(inner_dict)
#         my_list.append(inner_dict)
#     print(my_list)
#     filename = "dict_output.csv"
#     csvDictWriter(filename, columnNames, my_list)
    
     readWithPandas()
     readWithPandas_withindex()
     readExcelfile()