import sys

def solve():
    if hasattr(sys.stdin, "isatty") and sys.stdin.isatty():
        n = int(input("Введите число: "))
    else:
        n = int(input())
    print(10 <= n <= 99)

if __name__ == "__main__":
    solve()