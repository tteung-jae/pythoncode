import re

# p = re.compile('ab*')

# m = p.match('abbbc')
# print(m)

# m1 = p.search('babbbc')
# print(m1)

email = input("이메일 입력")
p = re.compile('[a-z][a-z0-9]{4,}@[a-z]{2,}.[a-z]{2,5}')
result = p.match(email)
print(result)