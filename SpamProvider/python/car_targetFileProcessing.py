# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/9/16
"""
import pandas as pd
import pickle
def targetFileProcessing():
    data = pd.read_csv('input/汽车品牌知识库.csv', encoding = 'gb2312',index_col='序号')
    temp0 = data['品牌'].tolist()
    temp0 = list(set(temp0))
    aa = []
    for item in temp0:
        if len(item) == 2:
            aa.append(item + '车')
    temp0 = temp0+aa
    temp1 = data['品牌分类'].tolist()
    # temp2 = data['汽车型号'].tolist()
    temp = temp0+temp1
    data_list = (list(set(temp)))
    with open('car_target_remove_dict.txt','r',encoding='utf-8') as f:
        item = f.readline().replace('\n', '')
        while item:
            if item:
                if item in data_list:
                    data_list.remove(item)
            item = f.readline().replace('\n', '')
    with open('car_target_add_dict.txt','r',encoding='utf-8') as f:
        item = f.readline().replace('\n', '')
        while item:
            if item:
                if item not in data_list:
                    data_list.append(item)
            item = f.readline().replace('\n', '')

    data_list  = list(map(lambda x:x.upper(),data_list))
    print(len(data_list))
    with open('Car_targets.txt', 'wb') as f:
        pickle.dump(data_list, f, pickle.HIGHEST_PROTOCOL)

if __name__ == "__main__":
    targetFileProcessing()
