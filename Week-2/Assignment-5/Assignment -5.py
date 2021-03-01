def binary_search_position(numbers, target):
    first_index = 0
    last_index = len(numbers)
    middle_index = (first_index+last_index)//2
    while True:
        # 找到符合 Target 的 index 後，再持續往前去看有沒有相等的數字，來找到符合資格的最小 idex
        if numbers[middle_index] == target :
            for i in range(middle_index): 
            #應該有更好的迴圈設法，但我現階段用 middle_index 的 Range ，是確保一定能更找到 index 0
                middle_index -= 1
                if numbers[middle_index] == target :
                    continue
                else :
                    middle_index = middle_index + 1
            return middle_index
        # 當找不到 target 的時候，會從左右兩邊來判斷，哪邊最接近取哪邊，若相等則取較小 index 的
        elif first_index == middle_index or last_index == middle_index :
            if numbers[first_index]-target > target-numbers[last_index]:
                return last_index
            else:
                return first_index
        elif numbers[middle_index] > target :
            last_index = middle_index
            middle_index = (first_index+last_index)//2            
        elif numbers[middle_index] < target :
            first_index = middle_index
            middle_index = (first_index+last_index)//2
