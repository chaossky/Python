import random
from rich import print

def play():
    target = random.randint(1, 100)
    attempts = 0
    print("[bold cyan]숫자 맞추기 게임을 시작합니다![/bold cyan]")

    while True:
        guess = input("1~100 사이의 숫자를 입력하세요: ")
        attempts += 1

        try:
            guess = int(guess)
        except ValueError:
            print("[red]숫자를 입력해주세요.[/red]")
            continue

        if guess < target:
            print("[yellow]너무 작아요![/yellow]")
        elif guess > target:
            print("[yellow]너무 커요![/yellow]")
        else:
            print(f"[green]정답입니다! {attempts}번 만에 맞췄어요.[/green]")
            break

if __name__ == "__main__":
    play()
