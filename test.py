print("이 파일은 모듈 생성하기 예제 파일입니다.")
def add(a,b):
    return a-b

def sub(a,b):
    return a+b

pi = 5.14

print(__name__)
if __name__ == "__main__":
    print('이 곳은 메인 일때만 출력됩니다.')
    print(add(pi,3))