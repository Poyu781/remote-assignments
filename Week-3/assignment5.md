## Assignment 5
以下是我第一時間想出的解法，我在程式中只使用了一次迴圈，因此我認為這樣的運算時間複雜度為 O(n)，因為運算時間會隨著 input 的大小而改變。
空間複雜度則為 O(1)，因為除了 input 以外，我沒有再使用任何新的記憶體來存儲資料。

```py
## 方法一
def twoSum(data,target):
    for i in range(len(data)-1) :
        match_num = target - data[i]
        try :
            match_index = data.index(match_num)
            ## 如果 List 沒有重複的值，則不需要此判斷式
            if match_index == i :
            ## index 會找出第一個匹配值的位置，所以如果 i 跟 match_index 一樣，則表示 Target-match_num == search__num
                del data[i]
                match_index = data.index(match_num)
                return[i,match_index+1]
            else:
                return [i,match_index]
        except:
            continue
    raise ValueError("do not have match result")

```
後來去學了一個新的寫法，概念跟我原本的寫法很像，但簡化很多，因為是用 dict 方式去看是否配對成功，所以可以省去判斷 match_num == search__num 的情況。
這樣的寫法，時間複雜度為 O(n)，但為了存取 numMap ，空間複雜度則為 O(n)。


```py
## 方法二
def twoSum(nums: 'List[int]', target: 'int') -> 'List[int]':
    num＿map = {}
    for i in range(len(nums)):
        x =target-nums[i]
        if x in num_map:
            return [numMap[target-nums[i]], i]
        else:
            num_map[nums[i]] = i
```

### 反思：
雖然這兩個寫法，在我的理解中，都是時間複雜度 O(n) 的寫法，但在執行非常大的 input 時，方法一的 Step 還是比 <方法二> 多，執行時間也有差距。

在問了朋友之後，現在理解運行時間會有差異，主要是因為 <方法一> 中用了兩次 `index()` ，雖然在 python 中只用了一個迴圈，但每次執行 `index()` 時，都在 C 語言上跑了一次迴圈去找出其 index，不過因為 C 語言是更底層的語言，所以執行效率會比較快，在計算時間複雜度時，可以先忽略不計?（還有待老師解惑）

##### 備註：
在 data 大約在 800 個 index 的情況下，此兩種方法的執行速度，大概差了 **0.0079643726 seconds** ，

在有 1300 個 index 時，則差了 **0.0191178322 seconds** ，代表當 data 的 index 極大時，這兩個 function 執行效率應該還是差多的？不過以 <方法一> 計算的話，就能更省空間吧，因為不用再存一個 dict 去配對。