def binary_search_position(numbers, target):
    first_index = 0
    last_index = len(numbers)
    middle_index = (first_index+last_index)//2
    while True:
        if numbers[middle_index] == target :
            return middle_index
        # 多加下行判斷式，來讓不存在的 List 的 Target 可以跳出迴圈
        elif first_index == middle_index or last_index == middle_index :
            return -1
        elif numbers[middle_index] > target :
            last_index = middle_index
            middle_index = (first_index+last_index)//2            
        elif numbers[middle_index] < target :
            first_index = middle_index
            middle_index = (first_index+last_index)//2