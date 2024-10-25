#  В качестве исходного кода был выбран поиск квадратного корня
class Root:
    @staticmethod
    def get_root(x: int) -> int:
        assert x > 2
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
    print(type(Root.get_root(12)))
