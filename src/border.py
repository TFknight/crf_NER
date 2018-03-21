# -*- coding: UTF-8 -*-
from __future__ import division
import os
import time
import math
import xlrd
import sys
import codecs
from pinyin import PinYin
reload(sys)
sys.setdefaultencoding('utf-8')

'''
这里的char_ch2.txt是表示词语的频率范围是０－２
char_ch.txt是表示词语的频率范围是０－５
'''
class match(object):

    def __init__(self,input_path,output_path):
        self.input = input_path
        self.output = output_path


    def match_pingyin(self,word):
        test = PinYin()
        test.load_word()
        word_list = test.hanzi2pinyin(word)
        return "".join(word_list)

    def read_name1(self):
        dict_name = {}
        wf1 = open("/home/gaorui/PycharmProjects/untitled3/标注/deal_word/三字名中字特征.txt","r")
        for line in wf1.readlines():
            line = line.split(" ")
            line[1] = line[1].strip().replace("\n","")
            dict_name[line[0]] = line[1]
        wf1.close()
        return dict_name

    def read_name2(self):
        dict_name = {}
        wf1 = open("/home/gaorui/PycharmProjects/untitled3/标注/deal_word/三字名尾字特证.txt","r")
        for line in wf1.readlines():
            line = line.split(" ")
            line[1] = line[1].strip().replace("\n","")
            dict_name[line[0]] = line[1]
        wf1.close()
        return dict_name

    def read_name3(self):
        dict_name = {}
        wf1 = open("/home/gaorui/PycharmProjects/untitled3/标注/deal_word/二字名尾字特征.txt","r")
        for line in wf1.readlines():
            line = line.split(" ")
            line[1] = line[1].strip().replace("\n","")
            dict_name[line[0]] = line[1]
        wf1.close()
        return dict_name

    def read_name4(self):
        dict_name = {}
        wf1 = open("/home/gaorui/PycharmProjects/untitled3/标注/deal_word/姓用字特征.txt","r")
        for line in wf1.readlines():
            line = line.split(" ")
            line[1] = line[1].strip().replace("\n","")
            dict_name[line[0]] = line[1]
        wf1.close()
        return dict_name

    def read_name5(self):
        english_name = []
        wf1 = open("/home/gaorui/PycharmProjects/untitled3/标注/deal_word/English_Names_Corpus（2W）.txt","r")
        list_name = wf1.readlines()
        for i in list_name:
            i = i.strip().replace("\n","")
            english_name.append(i)
        return english_name

    def read_name6(self):
        dict_name = {}
        wf1 = open("/home/gaorui/PycharmProjects/untitled3/标注/deal_word/中文译名首字特征.txt", "r")
        for line in wf1.readlines():
            line = line.split(" ")
            line[1] = line[1].strip().replace("\n", "")
            dict_name[line[0]] = line[1]
        wf1.close()
        return dict_name

    def read_name7(self):
        dict_name = {}
        wf1 = open("/home/gaorui/PycharmProjects/untitled3/标注/deal_word/中文译名中字特征.txt", "r")
        for line in wf1.readlines():
            line = line.split(" ")
            line[1] = line[1].strip().replace("\n", "")
            dict_name[line[0]] = line[1]
        wf1.close()
        return dict_name

    def read_name8(self):
        dict_name = {}
        wf1 = open("/home/gaorui/PycharmProjects/untitled3/标注/deal_word/中文译名尾字特征.txt", "r")
        for line in wf1.readlines():
            line = line.split(" ")
            line[1] = line[1].strip().replace("\n", "")
            dict_name[line[0]] = line[1]
        wf1.close()
        return dict_name

    def read_name9(self):
        dict_name = {}
        wf1 = open("/home/gaorui/PycharmProjects/untitled3/标注/deal_word/border_B_file.txt", "r")
        for line in wf1.readlines():
            line = line.split(" ")
            line[1] = line[1].strip().replace("\n", "")
            dict_name[line[0]] = line[1]
        wf1.close()
        return dict_name

    def read_name10(self):
        dict_name = {}
        wf1 = open("/home/gaorui/PycharmProjects/untitled3/标注/deal_word/border_S_file.txt", "r")
        for line in wf1.readlines():
            line = line.split(" ")
            line[1] = line[1].strip().replace("\n", "")
            dict_name[line[0]] = line[1]
        wf1.close()
        return dict_name

    def match_name(self):
        wf3 = open(self.input,"r")
        wf2 = open(self.output,"w+")

        dict_name1 = self.read_name1()
        dict_name2 = self.read_name2()
        dict_name3 = self.read_name3()
        dict_name4 = self.read_name4()
        list_name5 = self.read_name5()
        dict_name6 = self.read_name6()
        dict_name7 = self.read_name7()
        dict_name8 = self.read_name8()
        dict_name9 = self.read_name9()
        dict_name10 = self.read_name10()

        for line in wf3.readlines():

            if(line == "\n"):
                wf2.write("\n")
                # print "*********"
            else:
                line = line.strip()
                line = line.split("	")
                wf2.write(line[0] + "\t")
                #三名中字特征
                # if(line[0] in dict_name1):
                #     wf2.write(dict_name1[line[0]] + "\t")
                # else:
                #     wf2.write("0" + "\t")
                #三名尾字特征
                if(line[0] in dict_name2):
                    wf2.write(dict_name2[line[0]] + "\t")
                else:
                    wf2.write("0" + "\t")
                #两名尾子特征
                if (line[0] in dict_name3):
                    wf2.write(dict_name3[line[0]] + "\t")
                else:
                    wf2.write("0" + "\t")
                #姓用字特征
                if (line[0] in dict_name4):
                    wf2.write(dict_name4[line[0]] + "\t")
                else:
                    wf2.write("0" + "\t")
                # 英语名字字典,用１．．０来表示有没有特征存在
                if (line[0].lower() in list_name5):
                    print line[0].lower()
                    wf2.write("1" + "\t")
                else:
                    wf2.write("0" + "\t")
                #英文首字特征
                if (line[0] in dict_name6):
                    wf2.write(dict_name6[line[0]] + "\t")
                else:
                    wf2.write("0" + "\t")
                #英文中字特征
                if (line[0] in dict_name7):
                    wf2.write(dict_name7[line[0]] + "\t")
                else:
                    wf2.write("0" + "\t")
                #英文尾字特征
                if (line[0] in dict_name8):
                    wf2.write(dict_name8[line[0]] + "\t")
                else:
                    wf2.write("0" + "\t")

                #边界B特征
                if(line[0] in dict_name9):
                    wf2.write(dict_name9[line[0]] + "\t")
                else:
                    wf2.write("0" + "\t")
                #边界Ｓ特征
                if (line[0] in dict_name10):
                    wf2.write(dict_name10[line[0]] + "\t")
                else:
                    wf2.write("0" + "\t")

                # #二分类
                # if("nr" in line[1]):
                #     line[1]= line[1].replace("nrn","nr").replace("nrf","nr").replace("nre","nr")
                #把最后的答案补上去
                wf2.write(line[1] + "\n")

        wf2.close()
        wf3.close()


if __name__ == "__main__":
    '''
    输入你需要处理的文件以及输出文件,还有处理好ＢＳ特征的文件
    '''
    input_file = "/home/gaorui/PycharmProjects/untitled3/标注/deal_word/new_train.txt"
    output_file = "/home/gaorui/PycharmProjects/untitled3/标注/deal_word/bao_name_train.txt"

    p = match(input_file,output_file)

    p.match_name()