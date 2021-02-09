from wordcloud import WordCloud 
from scipy.misc import imread 
mask = imread('nike.png') 
f = open('jordan.txt','r',encoding='utf-8')
txt = f.read()
wordcloud = WordCloud(background_color= "white", \

                          width = 800, \

                          height = 600, \

                          max_words = 200, \

                          max_font_size= 80, \

                          mask = mask, \

                          ) .generate(txt)

wordcloud.to_file('JordanInWonderland.png')