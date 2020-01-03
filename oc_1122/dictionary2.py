menu = {"라면": 4000, "만두": 3500, "보쌈": 28000}
while True:
    choice= input("메뉴를 입력하세요 : ")

    if choice in menu:
        price = menu[choice]
        print(choice + "는 " + str(price) + "원 입니다.")
    else:
        print(choice + " 메뉴는 없습니다")