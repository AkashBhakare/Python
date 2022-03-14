# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 07:27:45 2021

@author: Akash
"""


# shutil : High Level File Operations
import shutil
import os
import sys

def print_list(mylist:list)->None:
    print("The list contents are as follows")
    for item in mylist:
        print(item)
        
        
def listfile_demo():
        #return a list containing the names of the files in the directory.
        # print( os.listdir('.')) # lists current directory
        # print_list(os.listdir('.'))
    
        # print("listing of files and directories")
        # print( "=>","\n=> ".join(os.listdir('.')))
        print( "\n=> ".join(os.listdir(path="B:/programs/"))) # list specified directory

    
def listing_dir():
    import pprint
    #change the current working directory
    os.chdir("d:/python/group")
    # Listing current directory
    print('\nList current directory:')
    pprint.pprint(os.listdir('.'))
    input("Press a key..")
    
    # Listing sub directory
    # print('\nList sub directory:' )
    # pprint.pprint(os.listdir('./__pycache__'))
    # input("Press a key..")
    
    # os.chdir("B:/programs/group/strings")
    # print('\nList current sub-directory:')
    # pprint.pprint(os.listdir('.'))
    # input("Press a key..")
     
    # Listing parent directory
    # print('\nList parent directory:')
    # pprint.pprint(os.listdir('..'))
    # input("Press a key..")
 


def create_dir():
    import os
    # define the name of the directory to be created
    path = "e:/temp/year"
    try:
        os.mkdir(path)
    except OSError: 
        print (f"Creation of the directory {path} has failed")
    else:
        print (f"Successfully created the directory {path}")
        
def create_dirs():
    import os

# define the name of the directory to be created
    path = "e:/temp/year/month/week/day/hour/min/sec"
    try:
        os.makedirs(path)
    except OSError:
        print (f"Creation of the directory {path} failed" )
    else:
        print (f"Successfully created the directory {path} ")

def delete_file():
    """Deleting File"""
    fileToDelete = r"e:/temp/data.txt"
    try:
        os.remove(fileToDelete)
    except FileNotFoundError as fnfe:
        print(fnfe)
    else:
        print(f'file {fileToDelete} has been deleted')

# Copy a file to a new file in current directory only.
# shutil.copyfile(src, dst, *, follow_symlinks=True)
# Copy the contents (no metadata) of the file named src to a 
# file named dst and return dst in the most efficient way possible. 
# src and dst are path-like objects or path names given as strings.
def copyfile_demo():
    import pprint
    print("\nBefore Copying")
    try:
        pprint.pprint(os.listdir(path="e:/temp"))
        src    = "d:\stories.txt"
        # dest = "d:/wkdir/abc/debug/readyou.txt"
        dest   = "e:/temp/story.txt"
    
        shutil.copyfile(src, dest)
        
        print("\nAfter Copying")
        pprint.pprint(os.listdir(path="e:/temp"))
    except FileNotFoundError as fnfe:
        print(fnfe,file=sys.stderr)
        
# create the shortcut using operating system command like mkink
def copysymlink_demo():
    # copy with symlinks (default is follow_symlinks=True)
    # shutil.copyfile('e:/test/read.lnk', 'readlink.txt')
    shutil.copyfile(R"d:\Python\myspyder.lnk", 
                    R'F:\TEMP\myspyder.ico',
                    follow_symlinks=False)
    print("is src a link ? ",os.path.islink(R"d:\Python\myspyder.lnk"))
    print("is dest a link ? ",os.path.islink(R'F:\TEMP\myspyder.ico'))
    # shutil.copyfile('d:/titan.lnk', 'd:/wkdir/titan.csv')

def copyfile_to_dir():
 # Copy file from current directory to specified sub-directory
    #shutil.copy(src_file, dst_dir, *, follow_symlinks=True)
    # shutil.copy('wheel.py', 'pack')
    # Copy File from one directory to another directory
    srcFile = r"e:\MySql\V37661-01.zip"
    destDir = r"f:\temp"
    shutil.copy(srcFile,destDir)  
    
    
# in windows use "attrib" and in Linux use "chmod"
def file_metadata(file_name):
    # Get the status of a file or a file descriptor
    stat_info = os.stat(file_name)
    # st_mode :File mode: file type and file mode bits (permissions).
    mode = stat_info.st_mode
    print('  Mode (oct)   :', mode)
    import time
    # the time of creation on Windows
    print(f'\tCreated : {time.ctime(stat_info.st_ctime)}')
    # Time of most recent access expressed in seconds.
    print(f'\tAccessed: {time.ctime(stat_info.st_atime)}')
    # Time of most recent content modification expressed in seconds.
    print(f'\tModified: {time.ctime(stat_info.st_mtime)}')
    # The size of the file
    print(f'\tFileSize: {stat_info.st_size} bytes')

  
def copy_metadata():
    # Copy File with Metadata(as much as possible)
    # make an exact clone of the file, along with the 
    # permissions and the metadata of a file
    print('SOURCE FILE:')
    src_file = r"E:\IOT\Papers\research.pdf"
    dest_file = "e:/temp/code1.pdf"
    # Does not copy the metadata
    # shutil.copy(src_file, dest_file)
    shutil.copy2(src_file, dest_file)
    print('source FILE:')
    file_metadata(src_file)
    print('DESTINATION FILE:')
    file_metadata(dest_file)
 
def copy_directory():
    import glob
    import pprint
    import shutil
    # Replicate a directory tree recursively.
    srcDir  = r"d:/python/programs/pack"
    destDir = r"d:/python/programs/pack_copy1"
    
    print('BEFORE:')
    pprint.pprint(glob.glob(srcDir))

    shutil.copytree(srcDir,destDir)  
    # shutil.copytree('../shutil', '/tmp/example')

    print('\nAFTER:')
    pprint.pprint(glob.glob(destDir))
    
    
   
def move_file():
    srcFile = "d:/python/programs/registration.xlsx"
    destDir = "e:/Temp"
    # Moving File
    shutil.move(srcFile,destDir)   

    
def move_dir():
    srcDir = "d:/python/programs/pack_copy1"
    destDir = "e:/temp"
    # Moving Director
    shutil.move(srcDir,destDir)
 
def delete_dir():
    '''Deleting Directories'''
    dirToDelete = "e:/temp/pack_copy1"
    shutil.rmtree(dirToDelete)
   

# Finding files
def find_files():
    
    # tells the path to an executable application which 
    # would be run if the given cmd was called.
    # print(shutil.which('g++'))
    # print(shutil.which('venvlauncher'))
    # When no path is specified, the results of os.environ() are used
    # print(os.environ)   
    print(shutil.which('venvwlauncher',path='D:\Python\Programs'))
 
#Monitoring File-system Space
def filesys_space():
    print(shutil.disk_usage('.'))  # returns shutil.usage
    
    total_b, used_b, free_b = shutil.disk_usage('.')
    gb = 10 ** 9
    
    print('Total: {:6.2f} GB'.format(total_b / gb))
    print('Used : {:6.2f} GB'.format(used_b  / gb))
    print('Free : {:6.2f} GB'.format(free_b  / gb))


        
def delete_directory():
    import shutil
    # define the name of the directory to be deleted
    # path = r"E:\temp\year\month\week\day\hour\min\sec"
    path = "E:\\temp\\year\\month\\week"
    
    try:
        # os.rmdir(path)     #deletes single empty directory
        # os.removedirs(path)  #recursively deletes empty directory  
        shutil.rmtree(path) #recursively deletes directory  
    except OSError:
        print ("Deletion of the directory %s failed" % path)
    else:
        print ("Successfully deleted the directory %s" % path)
 


# Copy the permission bits from src to dst. 
# The file contents, owner, and group are unaffected. 
# shutil.copymode(src, dst, *, follow_symlinks=True)
# src and dst are path-like objects or path names given as strings.  
def copy_permisions1():       
    import os
    import shutil
    
    with open('file1.txt', 'wt') as f:
        f.write('content')
    os.chmod('file1.txt', 0o444)
    
    print('BEFORE:', oct(os.stat('file1.txt').st_mode))
    
    shutil.copymode('area.py', 'file1.txt')
    
    print('AFTER :', oct(os.stat('file1.txt').st_mode))
    
def show_file_info(filename):
    import os
    import shutil
    import time
    stat_info = os.stat(filename)
    print('  Mode    :', oct(stat_info.st_mode))
    print('  Created :', time.ctime(stat_info.st_ctime))
    print('  Accessed:', time.ctime(stat_info.st_atime))
    print('  Modified:', time.ctime(stat_info.st_mtime))    
    
# To copy other metadata about the file use copystat().
# Only the permissions and dates associated with the file are 
# duplicated with copystat()
# Copy the permission bits, last access time, last modification time, 
# and flags from src to dst. On Linux, copystat() also copies the 
# “extended attributes” where possible. The file contents, owner, and 
# group are unaffected. src and dst are path-like objects or path names 
# given as strings.

def copy_permisions2():    
    import os
    import shutil
    
    with open('file2.txt', 'wt') as f:
        f.write('content')
    os.chmod('file2.txt', 0o444)
    
    print('BEFORE:')
    show_file_info('file2.txt')
    
    shutil.copystat('zip.py', 'file2.txt')
    
    print('AFTER:')
    show_file_info('file2.txt')

if __name__ == '__main__':
    
    # os module
    # listfile_demo()
     listing_dir()
    # create_dir()
    # create_dirs()
    # file_metadata(r"E:\IOT\Papers\research.pdf")
    # delete_file()

    # shutil module
    # copyfile_demo()
    #copysymlink_demo()
    # copyfile_to_dir()
    # copy_metadata()
    # copy_directory()  
    # move_file()
    # move_dir()
   
    # delete_dir()
    # find_files()
    # delete_directory()
    # filesys_space()
    # copy_permisions1()
    # copy_permisions2()    