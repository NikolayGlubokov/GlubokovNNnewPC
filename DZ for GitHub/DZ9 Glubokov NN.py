# print('Задание по идее выполнено, но есть некоторые вопросы')
# print('Hello')
# print('Hello')
# print('Hello')
# print('Hello')


def hello(name, word):
    print('Hello,', name, 'Say, ', word)


hello('Nikolay', 'hi')


def change(s):
    a=s[0]
    b=s[len(s)-1]
    for i in range(len(s)):
        if i==0:
            s[i]=b
        if i==len(s)-1:
            s[i]=a
        print(s[i], end=' ')





print(change([1,2,3]))
print(change([16,65,23,16,15]))
print(change(['s','l','o','n','e']))
