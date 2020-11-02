var containsDuplicate = function(nums) {
    let i = 0;
    while (i < nums.length){
        console.log(nums.slice(i+1))
        i++
    }
    return false
};

console.log(containsDuplicate([1,2,3,1]))
console.log(containsDuplicate([1,2,3,4]))
console.log(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))