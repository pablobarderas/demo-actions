def div (num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 0

if __name__ == "__main__":
    print(div(4,2))