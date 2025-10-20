import sys

def solve():
    if hasattr(sys.stdin, "isatty") and sys.stdin.isatty():
        a, b, c = sorted(map(int, input("Введите три стороны: ").split()))
    else:
        a, b, c = sorted(map(int, input().split()))
    print(c * c == a * a + b * b)

if __name__ == "__main__":
    solve()