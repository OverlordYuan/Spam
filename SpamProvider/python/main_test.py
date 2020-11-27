# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/8/28
"""
from Spam_Text_Recognition_local import Spam
if __name__ =='__main__':
    a = Spam('汽车')
    # a.read_xls()
    data_pd = a.read_csv()
    d = a.Spam_analysis(data_pd)
    a.save_rusult(d)
