#
# This file is created and completed at 2014/10/04 as the first day to study Python-language.
# One day to finish the shallow-research-study Python inlcude the basic grammer and some 
# coding-works.
#
import turtle
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

import plotMod
import Fcn001
import mymodule
from mymodule import Person, Teacher, dump


def sub_mains():
    sub_main_001()
    sub_main_002()
    sub_main_003()
    sub_main_004()
    sub_main_005()
    sub_main_006()


# ################################ # ################################  # ################################
# ################################          sub_main_001():
def sub_main_001():
    print(" ================================================================================ ") 
    print(" ===========  "+__file__) 
    plotMod.pRectangle(nt, -10, -10, 60)
    plotMod.pCircle(10,10,300,100)
    plotMod.pSunLight(400)


# ################################ # ################################  # ################################
# ################################             sub_main_002():
def sub_main_002():
    print(" ========================================================================== ") 
    print('current file path is', __file__)
    print('current file name is', __name__)
    print('current doc is', __doc__)
    print(" --------------------------------- ") 
    # ################################ Testing the method of application of string output
    s = '''This is a multi-line string.
    This is the second line.'''
    print(s)
    s = 'This is a string. \
    This continues the string.'
    print(s)
    print('i = 10**10 = ', 10**10)
    i = 134
    j = 50
    k = i//j
    print(' i =',i,' j =',j,' k = i//j =',k)
    k = i%j
    print(' i =',i,' j =',j,' k = i%j =',k)
    # ################################ Testing the method of application of for-loop
    for i in(10,12,33,14,57):
        if ~i%2:
            print(i,'is an even number.')
        else:
            print(i,'is an odd number.')
    for i in range(0, 3):
        print(i)
    else:
        print('The for loop is over with outputting range(0,3)')
    for i in range(0, 300, 98):
        print(i)
    else:
        print('The for loop is over with outputting range(0, 300, 98)')
# #   # ################################ Testing the method of application of while-if
# #   number = 23
# #   guess = 10
# #   while(guess!=number):
# #      guess = int(input('Enter an integer to guess: '))
# #      if guess == number:
# #          print('Congratulations, you guessed it.') # New block starts here
# #          print("(but you do not win any prizes!)") # New block ends here
# #      elif guess < number:
# #          print('No, it is a little lower than that') # Another block
# #          # You can do whatever you want in a block ...
# #      else:
# #          print('No, it is a little higher than that')
# #          # you must have guess > number to reach here
# #   else:
# #      print('The while loop is over.')
# #      # Do anything else you want to do here
# #   print('Done')
# #   # ################################ Testing the method of application of break-clause
# #   while True:
# #      s = input('Enter something until with quit: ')
# #      if s == 'quit':
# #         break
# #      elif len(s) < 3:
# #         print('input string is too short to quit')
# #         continue
# #      print('Length of the string is', len(s))
# #   print('Done')
    # ################################ Testing the method of application of call-funtion
    sayHello()
    printMax(100,321)
    print('maximum(123,142) is',maximum(123,142))
    printMaxDoc(123,142)
    print(printMaxDoc.__doc__)
    help(printMaxDoc)
    help(printMax)
    # ################################ Testing the method of application of modules
    print('The command line arguments are:')
    for i in sys.argv:
        print(i)
    print('\n\nThe PYTHONPATH is', sys.path, '\n')
    mymodule.sayhi()
    print('mymodule.version is', mymodule.version)
    # Fcn001.main()    # the same behavior with the time import first time
    # print('Fcn001.version is',Fcn001.version)
    print('math.sqrt(10.2) =', math.sqrt(10.2))
    print()
    print('multiply(10,21) is',mymodule.multiply(10,21))
    print('divide(10,21) is',mymodule.divide(10,21))
    print()
    # ################################ Testing the method of application of intrinsic constant
    if __name__ == '__main__':
        print('This program is being run by itself')
    else:
        print('I am being imported from another module')
    # print(__path__)
    # print(__line__)
    print('current file path is', __file__)
    # ################################ Testing the method of application of dir() fcn.
    zzz = 99
    newInt = 100
    print('Show the attribute-list of current module as following:')
    print(dir())
    yy = 78
    newString = 'ABC'
    print('Show the attribute-list of current module as following:')
    print(dir())
    del yy
    print('Show the attribute-list of current module as following:')
    print(dir())
    print('Show the attribute-list of sys module as following:')
    #print(dir(sys))
    # ################################ Testing the method of application of list-data-stucture
    shoplist = ['apple', 'mango', 'carrot', 'banana']
    print('I have', len(shoplist),'items to purchase.')
    print('These items are:') # Notice the comma at end of the line
    print('All the items :')
    for item in shoplist:
        print(item, ' ', ' ', sep='->', end='')
    else:
        print()
    shoplist.append('added001')
    shoplist.append('added002')
    shoplist.append('added001')
    shoplist.append(123123)
    shoplist.append(0.003782)
    sublist = [12,32.132,'ABC',"zyx",31,1323.1231]
    shoplist.append(sublist)
    print('All the items :')
    for item in shoplist:
        print(item, ' ', ' ', sep='->', end='')
    else:
        print()
    print('Output the shoplist : ', shoplist)
    # ################################ Testing the method of application of tuple (diffrent from list)
    zoo = ('wolf', 'elephant', 'penguin')
    print('Number of animals in the zoo is', len(zoo))
    new_zoo = ('monkey', 'dolphin', zoo)
    print('Number of animals in the new zoo is', len(new_zoo))
    print('All animals in new zoo are', new_zoo)
    print('Animals brought from old zoo are', new_zoo[2])
    print('Last animal brought from old zoo is', new_zoo[2][2])
    age = 22
    name = 'Swaroop'
    print('%s is %d years old' % (name, age))    # tuple mostly are used in print-clause
    print('Why is %s playing with that python?' % name)
    # ################################ Testing the method of application of key-value pair i.e. dictionary data structure
    ab = {   'Swaroop'   : 'swaroopch@byteofpython.info',
                'Larry'     : 'larry@wall.org',
                'Matsumoto' : 'matz@ruby-lang.org',
                'Spammer'   : 'spammer@hotmail.com'
        }
    print()
    print("Swaroop's address is %s" % ab['Swaroop'])
    # Adding a key/value pair
    ab['Guido'] = 'guido@python.org'
    # Deleting a key/value pair
    del ab['Spammer']
    print('\nThere are %d contacts in the address-book : \n' % len(ab))
    for name, address in ab.items():
        print('Contact %s at %s' % (name, address))
    if 'Guido' in ab: # OR ab.has_key('Guido')
        print("\nGuido's address is %s" % ab['Guido'])
    # ################################ Testing the method of application of sequence
    shoplist = ['apple', 'mango', 'carrot', 'banana']
    # Indexing or 'Subscription' operation
    print('Item 0 is', shoplist[0])
    print('Item 1 is', shoplist[1])
    print('Item 2 is', shoplist[2])
    print('Item 3 is', shoplist[3])
    print('Item -1 is', shoplist[-1])
    print('Item -2 is', shoplist[-2])
    print('Item -3 is', shoplist[-3])
    print('Item -4 is', shoplist[-4])
    # Slicing on a list
    print('Item 1 to 3 is', shoplist[1:3])
    print('Item 2 to end is', shoplist[2:])
    print('Item 1 to -1 is', shoplist[1:-1])
    print('Item start to end is', shoplist[:])
    # Slicing on a string
    name = 'ABCDefghijk'
    print('characters 1 to 3 in string \'swaroop\' is', name[1:3])
    print('characters 2 to end in string \'swaroop\' is', name[2:])
    print('characters 1 to -1 in string \'swaroop\' is', name[1:-1])
    print('characters start to end in string \'swaroop\' is', name[:])
    # ################################ Testing the method of application of reference and copy(i.e. ref and copy)
    print('Simple Assignment')
    shoplist = ['apple', 'mango', 'carrot', 'banana']
    mylist = shoplist # mylist is just another name pointing to the same object!
    del shoplist[0]
    print('shoplist is', shoplist)
    print('mylist is', mylist)
    # notice that both shoplist and mylist both print(the same list without
    # the 'apple' confirming that they point to the same object
    print('Copy by making a full slice')
    mylist = shoplist[:] # make a copy by doing a full slice
    del mylist[0] # remove first item
    print('shoplist is', shoplist)
    print('mylist is', mylist)
    # ################################ Testing the method of application of string (deeper study especially the fucntions)
    name = 'Swaroop' # This is a string object 
    if name.startswith('Swa'):
        print('Yes, the string starts with "Swa"')
    if 'a' in name:
        print('Yes, it contains the string "a"')
    if name.find('war') != -1:
        print('Yes, it contains the string "war"')
    delimiter = '_*_'
    mylist = ['Brazil', 'Russia', 'India', 'China']
    print(delimiter.join(mylist))
    delimiter = ' '
    mylistStr = delimiter.join(mylist)
    mylist2 = mylistStr.split(' ')
    print(mylist2)
    str = ('www...google.com')
    print(str)
    str_split = str.split('.',500)  # To split the primt stirng 2 times, i.e. create two sub-segment
    print(str_split)
    print('    --  A B C-de F  --                    '.strip(), 'End')
    # remove the blank spacing at the both ends of stirng, for more(lstrip,rstrip)
    # To remove the empty value of a sequence
   
    # ################################ Testing the method of application of TO BACKUP FILE OPER
    # 1. The files and directories to be backed up are specified in a list.
    source = [r'E:\Application\_SourceCodes\Python3p4p1\Test\file1\OK.txt', \
                r'E:\Application\_SourceCodes\Python3p4p1\Test\file2']
    # If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that

    # 2. The backup must be stored in a main backup directory
    target_dir = r'E:\Application\_SourceCodes\Python3p4p1\Test2' # Remember to change this to what you will be using

    # 3. The files are backed up into a zip file.
    # 4. The name of the zip archive is the current date and time
    target = target_dir + time.strftime(r'\%Y%m%d%H%M%S') + '.zip'
    print('source file 1 is :', source[0])
    print('source file 2 is :', source[1])
    print('target file is :', target)
    #tar = 'tar -cvzf %s %s -X /home/swaroop/excludes.txt' % (target, ' '.join(srcdir))

    # 3. The files are backed up into a zip file.
    # 4. The current day is the name of the subdirectory in the main directory
    today = target_dir + time.strftime(r'\%Y%m%d')
    # The current time is the name of the zip archive
    now = time.strftime('%H%M%S')
    # Create the subdirectory if it isn't already there
    if not os.path.exists(today):
        os.mkdir(today) # make directory
        print('Successfully created directory', today)
    
    # 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
    zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
    print('zip_command is', zip_command)
    # Run the backup
    if os.system(zip_command) == 0:
        print('Successful backup to', target)
    else:
        print('Backup FAILED')
    # ################################ Testing the method of application of zipfile-class to (un)empress files or dictionary
    zipFile = zipfile.ZipFile(r'E:\Application\_SourceCodes\Python3p4p1\Test\result.zip', 'w')
    zipFile.write(r'E:\Application\_SourceCodes\Python3p4p1\Test\file1\Prime001.txt', 'Prime001.txt', zipfile.ZIP_DEFLATED)
    zipFile.close()
    zipFile = zipfile.ZipFile(r'E:\Application\_SourceCodes\Python3p4p1\Test\result.zip', 'a')
    zipFile.write(r'E:\Application\_SourceCodes\Python3p4p1\Test\file1\Prime002.txt', 'Prime002.txt', zipfile.ZIP_DEFLATED)  
    zipFile.close()
    # ################################ Testing the method of application of class
    YY = Person('YY')
    print(YY)
    YY.sayHi()
    TT = Person('TT')
    print(TT)
    TT.showInfo()
    YY2 = Teacher('yy2', 20, 2E3)
    YY2.sayHi()
    YY2.tell()
    del(YY)
    del(TT)
    del(YY2)
    # ################################ Testing the method of application of iostream/IO - file Ope
    poem = '''\
    Programming is fun
    When the work is done
    if you wanna make your work also fun:
            use Python!
    '''
    try:
        f = open(r'E:\Application\_SourceCodes\Python3p4p1\Test\poem.txt', 'w') # open for 'w'riting
    except IOError:
        print("The file don't exist, Please double check!")
        exit()
    f = open(r'E:\Application\_SourceCodes\Python3p4p1\Test\poem.txt', 'w') # open for 'w'riting
    f.write(poem) # write text to file
    f.close() # close the file
    f = open(r'E:\Application\_SourceCodes\Python3p4p1\Test\poem.txt') # if no mode is specified, 'r'ead mode is assumed by default
    while True:
        line = f.readline()
        if len(line) == 0: # Zero length indicates EOF
            break
        print(line,)
        # Notice comma to avoid automatic newline added by Python
    f.close() # close the file
    # ################################ Testing the method of application of cPickle
    shoplistfile = 'shoplist.data'
    # the name of the file where we will store the object
    shoplist = ['Walking', 'down', 'the', 'same', 'old', 'street']
    # Write to the file
    f = open(shoplistfile, 'wb') #must be opened by '-b' method
    pickle.dump(shoplist, f) # dump the object to a file
    f.close()
    del shoplist # remove the shoplist
    # Read back from the storage
    f = open(shoplistfile, 'rb') #must be opened by '-b' method
    storedlist = pickle.load(f)
    print(storedlist)
    # ################################ Testing the method of application of expection
    class ShortInputException(Exception):
        '''A user-defined exception class.'''
        def __init__(self, length, atleast):
            Exception.__init__(self)
            self.length = length
            self.atleast = atleast
    try:
        #s = input('Enter something --> ')
        s = 'AB'
        if len(s) < 3:
            raise ShortInputException(len(s), 3)
        # Other work can continue as usual here
    except EOFError:
        print('\nWhy did you do an EOF on me?')
    except ShortInputException as x:
        print('ShortInputException: The input was of length %d, \
                was expecting at least %d' % (x.length, x.atleast))
    else:
        print('No exception was raised.')
    try:
        f = open(r'E:\Application\_SourceCodes\Python3p4p1\Test\MyPoem.txt')
        while True: # our usual file-reading idiom
            line = f.readline()
            if len(line) == 0:
                break
            #time.sleep(0.2)
            print(line,)
    finally:
        f.close()
        print('Cleaning up...closed the file')
    # ################################ Testing the method of application of sys-module
    print('sys.argv are', sys.argv)
    print('sys.version is', sys.version)
    print('sys.version_info is', sys.version_info)
    # ################################ Testing the method of application of os-module
    print()
    print('os.name is:', os.name)
    print()
    print('os.getcwd() is:', os.getcwd())
    print()
    print("os.getenv('path') is:", os.getenv('path'))
    print()
    print('os.listdir() is:', os.listdir())
    # ################################ Testing the method of application of list-synthesization
    listone = [2, 3, 4, 1, 7, 0, 8, 5, 6]
    listtwo = [2*i for i in listone if i > 3]
    listthree = [i**i**i for i in listone if i>0 and i<4]
    print(listtwo)
    print(listthree)
    # ################################ Testing the method of application of  Variadic function
    print('powersum(2,3,4) is',powersum(2,3,4))
    print('powersum(10,2) is',powersum(10,2))
    print('powersum(20,2) is',powersum(20,2))
    print('powersum(2,20) is',powersum(2,20))
    # ################################ Testing the method of application of lambda
    twice = make_repeater(2)
    print(twice('world'))
    print("'world'*2 is:",'world'*2)
    print(twice(2))
    # ################################ Testing the method of application of exec-eval
    exec('print("this clause is in exec fcn.")')
    print(eval('2**4**2'))
    # ################################ Testing the method of application of Assert
    mylist = ['item']
    assert len(mylist) >= 1
    mylist.pop()
    assert len(mylist) == 0
    # ################################ Testing the method of application of cMath(complex number)
    a = 8+9j
    b = 3132.99-42.3423j
    print('a is:',a)
    print('b is:',b)
    print('a+b is:',a+b)
    print('a-b is:',a-b)
    print('a*b is:',a*b)
    print('a/b is:',a/b)
    print('a**5 is:',a**5)
    # ################################ Testing the method of application of
    dump(0)
    dump(1.0)
    dump(0.0j) # complex number
    dump(()) # tuple
    dump([]) # list
    dump({}) # dictionary
    dump("string") # str
    dump(len) # function
    dump(sys) # module
    print('\nall members of class Person are: \n', mymodule.getmembers(Person))
    print('\nall members of class IOError are: \n', mymodule.getmembers(IOError))
    # ################################ Testing the method of application of dir()-function
    book = "library"
    pages = 250
    scripts = 350
    print("the %(book)s book contains more than %(scripts)s scripts" % vars())
    print("the %(book)s book contains more than %(scripts)s scripts")


# ################################ # ################################  # ################################
# ################################             sub_main_003():      current test funcion
def sub_main_003():
    # ################################ Testing the method of application of isinstance()-callable() functions
    print(len(mymodule.load("samples/sample.jpg")), "bytes")
    print(len(mymodule.load("Fcn001.py")), "bytes")
    mymodule.dumpCallable(Person)
    p = Person("me")
    mymodule.dumpCallable(p)
    del p
    mymodule.dumpCallable(str)
    mymodule.dumpCallable(Person.tell)
    mymodule.dumpCallable(mymodule.dumpCallable)
    mymodule.dumpCallable(dump)
    mymodule.dumpCallable(complex)
    i = 3
    if isinstance(i,int):
        print(i, "=>",type(1))
    else:
        print(i ,'is not', type(1))


# ################################ # ################################  # ################################
# ################################             sub_main_004():            current test funcion
def sub_main_004():
    # ################################ Testing the method of application of  eval() function
    print(" ================================================================================ ") 
    dump004('str')
    dump004('int')
    dump004('8j')
    dump004('0')
    dump004("1")
    dump004("1.0")
    dump004("'string'")
    dump004("1.0 + 2.0")
    dump004("'*' * 10")
    dump004("len('world')")
    BODY = """
    \nprint('the ant, an introduction')
    \nprint('the second line')
    \nfor i in range(4):
    \n\tprint(i)
    """
    code = compile(BODY, "<script>", "exec")
    print(code)
    exec(code)
    # ################################ Testing the method of application of Code generator
    #
    # try it out!
    c = CodeGeneratorBackend()
    c.begin()
    c.write("for i in range(3):")
    c.indent()
    c.write("print('current code line %(i)d :code generation made easy!' % vars())")
    c.dedent()
    exec(c.end())
    # ################################ Testing the method of application of test self-define exception
    #try:
    #    #raise HTTPError("http://www.python.org/foo", 200, "Not Found")
    #except error as HTTPError:
    #    print("url", "=>", error.url)
    #    print("errcode", "=>", error.errcode)
    #    print("errmsg", "=>", error.errmsg)
    #    raise # reraise exception
    # ################################ Testing the method of application of Start new process
    #program = "python"
    #arguments = [r"E:\Application\_SourceCodes\PythonCode\PythonApplication1\PythonApplication1\Fcn001.py"]
    #print(os.execvp(program, (program,) +  tuple(arguments)))
    # ################################ Testing the method of application of string
    a = string.Formatter
    print(a)
    # ################################ Testing the method of application of str.replace() function
    file = "Test/file2/poem.txt"
    replaceFileWord(file, "teh", "the")
    replaceFileWord(file, "U", "you")
    pass


# ################################ # ################################  # ################################
# ################################ current test funcion assist-functions
class HTTPError(Exception):
    # indicates an HTTP protocol error
    def __init__(self, url, errcode, errmsg):
        self.url = url
        self.errcode = errcode
        self.errmsg = errmsg

    def __str__(self):
        return (
            "<HTTPError for %s: %s %s>" %
            (self.url, self.errcode, self.errmsg)
        )


def dump004(expression):
    result = eval(expression)
    print(expression, "=>", result, type(result))


def replaceFileWord(file, search_for, replace_with):
    # replace strings in a text file
    back = os.path.splitext(file)[0] + ".bak"
    temp = os.path.splitext(file)[0] + ".tmp"
    try:
        # remove old temp file, if any
        os.remove(temp)
    except os.error:
        pass
    fi = open(file)
    fo = open(temp, "w")
    for s in fi.readlines():
        fo.write(str.replace(s, search_for, replace_with))
    fi.close()
    fo.close()
    try:
        # remove old backup file, if any
        os.remove(back)
    except os.error:
        pass
    # rename original to backup...
    os.rename(file, back)
    # ...and temporary to original
    os.rename(temp, file)


# ################################ # ################################  # ################################      os-module test
# ################################             sub_main_005():       �ļ������й�    current test funcion
def sub_main_005():
    # ################################ Testing the method of application of
    print(" ================================================================================ ") 
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
    # ################################ Testing the method of application of
    if not os.path.exists("NewTest/multiple/levels"):
        os.makedirs("NewTest/multiple/levels")
    fp = open("NewTest/multiple/levels/file", "w")
    fp.write("inspector praline")
    fp.close()
    # remove the file
    os.remove("NewTest/multiple/levels/file")
    # and all empty directories above it
    os.removedirs("NewTest/multiple/levels")
    # ################################ Testing the method of application of
    os.mkdir("test293487")
    os.rmdir("test293487")
    try:
        os.rmdir("samples") # this will fail for remove-dirctory is not empty MAYBE you can delete a root-dir by using rmtree()
    except os.error:
        pass
    # ################################ Testing the method of application of
    file = "samples/images/Image (1).jpg"
    #
    # get stats for a filename
    st = os.stat(file)
    print("stat", file)
    dump005(st)
    print()
    #
    # get stats for an open file
    fp = open(file)
    st = os.fstat(fp.fileno())
    print("fstat", file)
    dump005(st)
    # ################################ Testing the method of application of
    if os.name == "nt":
        command = "dir"
    else:
        command = "ls -l"
    print(command,'command')
    os.system(command)

    #program = "python"
    #arguments = ["Fcn001.py"]
    #print(os.execvp(program, (program,) +  tuple(arguments)))
    #for i in range(1000):
    #    print("goodbye")

    #run005("python", r"E:\Application\_SourceCodes\PythonCode\PythonApplication1\PythonApplication1\Fcn001.py")
    #print("goodbye")
    #runBack005("python", r"E:\Application\_SourceCodes\PythonCode\PythonApplication1\PythonApplication1\Fcn001.py", mode=os.P_NOWAIT)
    #print("goodbye")

    #try:
    #    sys.exit(1)
    #except value as SystemExit:
    #    print("caught exit(%s)" % value)
    #try:
    #    os._exit(2)
    #except value as SystemExit:
    #    print("caught exit(%s)" % value)
    #print("bye!")

    filename = r"\samples\file2\poem.txt"
    print("using", os.name, "...")
    print("split", "=>", os.path.split(filename))
    print("splitext", "=>", os.path.splitext(filename))
    print("dirname", "=>", os.path.dirname(filename))
    print("basename", "=>", os.path.basename(filename))
    print("join", "=>", os.path.join(os.path.dirname(filename),
                                     os.path.basename(filename)))
    filename = r"\samples\sub1\subend"
    print("using", os.name, "...")
    print("split", "=>", os.path.split(filename))
    print("splitext", "=>", os.path.splitext(filename))
    print("dirname", "=>", os.path.dirname(filename))
    print("basename", "=>", os.path.basename(filename))
    print("join", "=>", os.path.join(os.path.dirname(filename),
                                     os.path.basename(filename)))

    FILES = (
    os.curdir,
    "/",
    "file",
    "/file",
    "samples",
    "samples/sample.jpg",
    "directory/file",
    "../directory/file",
    r"E:\Application\_SourceCodes\PythonCode\PythonApplication1\PythonApplication1\samples\images",
    "/directory/file",
    "samples/file1",
    "samples/images",
    "samples/images/Image (1).jpg",
    "http://www.python.org/foo"
    )
    for file in FILES:
        print(file, "=>",)
        if os.path.exists(file):
            print("EXISTS",)
        else:
            print('NOT EXIST')
        if os.path.isabs(file):
            print("ISABS",)
        if os.path.isdir(file):
            print("ISDIR",)
        if os.path.isfile(file):
            print("ISFILE",)
        if os.path.islink(file):
            print("ISLINK",)
        if os.path.ismount(file):
            print("ISMOUNT",)
        print()

    print()
    print()
    for root, dirs, files in os.walk(r'E:\Application\_SourceCodes\PythonCode\PythonApplication1\PythonApplication1\samples'):
        print(root, "consumes", end=" ")
        print(sum( os.path.getsize( os.path.join(root, name)) for name in files), end=" ")
        print("bytes in", len(files), "non-directory files")
        if 'CVS' in dirs:
            dirs.remove('CVS')  # don't visit CVS directories
    
    print()
    print()
    for file in index("."):
        print(file)

    for file in DirectoryWalker("."):
        print(file)

    for file, st in DirectoryStatWalker("."):
        print(file, st[stat.ST_SIZE])
    # ################################ Testing the method of application of
    pass


# ################################ # ################################  # ################################
# ################################ current test funcion assist-functions
def dump005(st):
    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
    print("- size:", size, "bytes")
    print("- owner:", uid, gid)
    print("- created:", time.ctime(ctime))
    print("- last accessed:", time.ctime(atime))
    print("- last modified:", time.ctime(mtime))
    print("- mode:", oct(mode))
    print("- inode/dev:", ino, dev)


def run005(program, *args):
    # find executable
    for path in str.split(os.environ["PATH"], os.pathsep):
        file = os.path.join(path, program) + ".exe"
        try:
            return os.spawnv(os.P_WAIT, file, (file,) + args)
        except os.error:
            pass
    raise (os.error, "cannot find executable")


def runBack005(program, *args, **kw):
    # find executable
    mode = kw.get("mode", os.P_WAIT)
    for path in str.split(os.environ["PATH"], os.pathsep):
        file = os.path.join(path, program) + ".exe"
        try:
            return os.spawnv(mode, file, (file,) + args)
        except os.error:
            pass
    raise (os.error, "cannot find executable")


def spawn(program, *args):
    try:
        # possible 2.0 shortcut!
        return os.spawnvp(program, (program,) + args)
    except AttributeError:
        pass
    try:
        spawnv = os.spawnv
    except AttributeError:

        # assume it's unix
        pid = os.fork()
        if not pid:
            os.execvp(program, (program,) + args)
        return os.wait()[0]
    else:
        # got spawnv but no spawnp: go look for an executable
        for path in str.split(os.environ["PATH"], os.pathsep):
            file = os.path.join(path, program) + exefile
            try:
                return spawnv(os.P_WAIT, file, (file,) + args)
            except os.error:
                pass
        raise (IOError, "cannot find executable")


def callback005(arg, directory, files):
    for file in files:
        print(os.path.join(directory, file), repr(arg))


def index(directory):
    # like os.listdir, but traverses directory trees
    stack = [directory]
    files = []
    while stack:
        directory = stack.pop()
        for file in os.listdir(directory):
            fullname = os.path.join(directory, file)
            files.append(fullname)
            if os.path.isdir(fullname) and not os.path.islink(fullname):
                stack.append(fullname)
    return files



# ################################ # ################################  # ################################
# ################################             sub_main_006():      current test funcion
def sub_main_006():
    # ################################ Testing the method of application of str-string
    print(" ================================================================================ ") 
    text = "Monty Python's Flying Circus"
    print("upper", "=>", str.upper(text))
    print("lower", "=>", str.lower(text))
    print("split", "=>", str.split(text))
    print("join", "=>", str.join('+',str.split(text))) ### !!! join the first para to each middle of both second para.
    print("replace", "=>", str.replace(text, "Python", "Java"))
    print("find", "=>", str.find(text, "Python"), str.find(text, "Java"))
    print("count", "=>", str.count(text, "n"))

    print("upper", "=>", text.upper())
    print("lower", "=>", text.lower())
    print("split", "=>", text.split())
    print("join", "=>", "+".join(text.split()))
    print("replace", "=>", text.replace("Python", "Perl"))
    print("find", "=>", text.find("Python"), text.find("Perl"))
    print("count", "=>", text.count("n"))


    print(int("4711"))
    print(float("4711"),)
    print(locale.atof("1"),)
    print(locale.atof("1.23e5"))
    print(locale.atoi("4711"))
    print(locale.atoi("04711"))
    #print(locale.atoi("0x4711"))
    #print(str.atoi("11147", 8),) # octal ???????
    #print(locale.atoi("1267", 16),) # hexadecimal ?????��??????
    #print(locale.atoi("3mv", 36)) # whatever...
    #print(locale.atoi("4711", 0),)
    #print(locale.atoi("04711", 0),)
    #print(locale.atoi("0x4711", 0))
    
    # ################################ Testing the method of application of re-module
    text = "The Attila the Hun Show"
    # a single character ??????????��?��?
    m = re.match(".", text)
    if m: 
        print(repr("."), "=>", repr(m.group(0)))

    # any string of characters ??????????��?��???
    m = re.match(".*", text)
    if m: 
        print(repr(".*"), "=>", repr(m.group(0)))

    # a string of letters (at least one) ??????��?????????????????��?��???(????????)
    m = re.match("\w+", text)
    if m: 
        print(repr("\w+"), "=>", repr(m.group(0)))

    # a string of digits ??????��?????????????????��?��???
    m = re.match("\d+", text)
    if m: 
        print(repr("\d+"), "=>", repr(m.group(0)))

    text ="10/15/99"
    m = re.match("(\d{2})/(\d{2})/(\d{2,4})", text)
    if m:
        print(m.group(1, 2, 3))
    text ="10/15/998"
    m = re.match("(\d{2})/(\d{2})/(\d{2,4})", text)
    if m:
        print(m.group(1, 2, 3))
    text ="10/15/96659/1234567/12345"
    m = re.match("(\d{2})/(\d{2})/(\d{2,5})/(\d{2,8})/(\d{3,6})", text)
    if m:
        print(m.group(1, 2, 3, 4, 5))

    text = "Example 3: There is 1 date 10/25/95 in here! another type 9/12/2014"
    m = re.search("(\d{1,2})/(\d{1,2})/(\d{2,4})", text)
    if m:
        print(m.group(1), m.group(2), m.group(3))
        month, day, year = m.group(1, 2, 3)
        print(month, day, year)
        date = m.group(0)
        print(date)
    m = re.search("(\d{1,2})/(\d{1,2})/(\d{4})", text)
    if m:
        print(m.group(1), m.group(2), m.group(3))
        month, day, year = m.group(1, 2, 3)
        print(month, day, year)
        date = m.group(0)
        print(date)

    text = "you're no fun anymore..."
    # literal replace (string.replace is faster)
    # ????????? (string.replace ???????��?????��??)
    print(re.sub("fun", "entertaining", text))
    # collapse all non-letter sequences to a single dash 
    # ?????��???????��?��?????????��????????????????"-"(dansh,??????)
    print(re.sub("[^\w]+", "-", text))
    # convert all words to beeps 
    # ?????��?????????????? BEEP
    print(re.sub("\S+", "-BEEP-", text))

    patterns = [
        r"\d+",
        r"abc\d{2,4}",
        r"p\w+"
    ]
    p = combined_pattern(patterns)
    print(p("129391"))
    print(p("abc800"))
    print(p("abc1600"))
    print(p("python"))
    print(p("perl"))
    print(p("tcl"))
    # ################################ Testing the method of application of math-cmath
    print("e", "=>", math.e)
    print("pi", "=>", math.pi)
    print("hypot", "=>", math.hypot(3.0, 4.0))
    print("pi", "=>", cmath.pi)
    print("sqrt(-1)", "=>", cmath.sqrt(-1))
    # ################################ Testing the method of application of operator
    sequence = 1, 2, 4
    #print("add", "=>", reduce(operator.add, sequence))
    #print("sub", "=>", reduce(operator.sub, sequence))
    #print("mul", "=>", reduce(operator.mul, sequence))
    print("concat", "=>", operator.concat("spam", "egg"))
    #print("repeat", "=>", operator.repeat("spam", 5))
    print("getitem", "=>", operator.getitem(sequence, 2))
    print("indexOf", "=>", operator.indexOf(sequence, 2))
    #print("sequenceIncludes", "=>", operator.sequenceIncludes(sequence, 3))
    #print("sequenceIncludes", "=>", operator.sequenceIncludes(sequence, 4))
         
    dump006(0)
    dump006("string")
    dump006("string"[0])
    dump006([1, 2, 3])
    dump006((1, 2, 3))
    dump006({"a": 1})
    dump006(len) # function ????
    #dump006(UserList) # module ?????��??
    #dump006(UserList.UserList) # class ???��???��?��
    #dump006(UserList.UserList()) # instance ????

    # ################################ Testing the method of application of redirct the output
    # redirect standard output (including the print(statement)
    # ??????��????��???????��?????????(????��??????��?print????)
    old_stdout = sys.stdout
    sys.stdout = Redirect(sys.stdout)
    print("HEJA SVERIGE")
    print(r"FRISKT HUM\303\226R")
    # restore standard output
    # ????????��?????????
    sys.stdout = old_stdout
    print(r"M\303\205\303\205\303\205\303\205L!")
    # ################################ Testing the method of application of exit()
    sys.exitfunc = exitfunc
    try:
        sys.exit(1)
    except SystemExit:
        pass
    # ################################ Testing the method of application of time
    now = time.time()

    print(now, "seconds since", time.gmtime(0)[:6])
    print()
    print("or in other words:")
    print("- local time:", time.localtime(now))
    print("- utc:", time.gmtime(now))

    now = time.localtime(time.time())

    print(time.asctime(now))
    print(time.strftime("%y/%m/%d %H:%M", now))
    print(time.strftime("%a %b %d", now))
    print(time.strftime("%c", now))
    print(time.strftime("%I %p", now))
    #print(time.strftime("%Y-%m-%d %H:%M:%S %Z", now))

    # do it by hand...
    year, month, day, hour, minute, second, weekday, yearday, daylight = now
    print("%04d-%02d-%02d" % (year, month, day))
    print("%02d:%02d:%02d" % (hour, minute, second))
    print(("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")[weekday], yearday)

    # make sure we have a strptime function!
    # ????��?��???????? strptime
    try:
        strptime = time.strptime
    except AttributeError:
        from strptime import strptime
    #print(strptime("31 Nov 00", "%d %b %y")) # ?????????��?????????????
    #print(strptime("1 Jan 70 1:30pm", "%d %b %y %I:%M%p"))

    print(strptime("2000-12-20 01:02:03", "%Y-%m-%d %H:%M:%S"))
    print(strptime(time.ctime(time.time())))


    t0 = time.time()
    tm = time.localtime(t0)
    print(tm)
    print(t0)
    print(time.mktime(tm))
    # ################################ Testing the method of application of
    pass


# ################################ # ################################  # ################################
# ################################ current test funcion assist-functions
def combined_pattern(patterns):
    p = re.compile(
        str.join("|", map(lambda x: "("+x+")", patterns))
        )
    def fixup(v, m=p.match, r=range(0,len(patterns))):
        try:
            regs = m(v).regs
        except AttributeError:
            return None # no match, so m.regs will fail
        else:
            for i in r:
                if regs[i+1] != (-1, -1):
                    return i
    return fixup


def dump006(data):
    print(type(data), "=>", data)
    #if operator.isCallable(data):
    #    print("CALLABLE",)
    #if operator.isMappingType(data):
    #    print("MAPPING",)
    #if operator.isNumberType(data):
    #    print("NUMBER",)
    #if operator.isSequenceType(data):
    #    print("SEQUENCE",)
    print()


class Redirect:
    def __init__(self, stdout):
        self.stdout = stdout
    def write(self, s):
        self.stdout.write(str.lower(s))


def exitfunc():
    print("game is over, you can deal something imoportant here before exit.")

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
          "Sep", "Oct", "Nov", "Dec"]
SPEC = {
    # map formatting code to a regular expression fragment
    "%a": "(?P<weekday>[a-z]+)",
    "%A": "(?P<weekday>[a-z]+)",
    "%b": "(?P<month>[a-z]+)",
    "%B": "(?P<month>[a-z]+)",
    "%C": "(?P<century>\d\d?)",
    "%d": "(?P<day>\d\d?)",
    "%D": "(?P<month>\d\d?)/(?P<day>\d\d?)/(?P<year>\d\d)",
    "%e": "(?P<day>\d\d?)",
    "%h": "(?P<month>[a-z]+)",
    "%H": "(?P<hour>\d\d?)",
    "%I": "(?P<hour12>\d\d?)",
    "%j": "(?P<yearday>\d\d?\d?)",
    "%m": "(?P<month>\d\d?)",
    "%M": "(?P<minute>\d\d?)",
    "%p": "(?P<ampm12>am|pm)",
    "%R": "(?P<hour>\d\d?):(?P<minute>\d\d?)",
    "%S": "(?P<second>\d\d?)",
    "%T": "(?P<hour>\d\d?):(?P<minute>\d\d?):(?P<second>\d\d?)",
    "%U": "(?P<week>\d\d)",
    "%w": "(?P<weekday>\d)",
    "%W": "(?P<weekday>\d\d)",
    "%y": "(?P<year>\d\d)",
    "%Y": "(?P<year>\d\d\d\d)",
    "%%": "%"
}
class TimeParser:
    def __init__(self, format):
        # convert strptime format string to regular expression
        format = str.join(re.split("(?:\s|%t|%n)+", format))
        pattern = []
        try:
            for spec in re.findall("%\w|%%|.", format):
                if spec[0] == "%":
                    spec = SPEC[spec]
                pattern.append(spec)
        except KeyError:
            #raise ValueError, "unknown specificer: %s" % spec
            raise ValueError
        self.pattern = re.compile("(?i)" + str.join("", pattern))
    def match(self, daytime):
        # match time string
        match = self.pattern.match(daytime)
        if not match:
            #raise ValueError, "format mismatch"
            raise ValueError
        get = match.groupdict().get
        tm = [0] * 9
        # extract date elements
        y = get("year")
        if y:
            y = int(y)
            if y < 68:
                y = 2000 + y
            elif y < 100:
                y = 1900 + y
            tm[0] = y
        m = get("month")
        if m:
            if m in MONTHS:
                m = MONTHS.index(m) + 1
            tm[1] = int(m)
        d = get("day")
        if d: tm[2] = int(d)
        # extract time elements
        h = get("hour")
        if h:
            tm[3] = int(h)
        else:
            h = get("hour12")
            if h:
                h = int(h)
                if string.lower(get("ampm12", "")) == "pm":
                    h = h + 12
                tm[3] = h
        m = get("minute")
        if m: tm[4] = int(m)
        s = get("second")
        if s: tm[5] = int(s)
        # ignore weekday/yearday for now
        return tuple(tm)
def strptime(string, format="%a %b %d %H:%M:%S %Y"):
    return TimeParser(format).match(string)



# ################################ # ################################ # ################################
# ################################ Global function defination
# ################################ # ################################ # ################################
         
def sayHello():
    print('Hello World!') # block belonging to the function


def printMax(a, b):
    '''Prints the maximum of two integer numbers.

    The two values must be integers.
    So you'd better use two integers as the parameter of this function.'''
    if a > b:
        print(a, 'is maximum')
    else:
        print(b, 'is maximum')


def printMaxDoc(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.
    So you'd better use two integers as the parameter of this function.'''
    x = int(x) # convert to integers, if possible
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')


def maximum(x, y):
    if x > y:
        return x
    else:
        return y


def powersum(power, *args):
    '''Return the sum of each argument raised to specified power.'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total


def make_repeater(n):
    return lambda s: s*n

# ################################ # ################################ # ################################
# ################################ class defination
# ################################ # ################################ # ################################
     
class CodeGeneratorBackend:
    "Simple code generator for Python"

    def begin(self, tab="\t"):
        self.code = []
        self.tab = tab
        self.level = 0
        self.script = ''
    def end(self):
        self.code.append("") # make sure there's a newline at the end
        for item in self.code:
            self.script += item
        return compile(self.script, "<code>", "exec")

    def write(self, string):
        self.code.append(self.tab * self.level + string)

    def indent(self):
        self.level = self.level + 1
        # in 2.0 and later, this can be written as: self.level += 1

    def dedent(self):
        if self.level == 0:
            raise(SyntaxError, "internal error in code generator")
        self.level = self.level - 1 # or: self.level -= 1
        

class DirectoryWalker:
    # a forward iterator that traverses a directory tree
    def __init__(self, directory):
        self.stack = [directory]
        self.files = []
        self.index = 0
    def __getitem__(self, index):
        while 1:
            try:
                file = self.files[self.index]
                self.index = self.index + 1
            except IndexError:
                # pop next directory from stack
                self.directory = self.stack.pop()
                self.files = os.listdir(self.directory)
                self.index = 0
            else:
                # got a filename
                fullname = os.path.join(self.directory, file)
                if os.path.isdir(fullname) and not os.path.islink(fullname):
                    self.stack.append(fullname)
                return fullname


class DirectoryStatWalker:
    # a forward iterator that traverses a directory tree, and
    # returns the filename and additional file information
    def __init__(self, directory):
        self.stack = [directory]
        self.files = []
        self.index = 0
    def __getitem__(self, index):
        while 1:
            try:
                file = self.files[self.index]
                self.index = self.index + 1
            except IndexError:
                # pop next directory from stack
                self.directory = self.stack.pop()
                self.files = os.listdir(self.directory)
                self.index = 0
            else:
                # got a filename
                fullname = os.path.join(self.directory, file)
                st = os.stat(fullname)
                mode = st[stat.ST_MODE]
                if stat.S_ISDIR(mode) and not stat.S_ISLNK(mode):
                    self.stack.append(fullname)
                return fullname, st


# ################################ # ################################  # ################################
# ################################ current test funcion
def sub_main_007():
    # ################################ Testing the method of application of
    print(" ================================================================================ ") 
    info = input()
    N = locale.atoi(info)
    info = input()
    data = info.split(' ')
    buff = []
    for item in data:
        item = locale.atoi(item)
        buff.append(item)
    delta = (buff[len(buff)-1] - buff[0])//(len(buff)) # Python3.x Only used, "//" return the integer when dividing.
    #delta = int(delta)
    iter = 1
    while buff[iter] == buff[0]+iter*delta:
        iter = iter + 1
    print(buff[0]+iter*delta)
    # ################################ Testing the method of application of

    # ################################ Testing the method of application of

    # ################################ Testing the method of application of

    # ################################ Testing the method of application of

    # ################################ Testing the method of application of

    # ################################ Testing the method of application of

    # ################################ Testing the method of application of
    pass


# ################################ # ################################  # ################################
# ################################ current test funcion assist-functions


# ################################ # ################################  # ################################
# ################################ current test funcion
def sub_main_008():
    # ################################ Testing the method of application of format-output
    print(" ================================================================================ ") 
    for i in range(10):
        print("%(i)d -- %(i)d -- %(i)d -- %(i)d" % vars() )
    for i in range(10):
        print("%d -- %d -- %d", i, i*i, i**i)
    for i in range(10):
        print("{0:2d} {1:2d} {2:15d}".format(i, i*i, i**i) )
    for i in range(10):
        print("{0:2d} {1:2d} {2:15d}  {2:20d}".format(i, i*i, i*i*i, i**i) )
    # ################################ Testing the method of application of Python3.x New characters from Py2.x
    # Python3.x new characters diffirent from Python2.x
    print(100//23)       # Python3.x Only used, "//" return the integer when dividing operation.
    print(100/23)
    print(10,12)
    print((10,12))
    print((10,12,18,11))
    print(range(10,12))
    i = 1
    print("oct(",i,") are", oct(i))
    i = 12
    print("oct(",i,") are", oct(i))
    i = 438
    print("oct(",i,") are", oct(i))
    i = 1200
    print("oct(",i,") are", oct(i))
    i = 0o6
    print(oct(i), "are", i)
    i = 0o10
    print(oct(i), "are", i)
    i = 0o12
    print(oct(i), "are", i)
    i = 0o666
    print(oct(i), "are", i)
    i = 6
    print("bin(",i,") are", bin(i))
    i = 32
    print("bin(",i,") are", bin(i))
    i = 2048
    print("bin(",i,") are", bin(i))
    i = 89264978976783264842423523
    print("bin(",i,") are", bin(i))

    #?????��? = 'China'
    #print("Variable it is ", ?????��?)
    b = b'china' 
    print("b = b'china', and type(b) are", type(b))
    bytesStr = b'beautiful YY'
    unicodeStr = bytesStr.decode()
    bytesStr2 = unicodeStr.encode()
    print("bytes variable bytesStr2 are", bytesStr2)
    print("UTF-8 code variable unicodeStr are", unicodeStr)

    # ################################ Testing the method of application of dictionary
    # key-value, int-int dictionary
    dic1 = {19:1000-900, 6:1000-600, 10:1000-000, 4:1000-400, 11:1000-100, 
            2:1000-200, 15:1000-500, 3:1000-300, 17:1000-700, 4:1000-400}
    print("dictory dic1 = ", dic1)
    sorted_dic1 = sorted(dic1.items(), key=operator.itemgetter(0))
    print("sorted_dic1 = ", sorted_dic1)
    sorted_dic1 = sorted(dic1.items(), key=operator.itemgetter(1))
    print("sorted_dic1 = ", sorted_dic1)
    sorted_dic1 = sorted(dic1.items(), key=operator.itemgetter(1), reverse = True)
    print("sorted_dic1 = ", sorted_dic1)
    sorted_dic1 = sorted(dic1.items(), key=lambda dic1 : dic1[0], reverse = True)
    print("sorted_dic1 = ", sorted_dic1)
    sorted_dic1 = sorted(dic1.items(), key=lambda dic1 : dic1[1], reverse = True)
    print("sorted_dic1 = ", sorted_dic1)
    # key-value, int-str dictionary
    dic2 = {10:'HA', 20:'FB', 12:'MC', 32:'XB'}
    print("dictory dic1 = ", dic2)
    sorted_dic2 = sorted(dic2.items(), key=operator.itemgetter(0))
    print("sorted_dic2 = ", sorted_dic2)
    sorted_dic2 = sorted(dic2.items(), key=operator.itemgetter(1), reverse = True)
    print("sorted_dic2 = ", sorted_dic2)
    sorted_dic2 = sorted(dic2.items(), key=lambda dic2 : dic2[0])
    print("sorted_dic2 = ", sorted_dic2)
    sorted_dic2 = sorted(dic2.items(), key=lambda dic2 : dic2[1], reverse = True)
    print("sorted_dic2 = ", sorted_dic2)
    # key-value, list of dictionary
    x = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}, 
         {'name':'Wuen', 'age':21}, {'name':'rain','age':20}]  
    sorted_x = sorted(x, key=operator.itemgetter('name'))
    print("sorted_x = ", sorted_x)
    sorted_x = sorted(x, key=operator.itemgetter('name'), reverse = True)
    print("sorted_x = ", sorted_x)
    sorted_x = sorted(x, key=lambda x : x['name'])
    print("sorted_x = ", sorted_x)
    sorted_x = sorted(x, key=lambda x : x['name'], reverse = True)
    print("sorted_x = ", sorted_x)
    sorted_x = sorted(x, key=lambda x : x['age'])
    print("sorted_x = ", sorted_x)
    sorted_x = sorted(x, key=lambda x : x['age'], reverse = True)
    print("sorted_x = ", sorted_x)
    # ################################ Testing the method of application of Hunter for Offer
    print()
    for i in range(1,20): # From 1 to 20
        if 0 == i%3:
            print(i)
    print()
    for i in range(20): # From 0 to 20
        if 0 == i%3:
            print(i)
    # ################################ Testing the method of application of

    # ################################ Testing the method of application of

    # ################################ Testing the method of application of

    # ################################ Testing the method of application of
    pass


# ################################ # ################################  # ################################
# ################################ current test funcion assist-functions


# ################################ # ################################  # ################################
# ################################ # ################################  # ################################
def main():
    sub_mains()
main()

# ################################ # ################################  # ################################
# ################################  Amazon Online Test - Python2.x    # ################################


# ################################ # ################################  # ################################


# ################################ # ################################  # ################################


# ################################ # ################################  # ################################

#import locale
#def main():
#    info = raw_input()          # Python2.x
#    N = locale.atoi(info)       # import locale
#    info = raw_input()          # Python2.x
#    data = info.split(' ')
#    buff = []
#    for item in data:
#        item = locale.atoi(item)       # import locale
#        buff.append(item)
#    delta = (buff[len(buff)-1] - buff[0])/(len(buff))
#    delta = int(delta)
#    iter = 1
#    while buff[iter] == buff[0]+iter*delta:
#        iter = iter + 1
#    print(buff[0]+iter*delta)
#main()



# ################################ # ################################  # ################################


# ################################ # ################################  # ################################


# ################################ # ################################  # ################################
# ################################                                    # ################################


# ################################ # ################################  # ################################


# ################################ # ################################  # ################################


# ################################ # ################################  # ################################







