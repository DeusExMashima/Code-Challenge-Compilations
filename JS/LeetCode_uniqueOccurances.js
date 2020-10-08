//https://leetcode.com/problems/unique-number-of-occurrences/

/**
 * 
 * @param {number[]} arr
 * @return {boolean}
 * 
 * 
 */
var uniqueOccurrences = function (arr) {
    //every time we check a number, we count its occurance and store it in hash table
    //after that we check hash table for unique number
    occuranceCount = {}
    arr.forEach(number => {
        if (number in occuranceCount) {
            occuranceCount[number]++
        } else {
            occuranceCount[number] = 1
        }
    })
    let result = false
    let values = Object.values(occuranceCount)
    let newValues = [...new Set(values)]
    if (newValues.length === values.length) {
        return true
    }
    return result
};

const array1 = [1, 2, 2, 1, 1, 3]
const array2 = [1, 2]
const array3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]

console.log(uniqueOccurrences(array1)) //true
// 1 appears 3 times, 2 appears 2 times, and 3 appears 1 time

console.log(uniqueOccurrences(array2)) //false
// 1 appear 1 time, 2 only appear 1 time, so these numbers are not unique

console.log(uniqueOccurrences(array3)) // true