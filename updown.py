# import random


# def newgame():
#     while True:
#         yn = input("게임을 시작하시겠습니까 ?: [Y/N]")
#         if yn.lower() == "y":
#             updown()  # 게임 함수 호출
#         elif yn.lower() == "n":
#             print("게임을 종료합니다")
#             break  # 함수 종료
#         else:
#             print("잘못 입력하셨습니다.")


# def updown():  # 게임 함수
#     random_number = random.randint(1, 100)  # 무작위 번호 생성
#     count = 0
#     while True:
#         try:
#             answer = int(input("숫자를 입력하세요: "))
#             if answer < 1 or answer > 100:
#                 print("1부터 100 사이의 숫자만 입력하세요.")
#                 continue  # 다시 반복문의 처음으로 돌아감
#             if answer == random_number:  # 입력한 숫자와 비교y
#                 print("정답입니다.^^")
#                 print(f'시도횟수 {count} 번')
#                 break  # 함수 종료
#             elif answer > random_number:
#                 print("down")
#             else:
#                 print("up")
#             count += 1
#         except ValueError:
#             print("숫자만 입력가능합니다.")


# newgame()


import random


record = []  # 기록을 리스트에 추가


def bestrecord():  # 최고기록을 기록하기 위한 함수
    if not record:
        record.append(count)
        record.sort()  # 기록을 낮은 시도횟수 부터 정렬
    elif count < record[0]:
        record.append(count)
        record.sort()


while True:
    random_number = random.randint(1, 100)  # 무작위 번호 생성
    count = 0
    yn = input("게임을 시작하시겠습니까 ?: [Y/N]")
    if yn.lower() == "y":
        while True:
            answer = int(input("숫자를 입력하세요: "))
            if answer < 1 or answer > 100:
                print("1부터 100 사이의 숫자만 입력하세요.")
                continue  # 다시 반복문의 처음으로 돌아감
            if answer == random_number:  # 입력한 숫자와 비교
                print("정답입니다.^^")
                print(f'시도횟수 {count} 번')
                bestrecord()
                print(f'최고 기록은 {record[0]}입니다')  # 가장 낮은 기록 출력
                break  # 함수 종료
            elif answer > random_number:
                print("down")
                count += 1
                continue
            elif answer < random_number:
                print("up")
                count += 1
                continue
    elif yn.lower() == "n":
        print("게임을 종료합니다")
        break  # 함수 종료
    else:
        print("잘못 입력하셨습니다.")
        continue
