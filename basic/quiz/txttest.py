# f = open("test.txt", 'w', encoding='utf8')
# f.write("txt파일 생성")
# f.close()

f = open("./basic/quiz/test.txt", 'r', encoding='utf8')
line = "a"
while line:
    line = f.readline()
    print(line)
f.close()

f = open("./basic/quiz/test.txt", 'r', encoding='utf8')
line = f.readlines()
print(line)
f.close()
