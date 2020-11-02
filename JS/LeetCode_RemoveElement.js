/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
   //input array
   //remove val
   //return array without val
   //O(1) extra memory
   while (nums.includes(val)){
      nums.splice(nums.indexOf(val),1)
   }
   return nums
};

console.log(removeElement([3,2,2,3], 3)) // 2
console.log(removeElement([0,1,2,2,3,0,4,2], 2)) // 5