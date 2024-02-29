import random

rspgame = ['묵', '찌', '빠']

win = 0 #승리 기록
lose = 0 #패배 기록
drow = 0 # 무승부 기록
while True:
    yn = input("게임을 시작하시겠습니까 ?: [Y/N]")
    if yn.lower() == "y": #소문자 대문자 가능하게 변경
        while True:
            answer = input("안내면 진다 묵!찌!빠!: ")
            com_choice = random.choice(rspgame) #컴퓨터에게 랜덤으로 선택하게 하기      
            if (answer == "찌" and com_choice == "빠") or (answer == "묵" and com_choice == "찌") or answer == "빠" and com_choice == "묵":
                print(f"사용자: {answer} vs 컴퓨터: {com_choice} 이겼습니다.")
                print('- ' * 40)
                win += 1
            elif (answer == "찌" and com_choice == "묵") or (answer == "묵" and com_choice == "빠") or answer == "빠" and com_choice == "찌":
                print(f"사용자: {answer} vs 컴퓨터: {com_choice} 졌습니다.")
                print('- ' * 40)
                lose += 1
            elif answer ==  com_choice:
                print(f"사용자: {answer} vs 컴퓨터: {com_choice} 비겼습니다.")
                print('- ' * 40)
                drow += 1
            else:
                print("묵, 찌, 빠 중에 선택하세요.")
                print('- ' * 40)
                continue
            ans = input("한판 더? 종료하려면'N' / 계속하시려면 아무키나 누르세요: ") # 다시 플레이할지 선택
            # if ans.lower() == "y":
            #     continue
            if ans.lower() == "n":
                print(f'{win}승-{drow}무-{lose}패 하셨습니다')
                print("게임을 종료합니다.")
                print('- ' * 40)
                break
            else:
                continue
            # else:
            #     print("잘못 입력하셨습니다 [Y/N]중에 입력하세요")

    elif yn.lower() == "n":
        print("게임을 종료합니다")
        print('- ' * 20)
        break
    else:
        print("잘못 입력하셨습니다.")
        print('- ' * 20)
        continue