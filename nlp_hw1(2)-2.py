from collections import Counter
import matplotlib.pyplot as plt
import jieba

TOKEN_a = []
with open('articles_TOKEN.txt') as f:
    for i in f:
        TOKEN_a.append(i[:-1])

word_count = Counter(TOKEN_a)

# f = [f for w, f in word_count.most_common(100)]
# x = [i for i in range(100)]
# plt.plot(x, f)
# plt.show()

TOKEN_2_GRAM = [''.join(TOKEN_a[i : i + 2]) for i in range(len(TOKEN_a[:-1]))]
word_count_2 = Counter(TOKEN_2_GRAM)

def prob_1(word):
    return word_count[word] / len(TOKEN_a)

def prob_2(word1, word2):
    if word1 + word2 in word_count_2:
        return word_count_2[word1 + word2] / word_count[word2]
    else:
        return 1 / len(TOKEN_a)

def get_probablity(sentence):
    words = list(jieba.cut(sentence))
    sentence_pro = 1
    for i, word in enumerate(words[:-1]):
        next_ = words[i + 1]
        probablity = prob_2(word, next_)
        sentence_pro *= probablity

        sentence_pro *= prob_1(words[-1])
    return  sentence_pro

need_compared = [
    "今天晚上请你吃大餐，我们一起吃日料 明天晚上请你吃大餐，我们一起吃苹果",
    "真事一只好看的小猫 真是一只好看的小猫",
    "今晚我去吃火锅 今晚火锅去吃我",
    "洋葱奶昔来一杯 养乐多绿来一杯"
]
for s in need_compared:
    s1, s2 = s.split()
    p1, p2 = get_probablity(s1), get_probablity(s2)

    better = s1 if p1 > p2 else s2

    print('{} is more possible'.format(better))
    print('-' * 4 + ' {} with probility {}'.format(s1, p1))
    print('-' * 4 + ' {} with probility {}'.format(s2, p2))
