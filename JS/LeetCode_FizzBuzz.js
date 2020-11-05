/*
https://leetcode.com/problems/fizz-buzz/

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.

Example
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

*/


/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {

    // looping over n
    let fizzBuzzArray = []
    for (let i = 1; i <= n ; i++){
        let modulo = (i % 15)
        switch(modulo){
            case 0:
                fizzBuzzArray.push("FizzBuzz")
                break
            case 5: case 10:
                fizzBuzzArray.push("Buzz")
                break
            case 3: case 6: case 9: case 12:
                fizzBuzzArray.push("Fizz")
                break
            default:
                fizzBuzzArray.push(i.toString())
                break
        }
    }
    return fizzBuzzArray
};

console.log(fizzBuzz(15))

/*
Runtime: 88 ms, faster than 39.19% of JavaScript online submissions for Fizz Buzz.
Memory Usage: 40.8 MB, less than 55.42% of JavaScript online submissions for Fizz Buzz.
Next challenges:
*/