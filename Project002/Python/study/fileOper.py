#
# This file is created and completed at 2015/09/12 to study Python-language.
# It is mainly to operate on the file operations.
#

import random
import time
import sys
import math, cmath
import zipfile, os, stat
import pickle
import string

import locale
import re
import operator

import shutil
import time

def testMains():
    subMain001_openAndRWFile()

################################# #################################  #################################      
#################################          subMain001():
def subMain001_openAndRWFile():
    print(" ================================================================================ ") 
    print(" ===========  "+__file__) 
    for file in os.listdir("samples"):
        print(file)
    # where are we?
    cwd = os.getcwd()
    print("1", cwd)
    # go down
    os.chdir("samples")
    print("2", os.getcwd())
    # go back up
    os.chdir(os.pardir)
    print("3", os.getcwd())

    ################################# Testing the method of application of
    if not os.path.exists("NewTest/multiple/levels"):
        os.makedirs("NewTest/multiple/levels")
    fp = open("NewTest/multiple/levels/file", "w")
    fp.write("inspector praline")
    fp.close()
    # remove the file
    os.remove("NewTest/multiple/levels/file")
    # and all empty directories above it
    os.removedirs("NewTest/multiple/levels")
    ################################ high-level operation wiht the directories
    if not os.path.exists("Test2 - copy/lwt - copy/test/new/list"):
        os.makedirs("Test2 - copy/lwt - copy/test/new/list")
        os.mkdir("Test2 - copy/list1")
        os.mkdir("Test2 - copy/list2")
        os.mkdir("Test2 - copy/list3")
        os.mkdir("Test2 - copy/list4")
        os.mkdir("Test2 - copy/list4/sub1")
        os.mkdir("Test2 - copy/list4/sub2")
        os.mkdir("Test2 - copy/list4/sub3")
        os.mkdir("Test2 - copy/list4/sub4")
        os.mkdir("Test2 - copy/list4/sub4/sub01")
        os.mkdir("Test2 - copy/list4/sub4/sub01/sub0101")
        os.makedirs("Test2 - copy2/lwt - copy/test/new/list")
    os.removedirs("Test2 - copy2/lwt - copy/test/new/list")
    os.removedirs("Test2 - copy/list4/sub4/sub01/sub0101")
    shutil.rmtree("Test2 - copy")
    if not os.path.exists("NewTest/multiple/levels"):
        os.makedirs("NewTest/multiple/levels")
    fp = open("NewTest/multiple/levels/file", "w")
    fp.write("inspector praline")
    fp.close()
    ################################  File Analysis
    srcFileName = "poem.txt"
    dirRoot = "src/FileAnalysis/"
    timeStr = time.strftime('%Y%m%d_%H%M%S%m',time.localtime(time.time()))
    dstFileName = "poemExtractResult_" + timeStr + ".txt"
    if os.path.exists(dirRoot+srcFileName):
        fpR = open("src/FileAnalysis/poem.txt","r")
        readLineCurr = fpR.readline()
        print(readLineCurr)
        if not os.path.exists(dirRoot+dstFileName):
            fpW = open(dirRoot+dstFileName,"w")
            fpW.write("Extract result from src/FileAnalysis/poem.txt\n\n")
            fpW.write('%f\n\n' % time.time())          
            fpW.write('%s\n\n' % time.ctime())          
            #fpW.write(time.localtime())
            fpW.write(time.strftime( '%Y-%m-%d %H:%M:%S.%m', time.localtime() ))
            fpW.write("\n\n")
            fpW.write('%s\n\n' % readLineCurr)
            fpW.close()
        fopen = open(dirRoot+dstFileName,"a")
        allSrc = fpR.read()
        match = re.search(r'part00[0-9]', allSrc)
        print("\n\n ************************************************************************")
        print("\n\n ")
        print("match.string:"+match.string)
        print("match.re:")
        print(match.re)
        print("match.pos:%d" % (match.pos))
        print("match.endpos:%d" % (match.endpos))
        if match.lastindex != None:
            print("match.lastindex:%d" % (match.lastindex))
        #print("match.lastgroup:"+match.lastgroup)
        #print("match.group(1,2):"+match.group(1,2))
        #print("match.groupdict():"+match.groupdict())
        #print("match.start(2):"+match.start(2))
        #print("match.end(2):"+match.end(2))
        #print("match.span(2):"+match.span(2))
        #print(r"match.expand(r'\2 \1\3'):"+match.expand(r'\2 \1\3'))
        reResult = re.findall(r'part0[0-9][0-9]',allSrc)
        print('============================\nSearch Result:\n')
        print(reResult)
        for item in reResult:  
            fopen.write("%s\n" % item)
        reResult = re.findall(r'part0/d/d',allSrc)
        print('============================\nSearch Result:\n')
        print(reResult)
        for item in reResult:  
            fopen.write("%s\n" % item)
        fopen.close()
        fpR.close()
    print('============================\n\nRE Result:\n')
    s='ababab abbabb aabaab abab mmmmababmm mmmabab abababmm ababababb'
    result = re.findall( r'/b(?:ab)+/b', s )
    print(result)
    print('============================\n\nRE Result:\n')


