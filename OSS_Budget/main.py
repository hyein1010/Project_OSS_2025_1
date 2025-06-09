import os
from budget import Budget


def load_password():
    if not os.path.exists("password.txt"):
        return None
    with open("password.txt", "r") as f:
        return f.read().strip()


def save_password(password):
    with open("password.txt", "w") as f:
        f.write(password)


def check_password():
    stored = load_password()
    if stored is None:
        print("처음 사용하시는군요! 비밀번호를 설정해주세요.")
        new_pw = input("새 비밀번호: ")
        save_password(new_pw)
        print("비밀번호가 설정되었습니다.\n")
    else:
        for _ in range(3):
            pw = input("비밀번호를 입력하세요: ")
            if pw == stored:
                print("접속 성공!\n")
                return True
            else:
                print("비밀번호가 틀렸습니다.")
        print("비밀번호 입력 3회 실패. 프로그램을 종료합니다.")
        exit()


def change_password():
    current_pw = input("현재 비밀번호: ")
    if current_pw != load_password():
        print("비밀번호가 틀렸습니다.\n")
        return
    new_pw = input("새 비밀번호: ")
    save_password(new_pw)
    print("비밀번호가 변경되었습니다.\n")


def main():
    check_password()
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 수입 추가")
        print("3. 전체 내역 보기 (색상 표시)")
        print("4. 총 수입/지출/잔액 보기")
        print("5. 비밀번호 변경")
        print("6. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            category = input("카테고리 (예: 월급, 용돈 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_income(category, description, amount)

        elif choice == "3":
            budget.list_transactions()

        elif choice == "4":
            budget.total_summary()

        elif choice == "5":
            change_password()

        elif choice == "6":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()