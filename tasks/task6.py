def solve():
    a, b, c = sorted(map(int, input().split()))
    print(c * c == a * a + b * b)

if __name__ == "__main__":
    solve()