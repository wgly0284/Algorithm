T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = input()

    my_dict = {
        'A':10,
        'B':11,
        'C':12,
        'D':13,
        'E':14,
        'F':15,
        'G':16
    }

    result = []
    for cha in arr:
        if cha.isalpha():
            result.append(my_dict[cha])
        if cha.isdigit():
            result.append(int(cha))

    final_sum = sum(result)

    print(f"#{tc} {final_sum}")