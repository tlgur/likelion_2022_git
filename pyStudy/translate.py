from googletrans import Translator

tr = Translator()

# str = "안녕하세요 코드라이언입니다."
str = input("번역을 원하는 문장을 입력해주세요 : ")
dest = input("어떤 언어로 번역을 원하시나요?")
detected = tr.detect(str)
# print(detected)
# print(type(detected))

r = tr.translate(str, dest)
# print(r)
# print(type(r))

print("===========출 력 결 과===========")
print(detected.lang,":",str)
print(r.dest,":",r.text)
print("=================================")