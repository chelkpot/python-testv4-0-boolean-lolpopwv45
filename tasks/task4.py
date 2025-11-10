def solve():
    a, b, c = map(int, input().split())
    print(a + b > c and a + c > b and b + c > a)

if __name__ == "__main__":
    solve()