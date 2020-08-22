#caculate program

#예외처리
try:
    def caculate():
        equation = input('계산할 수식을 입력해주세요.: ')

        #공백 대체 후 그것을 기준으로 문자열을 나눈다.
        first = equation.replace('+', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' ').split()
        #number에는 숫자만
        number = [int(i) for i in first]
        #sign에는 연산자만
        sign = equation.replace('0', ' ').replace('1', ' ').replace('2', ' ').replace('3', ' ').replace('4', ' ').replace('5',
        ' ').replace('6', ' ').replace('7', ' ').replace('8', ' ').replace('9', ' ').replace('0', ' ').split()

        while len(sign) != 0: # for 루프를 계속 돌리기 위해(계산을 계속하기 위해)
            for i in sign:
                if i == '*':
                    f = sign.index('*')
                    a = number[f] * number[f + 1] #연산자의 앞뒤에 있는 숫자의 인덱스를 사용하여 계산
                    del sign[f] #계산 전 연산자 제거
                    del number[f] #계산 전 숫자 제거
                    number.insert(f, a) #계산 후 숫자를 삽입
                    del number[f + 1]#계산 전 숫자 제거

            for i in sign:
                if i == '/':
                    f = sign.index('/')
                    a = number[f] / number[f + 1]
                    del sign[f]
                    del number[f]
                    number.insert(f, a)
                    del number[f + 1]

            if ('*' or '/') in sign: # 곱하기와 나누기가 계속 있다면 while루프의 처음으로 다시 돌아가 실행
                continue
            for i in sign:
                if (i == '+' or i == '-'): # 더하기와 빼기는 우선순위가 없기때문에
                    if i == '+':
                        f = sign.index('+')
                        a = number[f] + number[f + 1]
                        del sign[f]
                        del number[f]
                        number.insert(f, a)
                        del number[f + 1]

                    elif i == '-':
                        f = sign.index('-')
                        a = number[f] - number[f + 1]
                        del sign[f]
                        del number[f]
                        number.insert(f, a)
                        del number[f + 1]
        print("계산의 결과는")
        print(number)
        print("입니다.")
    #메인함수실행
    caculate()
except ValueError:
    print("ValueError: You did not enter a number.")
except Exception as e:
    print("Unknown error:",e)
