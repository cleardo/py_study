# -*- coding: UTF-8 -*-

import collections
d = collections.defaultdict(lambda:1)


def init(filename='SogouLabDic.dic'):
    f=open(filename,'r')

    total=0

    while True:

        line=f.readline()

        if not line: break

        word, freq = line.split('\t')[0:2]
        #print word.decode('gbk').encode('utf-8')
        #print freq

        # 进行平滑处理
        total += int(freq)+1 # smooth

        #print total

        try:
            # 使用unicode编码
            d[word.decode('gbk')]=int(freq)+1
        except:
            d[word]=int(freq)+1

    f.close()
    d['_t_']=total


def solve(s):
    """
    要分词的字符串
    """
    l=len(s)

    p=[0 for i in range(l+1)]
    print p

    # 最后个字变为1
    p[l]=1

    # 初始化
    div=[1 for i in range(l+1)]
    print "div", div

    t = [1 for i in range(l)]

    for i in range(l-1,-1,-1):
        for k in range(1, l-i+1):
            print "i, k", i, k

            # 算出字典d中指定字符串的频率
            print s[i:i+k]
            tmp = d[s[i:i+k]]

            if k > 1 and tmp == 1:
                # tmp 为0，表示频率为0
                continue

            print "p i+k", i+k, p[i+k]
            print "div i+k", div[i+k]
            # 乘以相同分母，比较分子
            # if(d[s[i:i+k]]*p[i+k]*div[i] > p[i]*d['_t_']*div[i+k]):
            if d[s[i:i+k]] * p[i+k] > p[i]:
                # 如果概率有变大

                # 更新p[i]
                p[i] = d[s[i:i+k]]*p[i+k]

                # 感觉没必要啊?
                div[i] = d['_t_']*div[i+k]

                t[i] = k

    i=0

    while i<l:
        print s[i:i+t[i]],
        i=i+t[i]


if __name__ == '__main__':
    init()
    #print d

    s="其中最简单的就是最大匹配的中文分词"
    # s="匹配的中文分词"

    s=s.decode('utf8')

    solve(s)


