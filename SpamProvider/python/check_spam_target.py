# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/8/28
"""
import re,pickle,os
import jieba
import opencc
import jieba.analyse
import pandas as pd
import numpy as np
from patten_config import patten

root_dir = os.path.abspath('.')
input_dir = os.path.join(root_dir, 'input')

jieba.load_userdict("cut_dict.txt")
cc = opencc.OpenCC('t2s')
with open('Car_targets.txt', 'rb') as f:
    targets = pickle.load(f)

Social_media =['微博','短视频','Twtter','Facebook']
def target_find(title,content,source):
    # print(1)
    label = 1
    target = 0
    item0 = ''
    title = cc.convert(str(title))
    content = cc.convert(str(content))
    seg_dict = dict.fromkeys(targets, 0)
    text = title + content
    word_list =list(jieba.cut(title))
    # print(word_list)
    if source not in Social_media:
        for item in word_list:
            item = item.upper()
            if len(item)>1 and item in targets:
                # print(2)
                label = 0
                item0=item
                break
    if label==1:
        if source in Social_media:
            flag = 3
            for item in patten:
                text = re.compile(item).sub('',text)
        else:
            flag = max(len(text) / 400, 2)

        text_list = list(jieba.cut(text))
        # print(text_list)
        for item in text_list:
            item = item.upper()
            if len(item)>1 and item in seg_dict.keys():
                seg_dict[item] += 1
                target += 1
                if seg_dict[item]>=flag or target>flag*2:
                    label = 0
                    item0=item
                    break
    return item0

def read_xls():
    data_pd = pd.DataFrame(columns=['title','content','source','label'])
    data_dir = os.path.join(input_dir,'check')
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
                    data_pd['source'] = sheet['剔除id']
                    data_pd['label'] = sheet['垃圾']
                    # print(type)
                else:
                    data_temp = pd.DataFrame()
                    data_temp['title'] = sheet['标题']
                    data_temp['content'] = sheet['内容']
                    data_temp['source'] = sheet['剔除id']
                    data_temp['label'] = sheet['垃圾']
                    data_pd = pd.concat([data_pd,data_temp],ignore_index=True,sort=False)
                    type = set(data_pd['source'].tolist())
                    # print(type)
    print(data_pd.shape)
    # data = data_pd.loc[data_pd['label']=='上海市三八红旗手走进高校思政课堂']
    data = data_pd.loc[data_pd['label']=='[1]']
    type = set(data['source'].tolist())
    print(type)
    # data = data.loc[data['source']!= float('nan')]
    # print(set(data['source'].tolist()))
    data = data.loc[data['source'] != '[9326]']
    print(set(data['source'].tolist()))
    data = data.reset_index(drop=True)
    # print(data)
    # data.to_csv(os.path.join(data_dir,'check' + '.csv'), encoding='utf-8-sig')
    return data

def Social_media_fliter(content):
    text = content
    word_list = list(jieba.cut(text))
    flag = 2
    new_word_list = []
    for item in patten:
        obj = re.findall(item, text)
        new_word_list += obj
        text = re.compile(item).sub('', text)
    print(list(jieba.cut(','.join(new_word_list))))
    print(list(jieba.cut(text)))
    # print(jieba.analyse.textrank(','.join(new_word_list), topK=5, withWeight=True))
    # print(jieba.analyse.textrank(text, topK=5, withWeight=False))
if __name__=='__main__':
    data = read_xls()
    word_list = []
    print(data.shape[0])
    for i in range(data.shape[0]):
        if isinstance(data.loc[i]['source'],str):
            print(data.loc[i]['title'])
            Social_media_fliter(data.loc[i]['title'])
    # for item in list(set(word_list)):
    #     print(item)
