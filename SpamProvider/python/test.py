import jieba
from jieba import analyse
import Spam_Text_Recognition as st
# 引入TextRank关键词抽取接口
textrank = analyse.textrank

jieba.load_userdict("cut_dict.txt")
text = r"//@废橙一个:恭喜王一博！一直低调努力，博得大众喜爱！《陪你到世界之巅》正在芒果TV热播，《陈情令》正在腾讯视频热播，《天天向上》相约不变，新作《有翡》敬请期待！@UNIQ-王一博 ​​​".replace('·','')
print(len(text))
temp = list(jieba.lcut(text))
print(temp)
# label = st.Social_media_fliter(text)
