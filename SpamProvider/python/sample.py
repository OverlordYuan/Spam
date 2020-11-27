# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/9/04
"""
import pandas as pd
import os
def data_sample(target,data_time):
    filenames = [target+'_spam_'+data_time,target+'_data_'+ data_time]
    data_type = ['垃圾','有效']
    for i,filename in enumerate(filenames):
        file_name_type =filename.split('_')[1]
        data =pd.read_csv('output/'+target+'/'+filename+'.csv',index_col=0)
        print('{}文本数量为:{}'.format(file_name_type,data.shape[0]))
        type = list(set(data['source'].tolist()))
        path = 'output/sample/' + filename
        if not os.path.exists(path):
            os.mkdir(path)
        for item in type:
            data_temp = data[data['source'].isin([item])]
            print('{}{}文本数量为:{}'.format(item,data_type[i],data_temp.shape[0]))
            if data_temp.shape[0]>2000:
                temp = data_temp.sample(n=2000)
                temp.to_csv(path+'/'+item+'_'+file_name_type+'_'+str(data_temp.shape[0])+'sample_100.csv',encoding='utf-8-sig')
            else:
                data_temp.to_csv(path+'/'+item+'_'+file_name_type+'_'+str(data_temp.shape[0])+'sample_'+str(data_temp.shape[0])+'.csv',encoding='utf-8-sig')
if __name__ == "__mian__":
    data_sample('汽车', '2019-09-11_16_58')
    print(1)