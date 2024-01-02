"""Day-16"""


def solver(n: int = 1000):
    """function to find sum of all the digits of 2^n"""
    total_product, ans = "2", 0
    for i in range(n - 1):
        next_number, current_remainder = "", 0
        index = len(total_product) - 1
        while index >= 0:
            temp = int(total_product[index]) * 2 + current_remainder
            if len(str(temp)) == 1:
                next_number = str(temp) + next_number
                current_remainder = 0
            else:
                next_number = str(temp % 10) + next_number
                current_remainder = temp // 10
            index -= 1
        if current_remainder:
            next_number = str(current_remainder) + next_number

        total_product = next_number

    for i in total_product:
        ans += int(i)
    return ans


if __name__ == "__main__":
    print(solver(15))
