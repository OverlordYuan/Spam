# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/8/28
"""
import os
import pandas as pd
import datetime
import opencc
from Judgment_function import Judgment_function
from tqdm import tqdm

cc = opencc.OpenCC('t2s')

class Spam():
    def __init__(self,target):
        '''
        本地测试垃圾识别初始化程序
        :param target: 识别的主题及文件的路径
        '''
        self.root_dir = os.path.abspath('.')
        self.input_dir = os.path.join(self.root_dir,'input')
        self.output_dir = os.path.join(self.root_dir,'output')
        self.target = target
        time = str(datetime.datetime.now()).replace(' ', '_').split(':')
        self.label = time[0] + '_' + time[1]

    def read_xls(self):
        data_pd = pd.DataFrame(columns=['title','content','source','label'])
        data_dir = os.path.join(self.input_dir,self.target)
        list = os.listdir(data_dir) #列出文件夹下所有的目录与文件
        for i in range(0,len(list)):
            if os.path.splitext(list[i])[1] == ".xls" or  os.path.splitext(list[i])[1] == ".xlsx":
                path = os.path.join(data_dir,list[i])
                if os.path.isfile(path):
                    print(i)
                    sheet = pd.read_excel(path)
                    if i == 0:
                        data_pd['title'] = sheet['标题']
                        data_pd['content'] = sheet['内容']
                        data_pd['source'] = sheet['数据源']
                        type = set(data_pd['source'].tolist())
                        print(type)
                    else:
                        data_temp = pd.DataFrame()
                        data_temp['title'] = sheet['标题']
                        data_temp['content'] = sheet['内容']
                        data_temp['source'] = sheet['数据源']
                        data_pd = pd.concat([data_pd,data_temp],ignore_index=True,sort=False)
                        type = set(data_pd['source'].tolist())
                        print(type)
        data_pd.to_csv(os.path.join(data_dir,self.target + '.csv'), encoding='utf-8-sig')

    def read_csv(self):
        data_dir = os.path.join(self.input_dir, self.target)
        list = os.listdir(data_dir)  # 列出文件夹下所有的目录与文件
        for i in range(0, len(list)):
            if os.path.splitext(list[i])[1] == ".csv":
                path = os.path.join(data_dir, list[i])
                data_pd = pd.read_csv(path,sep=',',index_col=0)
                return data_pd

    def save_rusult(self,data_pd):
        time = str(datetime.datetime.now()).replace(' ','_').split(':')
        label =time[0]+'_'+time[1]
        data_dir = os.path.join(self.output_dir, self.target)
        try:
            data_pd_dir = os.path.join(data_dir, self.target+'_data_'+label+'.csv')
            garbage_pd_dir = os.path.join(data_dir, self.target+'_spam_'+label+'.csv')
            data = data_pd[data_pd['label'].isin([0])]
            Garbage = data_pd[data_pd['label'].isin([1])]
            self.data_sample([Garbage,data])
            print(Garbage.shape)
            data.to_csv(data_pd_dir, encoding='utf-8-sig')
            Garbage.to_csv(garbage_pd_dir, encoding='utf-8-sig')

        except Exception as e:
            print(e)
            print('Save failed!')


    def Spam_analysis(self,data):
        data_len = data.shape[0]
        data['label'] = [0]*data_len
        for i in tqdm(range(data_len)):
            try:
                try:
                    title = data['title'][i]
                except:
                    title = ''
                try:
                    content =  data['content'][i]
                except:
                    content = ''
                try:
                    source = data['source'][i]
                except:
                    source = ''
                data['label'][i] =Judgment_function(title,content,source)
            except Exception as e:
                print(e)
        return data


    def data_sample(self,data_list):
        filenames = [self.target + '_spam_' + self.label, self.target + '_data_' + self.label]
        data_type = ['垃圾', '有效']
        for i, data in enumerate(data_list):
            print('{}文本数量为:{}'.format( data_type[i], data.shape[0]))
            type = list(set(data['source'].tolist()))
            path = 'output/sample/' + filenames[i]
            if not os.path.exists(path):
                os.mkdir(path)
            for item in type:
                data_temp = data[data['source'].isin([item])]
                print('{}{}文本数量为:{}'.format(item, data_type[i], data_temp.shape[0]))
                if data_temp.shape[0] > 200:
                    temp = data_temp.sample(n=200)
                    temp.to_csv(
                        path + '/' + item + '_' + data_type[i] + '_' + str(data_temp.shape[0]) + 'sample_200.csv',
                        encoding='utf-8-sig')
                else:
                    data_temp.to_csv(
                        path + '/' + item + '_' + data_type[i] + '_' + str(data_temp.shape[0]) + 'sample_' + str(
                            data_temp.shape[0]) + '.csv', encoding='utf-8-sig')
