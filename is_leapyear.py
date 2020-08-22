#-*-coding:utf-8-*-
#문제2번

# 함수 정의하기
def IsLeapYear(year):
    if (year%4 == 0 and year%100 != 0) :
        return("True")
    elif( year%400 == 0):
        return ("True")
    else:
        return("False")

# 연도를 입력받아 윤년인지 아닌지 판별한다.
y = int(input("연도를 입력해주세요."))
# -1이 아닌 상황이 참일때 무한히 도는 루프
while (y != -1) :
    if y <= 0:
        print("잘못 입력하였습니다. 1이상의 값을 입력하여 주십시오.")
    else:
        # 각 리턴값에 대응되는 출력값
        # 함수호출
        if (IsLeapYear(y)) == ("True"): print("윤년입니다.")
        elif (IsLeapYear(y)) == ("False"): print("윤년이 아닙니다.")
    y = int(input("연도를 다시 입력해주세요."))