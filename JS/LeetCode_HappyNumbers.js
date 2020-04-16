const isHappy = (n) => {
    let happy = n
    let digits = happy.toString().split('')
    while (digits.length > 1) {
        digits = digits.map(el => {
            parseInt(el)
            return el * el
        })
        happy = digits.reduce((acc,nm) => acc + nm)
        digits = happy.toString().split('')
        console.log(digits)
    }
    if (happy === 1 || happy === 7) {
        return true
    } else {
        return false
    }
}

console.log(3%2)
console.log(isHappy(3))
console.log(isHappy(7))
console.log(isHappy(19))
console.log(isHappy(4))
console.log(isHappy(25))