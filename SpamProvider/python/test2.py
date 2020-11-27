import pickle
with open('dict/House_targets.txt', 'rb') as f:
    data  = pickle.load(f)
print(len(data))
# for item in data:
#     newdata.append(item.replace('\n',"|"))
with open('input/house.txt', 'w',encoding='utf-8') as f:
    for i in range(3):
        f.write('|'.join(data[i*180:i*180+180]))
        f.write('\n')
# print(newdata)