import sys
'''fobj = file("C:\Calculator\calculator\Functions\Sample.txt",'w')
fobj.write("hi this is first line in this file " )
fobj.write("i this is second line in this file ")
fobj.close()

fobj = file("C:\Calculator\calculator\Functions\Sample.txt",'r')
#print fobj.readline()
for line in fobj.readline():
        print len(line)

fobj.close()'''

import shutil
import os
path = "C:\Calculator\calculator"
#shutil.copy("Sample.txt","path.txt")
#shutil.move("path.txt","Sample.txt")
os.makedirs("dir1")