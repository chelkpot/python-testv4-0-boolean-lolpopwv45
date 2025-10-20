import sys

def solve():
    if hasattr(sys.stdin, "isatty") and sys.stdin.isatty():
        a, b, c = map(int, input("Введите три числа: ").split())
    else:
        a, b, c = map(int, input().split())
    print(a == b == c)

if __name__ == "__main__":
    solve()