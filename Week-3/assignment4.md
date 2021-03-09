## python 解法
```py
r = [2, 7, 3, 15,7]

def twoSum(data,target):
    for i in range(len(data)-1) :
        match_num = target - data[i]
        try :
            match_index = data.index(match_num)
            if match_index == i :
                del data[i]
                match_index = data.index(match_num)
                return[i,match_index+1]
            else:
                return [i,match_index]
        except:
            continue
    raise ValueError("do not have match result")
twoSum(r,14)
```
