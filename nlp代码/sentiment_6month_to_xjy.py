import pandas as pd
from datetime import datetime

import matplotlib.dates as mdate
import matplotlib.pyplot as plt

df = pd.read_table('./result2.txt',names=['comment_content','create_time','sentiment'],error_bad_lines=False,sep='\t')
# print(df)
df.dropna(axis=0, how='any', inplace=True)
# print(df)
df = df.reset_index()
df = df.set_index('create_time')
del df['index']

# index(datetime)
df.index = [datetime.strptime(datetime.strptime(t, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d'), '%Y-%m-%d') for t in df.index]
df = df.sort_index(ascending=False)
sentiment_mean = df['sentiment'].groupby(df.index).mean().iloc[-190:-7] #3月1日-8月31日
# y 轴
# print(list(sentiment_mean))
# x 轴
# print(list(sentiment_mean.index))
# a = list(sentiment_mean.index)
# new = []
# for i in a :
#     term = str(i).split(" ")[0]
#     new.append(term)
# print(new)

plt.figure(figsize=(15,6),dpi=80)
plt.plot(sentiment_mean, label='新华社公众号评论情感均值')

plt.gca().xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdate.MonthLocator())
plt.gcf().autofmt_xdate()  # 自动旋转日期标记


# plt.legend(loc='upper right')
# plt.xlabel('日期')
# plt.ylabel('情感值')
# plt.title('情感均值变化情况')
plt.show()


# print('情绪最低落的一天:')
# print(sentiment_mean[sentiment_mean.values == sentiment_mean.min()])
# df_min = df[df.index == '2018-07-06']
# print('情绪最低落这一天的评论内容:')
# print(df_min)
#
# print('情绪最高涨的一天:')
# print(sentiment_mean[sentiment_mean.values == sentiment_mean.max()])
# df_min = df[df.index == '2018-07-07']
# print('情绪最高涨这一天的评论内容:')
# print(df_min)
