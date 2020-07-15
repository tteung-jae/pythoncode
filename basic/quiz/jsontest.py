import json

# 테스트용 Python Dictionary
customer = {
    'id': 21422514,
    'name': '김승재', 
    'history': [
        {'date':'2015-03-11', 'item':'tPhone'},
        {'date':'2016-02-23', 'item':'Monitor'}
    ]
}

# json.load json 파일을 읽어서 파이썬 객체로 변경
with open("./basic/quiz/data.json", "rb") as f:
    data = json.load(f)

# Json 인코딩
# jsonString = json.dumps(customer)

# 문자열 출력

# json.dumps 파일로 바로 저장
with open('./basic/quiz/data.json', 'wt') as f:
    json.dump(customer, f, indent=4)    # indent=4 : 들여쓰기 4칸