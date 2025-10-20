import sys

def solve():
    if hasattr(sys.stdin, "isatty") and sys.stdin.isatty():
        a, b, c = map(int, input("Введите a b c: ").split())
    else:
        a, b, c = map(int, input().split())
    print(a + b > c and a + c > b and b + c > a)

if __name__ == "__main__":
    solve()