import pandas as pd
import matplotlib.pyplot as plt

commment_list = []
sentiment_list = []

file = open('./result2.txt','r')

for i in file.readlines():
    if len(i.split('\t')) == 3 :
        commment_list.append(i.split('\t')[0])
        sentiment_list.append(i.split('\t')[2].replace('\n',""))

df = pd.DataFrame({
    'commment': commment_list,
    'sentiment': sentiment_list,
})
# print(df)

df["sentiment"] = df["sentiment"].astype(float)
index1 = df[(df["sentiment"]>=0) & (df["sentiment"]<0.1)]['commment'].count()
index2 = df[(df["sentiment"]>=0.1) & (df["sentiment"]<0.2)]['commment'].count()
index3 = df[(df["sentiment"]>=0.2) & (df["sentiment"]<0.3)]['commment'].count()
index4 = df[(df["sentiment"]>=0.3) & (df["sentiment"]<0.4)]['commment'].count()
index5 = df[(df["sentiment"]>=0.4) & (df["sentiment"]<0.5)]['commment'].count()
index6 = df[(df["sentiment"]>=0.5) & (df["sentiment"]<0.6)]['commment'].count()
index7 = df[(df["sentiment"]>=0.6) & (df["sentiment"]<0.7)]['commment'].count()
index8 = df[(df["sentiment"]>=0.7) & (df["sentiment"]<0.8)]['commment'].count()
index9 = df[(df["sentiment"]>=0.8) & (df["sentiment"]<0.9)]['commment'].count()
index0 = df[(df["sentiment"]>=0.9) & (df["sentiment"]<=1)]['commment'].count()


x = ['[0,0.1)','[0.1,0.2)','[0.2,0.3)','[0.3,0.4)','[0.4,0.5)','[0.5,0.6)','[0.6,0.7)','[0.7,0.8)','[0.8,0.9)','[0.9,1.0]']
y = [index1,index2,index3,index4,index5,index6,index7,index8,index9,index0]
# print(y)

# 这里的饼图只是简单表示。希望前端呈现的效果是：由[0,0.1)->[0.9,1.0]是由灰色像有色彩过度，突出0-1是由消极到积极的过度。
plt.pie(y,labels=x,autopct='%1.2f%%')
plt.show()
