# 原始寫法
def binary_search_position(numbers, target):
    first_index = 0
    last_index = len(numbers)-1  # 原本為 len(numbers) ，後修改 -1 ，確保 last_index 不會超出 numbers 範圍
    middle_index = (first_index+last_index)//2
    while True:
        # 找到符合 Target 的 index 後，再持續往前去看有沒有相等的數字，來找到符合資格的最小 index
        if numbers[middle_index] == target :
            for i in range(middle_index): 
            #應該有更好的迴圈設法，但我現階段用 middle_index 的 Range ，是確保一定能更找到 index 0
                middle_index -= 1
                if numbers[middle_index] == target :
                    continue
                else :
                    middle_index = middle_index + 1
                    return middle_index
        elif target > numbers[len(numbers)-1] :
            return len(numbers)
        # 當找不到 target 的時候，會從左右兩邊來判斷，哪邊最接近取哪邊，若相等則取較小 index 的
        elif first_index == middle_index or last_index == middle_index :
            if target - numbers[first_index] > numbers[last_index] - target:
                return last_index
            else:
                return first_index
        elif numbers[middle_index] > target :
            last_index = middle_index
            middle_index = (first_index+last_index)//2            
        elif numbers[middle_index] < target :
            first_index = middle_index
            middle_index = (first_index+last_index)//2

# 參照 bisect_left 的方式去仿寫

def binary_search_first(numbers, target, start_index=0, last_index=None):
    if start_index < 0:
        raise ValueError('start_index must be non-negative')
    if last_index is None:
        last_index = len(numbers)

    while start_index < last_index:
        mid = (start_index + last_index) // 2
        if numbers[mid] < target:
            start_index = mid + 1
        else:
            last_index = mid 

    return start_index