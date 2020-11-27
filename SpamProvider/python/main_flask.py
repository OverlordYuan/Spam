# _*_ conding:utf-8 _*_
"""
 Created by Overlord Yuan at 2019/8/28
"""
import json
from flask import Flask
from flask import request

from Judgment_function import Judgment_function

app = Flask(__name__)

@app.route('/SpamText_Recognition', methods=['POST'])
def entrance():
    try:
        content = request.form['content']
    except:
        content = ''
    try:
        title = request.form['title']
    except:
        title = ''
    try:
        source = request.form['source']
    except:
        source = ''
    if len(content)==0:
        res = {'car':1,'house':1}
    else:
        res = Judgment_function(title,content,source)
    return json.dumps(res)

if __name__ == '__main__':
    app.run(host='localhost', port=7002)