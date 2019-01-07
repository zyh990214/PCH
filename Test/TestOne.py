

#这段代码就是测试我的pachram是否能同步到git中,写的代码是我今天看到的一个练习题

#here is a sample of english text这段话中每个字母出现了几次

s = "here is a sample of english text"
d = {}
for i in s:
    if i in d:
        d[i] = d[i] + 1
        print(d[i])
    else:
        d[i] = 1
print(d)