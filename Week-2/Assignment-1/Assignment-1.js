function max(numbers){
    let max_num = numbers[0]
    for(let i of numbers){
        if (i > max_num){
            max_num = i;
        }
    }
    return max_num
}

function findPosition(numbers,target){
    for(let i=0; i<numbers.length; i++){

        if (numbers[i] === target){
            return i
        }
        else if(i == numbers.length-1){
            return -1
        }           
    }    
}





