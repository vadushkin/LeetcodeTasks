class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        i factorial:

        1:  1  - 0
        2:  2  - 0
        3:  6  - 0
        4:  24  - 0
        5:  120  - 1
        6:  720  - 1
        7:  5040  - 1
        8:  40320  - 1
        9:  362880  - 1
        10: 3628800  - 2
        11: 39916800  - 2
        12: 479001600  - 2
        13: 6227020800  - 2
        14: 87178291200  - 2
        15: 1307674368000  - 3
        16: 20922789888000  - 3
        17: 355687428096000  - 3
        18: 6402373705728000  - 3
        19: 121645100408832000  - 3
        20: 2432902008176640000  - 4
        21: 51090942171709440000  - 4
        22: 1124000727777607680000  - 4
        23: 25852016738884976640000  - 4
        24: 620448401733239439360000  - 5
        ...
        """

        cur = 5
        res = 0

        while cur <= n:
            res += n // cur
            cur *= 5

        return res


def main():
    s = Solution()
    print(s.trailingZeroes(10))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 43 ms Beats 84.88%
   Memory 13.9 MB Beats 61.81%

2. Runtime 65 ms Beats 50.49%
   Memory 13.7 MB Beats 99.80%
"""
