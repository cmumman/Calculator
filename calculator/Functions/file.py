import sys
'''fobj = file("C:\Calculator\calculator\Functions\Sample.txt",'w')
fobj.write("hi this is first line in this file " )
fobj.write("i this is second line in this file ")
fobj.close()

fobj = file("C:\Calculator\calculator\Functions\Sample.txt",'r')
#print fobj.readline()
for line in fobj.readline():
        print len(line)

fobj.close()

import shutil
import os
path = "C:\Calculator\calculator"
#shutil.copy("Sample.txt","path.txt")
#shutil.move("path.txt","Sample.txt")
os.makedirs("dir1")'''

import os,os.path
import re
a = os.getcwd()
print a
def print_pdf (arg, dir,files):
    for file in files:
      #  path = os.path.join(dir,file)
#        path = os.path.normcase(path)
        if re.search(r".*\.py",file):
            print file
os.path.walk('.', print_pdf,0)

