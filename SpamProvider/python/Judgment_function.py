# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/8/28
"""
import Car_STR  as car
import House_STR as house

def Judgment_function(title,content,source):
    car_label = 0
    house_label = 0
    try:
        car_label = car.target_fliter(title,content,source)
        house_label = house.target_fliter(title,content,source)
    except Exception as e:
        print(e)
    res = {'car':car_label,'house':house_label}
    return res