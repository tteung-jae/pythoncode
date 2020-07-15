from mod.sound.etc import mod1 as m

a = m.add(2, 4)
print(a)

b = m.sub(4, 1)
print(b)

# import하려는 파일이 다른 폴더에 있을때
import sys
print(sys.path)
# sys.path에 다른 폴더 주소를 추가해준다.
sys.path.append('c:\\python\\pythoncode')
import mtest.mod2
print(mtest.mod2.div(3,5))

