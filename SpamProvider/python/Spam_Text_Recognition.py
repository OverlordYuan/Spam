# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/8/28
"""
import re,pickle
import jieba
import opencc
from patten_config import patten
import jieba.analyse
jieba.load_userdict("cut_dict.txt")
cc = opencc.OpenCC('t2s')

Social_media =['微博','短视频','Twtter','Facebook']
type_word = ['汽车']
mix_word = ['大众']
def target_fliter(title,content,source,targets):
    # print(1)
    title = cc.convert(str(title.replace('·','_')))
    content = cc.convert(str(content))

    if source in Social_media:
        label = Social_media_fliter(content,targets)
    else:
        label = News_media_fliter(title,content,targets)
    return label

def Social_media_fliter(content,targets):
    label = 0
    target = 0
    text = content
    seg_dict = dict.fromkeys(targets, 0)
    patten_flag = 0
    for item in patten:
        obj = re.findall(item, text)
        for tag in obj:
            tag_list = list(jieba.cut(tag))
            tag_num = 0
            for tag_item in tag_list:
                if tag_item in seg_dict.keys():
                    tag_num = 1
                    break
            if tag_num == 1 or (tag.isdigit() and len(tag)<3):
                patten_flag += 1
        if len(obj)-patten_flag>2:
            label = 1
            break
    if label == 0:
        label = 1
        flag = max(len(text) / 200, 1)
        word_list = list(jieba.cut(text))
        for item in word_list:
            item = item.upper()
            if len(item) > 1 and item in seg_dict.keys():
                seg_dict[item] += 1
                target += 1
                if seg_dict[item] >= flag or target >= flag * 2:
                    label = 0
                    print(item)
                    break
    return label

def News_media_fliter(title,content,targets):
    label = 1
    target = 0
    seg_dict = dict.fromkeys(targets, 0)
    word_list = list(jieba.cut(title))
    for item in word_list:
        item = item.upper()
        if len(item) > 1 and item in targets and len(content)>20 and item not in mix_word:
            label = 0
            # print(item)
            break
    if label == 1:
        text = title + content
        flag = max(len(text) / 400, 2)
        # print(flag)
        text_list = list(jieba.cut(text))
        for item in text_list:
            item = item.upper()
            if len(item) > 1 and item in seg_dict.keys():
                seg_dict[item] += 1
                target += 1
                if seg_dict[item] >= flag or target >= flag * 2:
                    label = 0
                    break
    return label

