# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/10/08
"""
import pickle
import Spam_Text_Recognition as st
with open('dict/House_targets.txt', 'rb') as f:
    targets = pickle.load(f)

def target_fliter(title, content, source):
    label = st.target_fliter(title, content, source, targets)
    return label