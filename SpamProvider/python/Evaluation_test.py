# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/9/27
"""
import re,pickle,os
import datetime
import opencc
import pandas as pd
import numpy as np
from patten_config import patten
import random

root_dir = os.path.abspath('.')
output_dir = os.path.join(root_dir,'output')
input_dir = os.path.join(root_dir, 'input')

def eachfile(filepath):
    '''

    :param filepath: 文件夹路径
    :return: soundfile:excel文件列表
    '''
    soundfile = []
    pathdir = os.listdir(filepath)
    for s in pathdir:
        newdir = os.path.join(filepath, s)  # 将文件名加入到当前文件路径后面
        if os.path.isfile(newdir):  # 如果是文件
            if os.path.splitext(newdir)[1] == ".xls" or os.path.splitext(newdir)[1] == ".xlsx":
                soundfile.append(newdir)# 如果文件是".pdb"后缀的
    return soundfile

def read_xls(filename,sample):
    '''
    随机读取excel文件
    :param filename:文件夹名称
    :param sample:抽样比例或抽样数量
    :return data_pd：合并后的数据
    '''
    data_dir = os.path.join(input_dir, filename)
    list = eachfile(data_dir)  # 列出文件夹下所有的目录与文件
    data_pd = pd.DataFrame(columns=['title', 'content', 'source', 'label'])

    if sample:
        if isinstance(sample,float):
            sample_num = random.sample(range(len(list)),round(len(list)*sample))
        elif isinstance(sample,int):
            if sample>len(list):
                sample_num = range(len(list))
            else:
                sample_num = random.sample(range(len(list)), sample)
        else:
            print('采样数据输入错误，已经将采样比例设为100%！')
            sample_num = range(len(list))
    else:
        sample_num = range(len(list))

    for i in sample_num:
        if os.path.isfile(list[i]):
            try:
                sheet = pd.read_excel(list[i])
                if i == 0:
                    data_pd['title'] = sheet['标题']
                    data_pd['content'] = sheet['内容']
                    data_pd['source'] = sheet['数据源']
                    data_pd['label'] = sheet['垃圾']
                    # print(type)
                else:
                    data_temp = pd.DataFrame()
                    data_temp['title'] = sheet['标题']
                    data_temp['content'] = sheet['内容']
                    data_temp['source'] = sheet['数据源']
                    data_temp['label'] = sheet['垃圾']
                    data_pd = pd.concat([data_pd,data_temp],ignore_index=True,sort=False)
            except:
                print(i)
    data_pd.to_csv(os.path.join(data_dir, '评估.csv'), encoding='utf-8-sig')
    return data_pd

def data_sample(target,data_list):
    time = str(datetime.datetime.now()).replace(' ', '_').split(':')
    label = time[0] + '_' + time[1]
    filenames = [target + '_spam_' + label, target + '_data_' + label]
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
            if data_temp.shape[0] > 500:
                temp = data_temp.sample(n=500)
                temp.to_csv(
                    path + '/' + item + '_' + data_type[i] + '_' + str(data_temp.shape[0]) + 'sample_500.csv',
                    encoding='utf-8-sig')
            else:
                data_temp.to_csv(
                    path + '/' + item + '_' + data_type[i] + '_' + str(data_temp.shape[0]) + 'sample_' + str(
                        data_temp.shape[0]) + '.csv', encoding='utf-8-sig')

def save_rusult(target,data_pd):
    time = str(datetime.datetime.now()).replace(' ','_').split(':')
    label =time[0]+'_'+time[1]
    data_dir = os.path.join(output_dir,target)
    try:
        data_pd_dir = os.path.join(data_dir, target+'_data_'+label+'.csv')
        garbage_pd_dir = os.path.join(data_dir, target+'_spam_'+label+'.csv')
        data = data_pd[data_pd['label'].isin([0])]
        Garbage = data_pd[data_pd['label'].isin([1])]
        data_sample(target,[Garbage,data])
        print(Garbage.shape)
        data.to_csv(data_pd_dir, encoding='utf-8-sig')
        Garbage.to_csv(garbage_pd_dir, encoding='utf-8-sig')

    except Exception as e:
        print(e)
        print('Save failed!')

if __name__ == "__main__":
    data_pd = read_xls('test',100)
    data = data_pd.loc[data_pd['label'] == '[0]']
    spam = data_pd.loc[data_pd['label']=='[1]']

    # data.to_csv(data_pd_dir, encoding='utf-8-sig')
    # Garbage.to_csv(garbage_pd_dir, encoding='utf-8-sig')
    data_sample('评估', [spam,data])
    # data_pd.to_csv(os.path.join(data_dir, self.target + '.csv'), encoding='utf-8-sig')
    # print(data_pd.shape)
