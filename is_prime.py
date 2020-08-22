#-*-coding:utf-8-*-
#문제1번

# 함수 정의하기
def IsPrime(num):
    # num을 2부터 num-1까지의 수로 나눈다.
    for i in range(2,num):
        if num%i == 0:
            return("False")
    return True

# 정수를 입력받아 소수인지 아닌지를 판별한다.
num = int(input("정수를 입력해주세요."))
# -1이 아닌 상황이 참일때 무한히 도는 루프
while (num != -1):

    if num <= 0:
        print("잘못 입력하였습니다. 2이상의 값을 입력하여 주십시오")
    elif num == 1:
        print("False")
    elif num == 2:
        print("True")
    else:
        # 함수 호출
        print(IsPrime(num))
    num = int(input("정수를 다시 입력해주세요."))



