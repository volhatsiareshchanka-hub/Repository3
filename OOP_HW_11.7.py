# 7. Парсер числа из строки

def parse_int_list(strings):
    int_list = []
    for value in strings:
        try:
            int_list.append(int(value))
        except ValueError:
            print(f"Warning: {value}")
    return int_list

raw = ["10", "20", "abc", "30", "4.5", "40"]
nums = parse_int_list(raw)
print(nums)  # [10, 20, 30, 40]

