import random
import pandas as pd
import re
from collections import Counter
import jieba

def token(string):
    return re.findall('\w+', string)


content = pd.read_csv('sqlResult_1558435.csv', encoding='gb18030')

articles = content['content'].tolist()

articles_clean = [''.join(token(str(a))) for a in articles]
print(len(articles_clean))

TOKEN = []
for i, line in enumerate(articles_clean):
    if i % 100 == 0:
        print(i)

    # if i > 2000:
    #     break

    TOKEN += list(jieba.cut(line))

with open('articles_TOKEN.txt', 'w') as f:
    for a in TOKEN:
        f.write(a + '\n')


# word_count = Counter(TOKEN)