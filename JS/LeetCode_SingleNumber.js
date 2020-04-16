const singleNumber = (nums) => {
    let num = 0;
    nums.forEach(el => {
        if (nums.filter(e => e === el).length === 1){
            num = el
        }
    })
    return num
}

console.log(singleNumber([2,2,1]))
console.log(singleNumber([4,1,2,1,2]))