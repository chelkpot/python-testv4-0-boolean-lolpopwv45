import sys

def solve():
    if hasattr(sys.stdin, "isatty") and sys.stdin.isatty():
        w1 = input("Введите первое слово: ").strip()
        w2 = input("Введите второе слово: ").strip()
    else:
        w1 = input().strip()
        w2 = input().strip()
    print(w1 == "awesome" or w2 == "awesome")

if __name__ == "__main__":
    solve()