# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/9/04
"""
from main_test import Spam
import pandas as pd
def pre_data(data):
    name = set(data['title'].tolist())
    content = []
    for i in name:
        temp0 = ''
        temp = data['content'][data[data.T.index[0]] == i]
        # print(temp)
        for j in range(temp.shape[0]):
            temp1 =temp.values[j]
            if isinstance(temp1,str):
                temp0 += temp.values[j]
        content.append(temp0)
    new_data = pd.DataFrame({"content":content})
    return new_data
if __name__ =='__main__':
    a = Spam('华为')
    # data_pd = pd.read_csv(path, index_col=0)
    test = a.read_csv()
    test['source'] = '微博'
    d = a.Spam_analysis(test)
    a.save_rusult(d)

    # data = pd.read_csv('input/华为/huawei.csv', index_col=0)
    # print('文本数量为:{}'.format(data.shape[0]))
    # type = list(set(data['source'].tolist()))
    # # print(type[0])
    # for item in type:
    #     data_temp = data[data['source'].isin([item])]
    #     print('{}文本数量为:{}'.format(item, data_temp.shape[0]))
        # if data_temp.shape[0] > 100:
        #     temp = data_temp.sample(n=100)
        #     temp.to_csv('output/sample/' + item + '_garbage_' + str(data_temp.shape[0]) + 'sample_100.csv',
        #                 encoding='utf-8-sig')
        # else:
        #     data_temp.to_csv('output/sample/' + item + '_garbage_' + str(data_temp.shape[0]) + 'sample_' + str(
        #         data_temp.shape[0]) + '.csv', encoding='utf-8-sig')
