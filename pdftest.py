# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 22:22:12 2019

@author: Balaji.B.R
"""

import PyPDF2
import os
import sys, datetime
#import shutil

src = 'C:/Users/Balaji.B.R/Downloads/'
dst = 'C:/Users/Balaji.B.R/Downloads/success/'
op = 'C:/Users/Balaji.B.R/Desktop/op.txt'
#files = os.listdir(src)
#os.unlink(src)
sys.stdout = open(op,'w')
print("Date & Time :", datetime.datetime.now(), "\n")
files = os.listdir(src)
i=0
for f in files: 
    if (f.endswith('.pdf')):  
        #print("The File Name is",f)
        pdffileobj = open(src+f, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdffileobj)
        if pdfReader.isEncrypted:
            print("The File Name is",f)
            print("PDF is either protected or corrupted, kindly rescan \n")
            i+=1
        else: 
            # print(i)
            #shutil.move(src+f,dst+f)
            #print(i+1)
            # os.remove(src+f)
            i+=1
            #print("PDF is able to open")
            #   print("Number of pages:",pdfReader.numPages)
            pdffileobj.close()
    else:
        continue
else:
    print("Total PDF files scanned are:", i)
    sys.stdout.close()
