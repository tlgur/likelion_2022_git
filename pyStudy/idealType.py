totalDic = {}

while True:
    question = input("질문을 입력해주세요 : ")
    if(question == 'q'):
        break
    totalDic[question] = ""

for i in totalDic:
    totalDic[i] = input(i + " : ")
print(totalDic)