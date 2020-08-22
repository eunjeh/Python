#-*-coding:utf-8-*-

from graphics import *

#메인 함수 정의
def textcount():
    f = open('C:/python36/1.txt', 'r')
    a = f.read() #파일 전체를 읽음
    freq = []
    wordlist = a.split() #공백을 기준으로 단어 나누기
    b = set(wordlist) #중복되는 단어 제거
    li = list(b)
    for i in b:#중복 없는 단어들을 차례로 중복 있는 리스트에서 개수 세기
        freq.append(wordlist.count(i))
    m = max(freq)
    # counted 은 GraphWin 의 인스턴스.
    # (title, width, height)
    counted = GraphWin("Text frequency counting program", 500, 10*m)
    # 클래스함수 setBackground 호출 - color 설정
    counted.setBackground("white")
    # draw 함수를 이용해 counted 에 Text 그려넣기
    # y축 값 - 최댓값을 최대 y 값으로 나타내기
    Text(Point(20, 10*m-30), '0').draw(counted)
    Text(Point(20, 10*m-80), '5').draw(counted)
    Text(Point(20, 10*m-130), '10').draw(counted)
    Text(Point(20, 10*m-180), '15').draw(counted)
    Text(Point(20, 10*m-230), '20').draw(counted)
    Text(Point(20, 20), m).draw(counted)

    for n in range(0,7):  # x축 값 - 인덱스 0 부터 6까지 7개의 단어
        q = li[n]
        Text(Point(52.5 + n* 65, 10*m-10), q).draw(counted)

    for n in range(0,7):  # 25간격으로 바 생성, 세어진 빈도값을 y축에 표현
        x = n * 65
        height = freq[n]
        bar = Rectangle(Point(40 + x, 10*m-30), Point(65 + x, 10*m-30 - height * 10))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(counted)
    input("Press <Enter> to quit")
    counted.close()
    f.close()


# main 함수 호출
textcount()
