#-*-coding:utf-8-*-
#문제3번

#윤년 판별 함수 정의해두기.
def IsLeapYear(year):
    if (year%4 ==0 and year%100 != 0):
        return ("True")
    elif ( year%400 == 0):
        return ("True")
    else:
        return("False")

#함수 정의하기
def GetDayOfYear(year,month):
    #year에 대한 조건은 없고 month 조건만.
    if month == (1 or 3 or 5 or 7 or 8 or 10 or 12):
        return ("이 달은 31일까지 있습니다.")
    elif month == (4 or 6 or 9 or 11):
        return ("이 달은 30일까지 있습니다.")
    #month가 2월일 경우 윤년판별함수를 호출한다.
    elif (IsLeapYear(year)) == ("True") and month == 2:
        return ("이 달은 29일까지 있습니다.")
    elif (IsLeapYear(year)) ==  ("False") and month == 2:
        return ("이 달은 28일까지 있습니다.")

#연도와 월을 입력받고 함수속 판별결과를 출력한다.
year = int(input("연도를 입력해주세요."))
month = int(input("월을 입력해주세요."))
print(GetDayOfYear(year, month))