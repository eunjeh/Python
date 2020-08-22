#-*-coding:utf-8-*-

from graphics import *

#예외처리
try:
    #메인 함수 정의
    def main():
        print("This program counts each number.")


        #counted 은 GraphWin 의 인스턴스.
        # (title, width, height)
        counted = GraphWin("Number Counting Chart", 350, 270)
        # 클래스함수 setBackground 호출 - color 설정
        counted.setBackground("white")
        # draw 함수를 이용해 counted 에 Text 그려넣기
        # y축 값
        Text(Point(20, 230), '0').draw(counted)
        Text(Point(20, 180), '5').draw(counted)
        Text(Point(20, 130), '10').draw(counted)
        Text(Point(20, 80), '15').draw(counted)
        Text(Point(20, 30), '20').draw(counted)

        num = [0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10]
        # 파일 불러오기
        f = open("1.txt", 'r')

        for p in range(0, 11): # x축 값 (0부터 10까지)
            Text(Point(52.5 + p*25, 240), p).draw(counted)
        for num in range(0, 11): # 세어진 수의 개수를 표현해주는 statistics 라인
            Text(Point(52.5 + num*25, 260), f.count(num)).draw(counted)
        Text(Point(20, 260), 'stats').draw(counted)

        for num in range(0, 11): # 25간격으로 바 생성, 세어진 개수 값을 y축에 표현

            x = num*25
            height = f.count(num)
            bar = Rectangle(Point(40 + x, 230), Point(65 + x, 230 - height*10))
            bar.setFill("green")
            bar.setWidth(2)
            bar.draw(counted)
        input("Press <Enter> to quit")
        counted.close()


    # main 함수 호출
    main()
except ValueError:
    print("ValueError: You did not enter a number.")
except Exception as e:
    print("Unknown error:",e)