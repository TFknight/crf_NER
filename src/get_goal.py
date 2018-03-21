# -*- coding: utf-8 -*-

from __future__ import division

class get_reuslt_goal(object):
    def __init__(self, n):
        self.document = n

    def result_goal(self):
        #计算准确率
        sum = 0
        list1 = []
        list2 = []

        #我处理好的
        with open(self.document,"r") as p1:
            for i in p1.readlines():
                i = i.replace("\n","")
                if(i):
                    i = i.split("\t")
                    list1.append(i[i.__len__()-1])
                    if(i[i.__len__()-2] == i[i.__len__()-1]):
                        print i[i.__len__()-2],i[i.__len__()-1]
                        sum += 1
                    # print i[2]
                else:
                    continue
        print sum
        print "准确率为：　　"
        print sum/(list1.__len__())

    def result_name_goal(self):
        #计算召回率
        sum = 0
        list1 = []
        list_name = []
        sum_total_name = 0
        sum_predict_name = 0
        #我处理好的
        '''
        i[i.__len__()-2]是指源文档中被标记为人名的字体

        i[i.__len__()-1])是指预测文档中被标记为人名的字体

        '''
        with open(self.document,"r") as p1:
            for i in p1.readlines():
                #逐行读取
                i = i.replace("\n","")
                if (i.__len__() == 0):

                    #这里用每个句子里面有多少个ＢＭＥ来判断预测出来的准确人名有多少

                    str_name = "".join(list_name)
                    print
                    print "BE数量：　　",str_name.count("BE")
                    print "BME数量：　　",str_name.count("BME")


                    sum_predict_name += str_name.count("BME")
                    sum_predict_name += str_name.count("BE")
                    list_name = []
                    print "****"

                else:
                    i = i.split("\t")

                    #确实是人名
                    if("nr" in i[i.__len__()-2] ):

                        #这里计算应该计算出来的总人名数,测试集统计出来的人名数
                        if("E" in i[i.__len__()-2] or "S-n" in i[i.__len__()-2]):
                            sum_total_name +=1
                        list1.append(i[i.__len__()-2])


                        if("-" in i[i.__len__()-2] and "-" in i[i.__len__()-1]):

                            if("S-n" in i[i.__len__()-1]):
                                sum_predict_name +=1

                            print i[0],i[i.__len__()-2],i[i.__len__()-1]
                            sum += 1
                            line = i[i.__len__()-1].split("-")
                            str_tag = line[0]
                            list_name.append(str_tag)



        print sum
        print list1.__len__()
        print "人名准确率为：　　"
        print sum/(list1.__len__())
        accuracy = sum/(list1.__len__())

        print "总人数为：　",sum_total_name
        print "预测出的人数为：　",sum_predict_name
        print "人名召回率为：　",sum_predict_name/(sum_total_name)
        recall = sum_predict_name/(sum_total_name)

        print "f1值为：　",2*accuracy*recall/(accuracy + recall)

#输出最终的准确率
v = get_reuslt_goal('vali_bao2.txt')
v.result_name_goal()


