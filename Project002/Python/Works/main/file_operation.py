#
# This file is created and completed at 2015/09/12 to study Python-language.
# It is mainly to operate on the file operations.
#
import os
import re
import shutil
import time


# 模块功能自测
def main_test():
    FileOper.test_mains()
    people = People('tom', 10, 30)
    people.speak()
    student = Student('ken', 20, 60, 3)
    student.speak()
    person1 = Person('Wvsen1')
    person1.say_hi()
    person2 = Person('Wvsen2')
    person2.say_hi()
    person = Person('Wvsen')
    person.say_hi()
    person.how_many()


# 类定义，操作
class FileOper:

    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    @classmethod
    def __init__(cls, n, a, w):
        cls.name = n
        cls.age = a
        cls.__weight = w

    @staticmethod
    def submain001_open_read_write_file():
        print(" ================================================================================ ")
        print(" ===========  " + __file__)
        print("当前工作目录：" + os.getcwd())
        parent_path = os.path.dirname(os.getcwd())
        print("当前工作目录的父目录：" + parent_path)
        if not os.path.exists(parent_path):
            os.makedirs(parent_path)
        print("当前工作目录：" + os.getcwd())
        os.chdir(parent_path + "/src")
        print("当前工作目录：" + os.getcwd())
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

        # ###########################################Testing the method of application of
        if not os.path.exists("NewTest/multiple/levels"):
            os.makedirs("NewTest/multiple/levels")
        fp = open("NewTest/multiple/levels/file", "w")
        fp.write("inspector praline")
        fp.close()
        # remove the file
        os.remove("NewTest/multiple/levels/file")
        # and all empty directories above it
        os.removedirs("NewTest/multiple/levels")
        # ########################################### high-level operation wiht the directories
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
        # ########################################### File Analysis
        srcFileName = "poem.txt"
        dirRoot = "src/FileAnalysis/"
        timeStr = time.strftime('%Y%m%d_%H%M%S%m', time.localtime(time.time()))
        dstFileName = "poemExtractResult_" + timeStr + ".txt"
        print("当前工作目录：" + os.getcwd())
        os.chdir(parent_path)
        print("当前工作目录：" + os.getcwd())
        if os.path.exists(dirRoot + srcFileName):
            fpR = open("src/FileAnalysis/poem.txt", "r")
            readLineCurr = fpR.readline()
            print(readLineCurr)
            if not os.path.exists(dirRoot + dstFileName):
                fpW = open(dirRoot + dstFileName, "w")
                fpW.write("Extract result from src/FileAnalysis/poem.txt\n\n")
                fpW.write('%f\n\n' % time.time())
                fpW.write('%s\n\n' % time.ctime())
                # fpW.write(time.localtime())
                fpW.write(time.strftime('%Y-%m-%d %H:%M:%S.%m', time.localtime()))
                fpW.write("\n\n")
                fpW.write('%s\n\n' % readLineCurr)
                fpW.close()
            fopen = open(dirRoot + dstFileName, "a")
            allSrc = fpR.read()
            match = re.search(r'part00[0-9]', allSrc)
            print("\n\n ************************************************************************")
            print("\n\n ")
            print("match.string:" + match.string)
            print("match.re:")
            print(match.re)
            print("match.pos:%d" % (match.pos))
            print("match.endpos:%d" % (match.endpos))
            if match.lastindex != None:
                print("match.lastindex:%d" % (match.lastindex))
            # print("match.lastgroup:"+match.lastgroup)
            # print("match.group(1,2):"+match.group(1,2))
            # print("match.groupdict():"+match.groupdict())
            # print("match.start(2):"+match.start(2))
            # print("match.end(2):"+match.end(2))
            # print("match.span(2):"+match.span(2))
            # print(r"match.expand(r'\2 \1\3'):"+match.expand(r'\2 \1\3'))
            reResult = re.findall(r'part0[0-9][0-9]', allSrc)
            print('============================\nSearch Result:\n')
            print(reResult)
            for item in reResult:
                fopen.write("%s\n" % item)
            reResult = re.findall(r'part0/d/d', allSrc)
            print('============================\nSearch Result:\n')
            print(reResult)
            for item in reResult:
                fopen.write("%s\n" % item)
            fopen.close()
            fpR.close()
        print('============================\n\nRE Result:\n')
        s = 'ababab abbabb aabaab abab mmmmababmm mmmabab abababmm ababababb'
        result = re.findall(r'/b(?:ab)+/b', s)
        print(result)
        print('============================\n\nRE Result:\n')

    @staticmethod
    def submain002_regular_expression_operation():
        print(" ================================================================================ ")
        print(" ===========  " + __file__)
        parent_path = os.path.dirname(__file__)
        os.chdir(parent_path)
        print("当前工作目录：" + os.getcwd())
        os.chdir(os.pardir)
        print("当前工作目录：" + os.getcwd())
        # ########################################### File Analysis
        srcFileName = "poem.txt"
        dirRoot = "src/FileAnalysis/"
        timeStr = time.strftime('%Y%m%d_%H%M%S%m', time.localtime(time.time()))
        dstFileName = "poemExtractResult_" + timeStr + ".txt"

        if os.path.exists(dirRoot + srcFileName):
            # ########################################## 测试用
            fpR = open("src/FileAnalysis/poem.txt", "r")
            readLineCurr = fpR.readline()
            print(readLineCurr)
            if not os.path.exists(dirRoot + dstFileName):
                fpW = open(dirRoot + dstFileName, "w")
                fpW.write("Extract result from src/FileAnalysis/poem.txt\n\n")
                fpW.write('%f\n\n' % time.time())
                fpW.write('%s\n\n' % time.ctime())
                # fpW.write(time.localtime())
                fpW.write(time.strftime('%Y-%m-%d %H:%M:%S.%m', time.localtime()))
                fpW.write("\n\n")
                fpW.write('%s\n\n' % readLineCurr)
                fpW.close()
            fileTarget = open(dirRoot + dstFileName, "a")
            allSrc = fpR.read()
            fpR.close()
            match = re.search(r'part00[0-9]', allSrc)
            if 'unexist' in dir():
                print("源数据：" + allSrc)
                print("查询结果")
                print("\n\n ************************************************************************")
                print("\n\n ")
                print("match.string:" + match.string)
                print("match.re:")
                print(match.re)
                print("match.pos:%d" % (match.pos))
                print("match.endpos:%d" % (match.endpos))
            if match.lastindex != None:
                print("match.lastindex:%d" % (match.lastindex))
            # ########################################## 匹配模式截取源文件，获取截取节点列表
            fpRead = open("src/FileAnalysis/poem.txt", "r")
            fpRead.seek(0)
            allSrc = fpRead.read()
            fpRead.close()
            pattern = r'part0\d+\b'
            startIndex = []
            for iter in re.finditer(pattern, allSrc):
                print("========================================================================================\n")
                print("===================初级匹配结果")
                print(iter.group(), iter.span())
                startIndex.append(iter.span()[0])
            startIndex.append(len(allSrc))
            # ########################################## 次级模式匹配     |  s1 9b'xxxxxx000  -------------
            patternSub = r'\s*\|\s*s\d*\s*\d{1,3}b\'x*\d*\b'
            patternTrp = r'x\d*\b'
            sIndex = startIndex.pop(0)
            count = 0
            while startIndex:
                count = count + 1
                tIndex = startIndex.pop(0)
                srcStr = allSrc[sIndex:tIndex]
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("第 %d 段切片" % count)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("切片范围：")
                print([sIndex, tIndex])
                print("切片内容：")
                print(srcStr)
                for iterSub in re.finditer(patternSub, srcStr):
                    print("===================二级匹配结果")
                    print(iterSub.group(), iterSub.span())
                    thirdStr = iterSub.group()
                    for iterTrp in re.finditer(patternTrp, thirdStr):
                        print("最终幻想：%d" % int(iterTrp.group()[1:]))
                sIndex = tIndex

    @staticmethod
    def test_mains():
        print("OK")
        FileOper.submain001_open_read_write_file()
        FileOper.submain002_regular_expression_operation()


# 类定义 ---------------仅测试用
class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    # 定义构造方法

    @classmethod
    def __init__(cls, n, a, w):
        cls.name = n
        cls.age = a
        cls.__weight = w
    @classmethod
    def speak(cls):
        print("%s is speaking: I am %d years old" % (cls.name, cls.age))


# 单继承示例 ---------------仅测试用
class Student(People):
    grade = ''

    @classmethod
    def __init__(cls, n, a, w, g):
        # 调用父类的构函
        People.__init__(n, a, w)
        cls.grade = g
        # 覆写父类的方法

    @classmethod
    def speak(cls):
        print("%s is speaking: I am %d years old,and I am in grade %d" % (cls.name, cls.age, cls.grade))


# 类 ---------------仅测试用
class Person:
    # '''Represents a person.'''
    population = 0

    @classmethod
    def __init__(cls, name):
        # '''Initializes the person's data.'''
        cls.name = name
        print('(Initializing %s)' % cls.name)
        # When this person is created, he/she
        # adds to the population
        Person.population += 1

    @classmethod
    def __del__(cls):
        # '''I am dying'''
        print('%s says bye.' % cls.name)
        Person.population -= 1
        if Person.population == 0:
            print('I am the last one.')
        else:
            print('there are still %d people left.' % Person.population)

    @classmethod
    def say_hi(cls):
        # '''Greeting by the person
        # Really, that's all it does.'''
        print('Hi, my name is %s.' % cls.name)

    @staticmethod
    def how_many():
        # '''Prints the current population.'''
        if Person.population == 1:
            print('I am the only person here.')
        else:
            print('We have %d persons here.' % Person.population)


# 模块功能定义
if __name__ == "__main__":
    main_test()
__name__

