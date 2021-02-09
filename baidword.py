#-*- coding: UTF-8 -*-
#前提是python已安装aip库--》pip install baidu-aip
 
import os
from aip import AipOcr  # baidu-api
import json
APP_ID = '' #你的APP_ID
API_KEY = '' #你的API_KEY
SECRET_KEY = ''	#你的SECRET_KEY
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
os.chdir("C:\\Users\\86157\\Desktop\\xhh")  #你需要转换的图片目录C:\Users\86157\Desktop
dirs = os.listdir()
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"
 
print('开始处理，共'+str(len(dirs))+"张图片。")
flag=0
T = 0 #统计处理图片成功的数量
for filePath in dirs:
    if filePath.split('.')[-1]=='txt':continue
    flag+=1
    print('正在处理第'+str(flag)+'张图片')
    try:
        result = aipOcr.basicGeneral(get_file_content(filePath), options)
    except BaseException as e:
        print(e)
    else:
        try:
            with open(filePath.split('.')[0]+'.txt','w',encoding='utf-8') as f:
                for i in result['words_result']:
                        f.write(i['words']+'\n')
                T += 1
        except BaseException as e :
            print(e)
        else:
            print('处理完成')
print('{}全部处理完成！{}'.format("="*30,"="*30))
print('处理成功的图片有{}张,处理失败的图片有{}张'.format(T,len(dirs)-T))


#注意需要导入的三个值 APP_ID 、API_KEY 、SECRET_KEY 。在百度文字识别项目里可以查看