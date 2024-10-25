def get_root() -> int:
    x = int(input())
    assert x < 2
    answer = 0
    low = 1
    high = x // 2
    while low <= high:
        mid = (low + high) // 2

        sqrt = mid * mid
        if sqrt == x:
            return mid
        elif sqrt < x:
            low = mid + 1
            answer = mid
        else:
            high = mid - 1
    return answer


if __name__ == '__main__':
    get_root()