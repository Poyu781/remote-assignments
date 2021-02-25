# 第一題
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num :
            max_num = num
    return max_num

print(find_max([5, 2, 7, 1, 6]))      


# 第二題
def find_position(numbers, target):
    index = -1 
    for num in numbers:
        index += 1
        if num == target:
            return index
    return -1
    
print(find_position([5, 2, 7, 1, 6], 8))