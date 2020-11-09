/*

https://leetcode.com/problems/ugly-number/

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Note: 
1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−231,  231 − 1].
*/

/**
 * @param {number} num
 * @return {boolean}
 * 
 * Example 1:
 *      Input: 6
 *      Output: true
 *     
 * Example 2:
 *      Input: 8
 *      Output: true
 * 
 * Example 3:
 *      Input: 14
 *      Output: false
 */
var isUgly = function(num) {

    // while (num % 2 == 0 || num % 3 == 0 || num %5 == 0) {
    //     if (num % 5 == 0){
    //         num = num /5
    //     } if (num % 3 == 0){
    //         num = num /3
    //     } if (num % 2 == 0){
    //         num = num /2
    //     }      
    // }
    // return num === 1
    if (num === 1){ return true }
    if (num % 5 == 0){
          return isUgly(num / 5)
      } if (num % 3 == 0){
          return isUgly(num / 3)
      } if (num % 2 == 0){
          return isUgly(num / 2)
      }      
};

console.log(isUgly(-1))
console.log(isUgly(32))