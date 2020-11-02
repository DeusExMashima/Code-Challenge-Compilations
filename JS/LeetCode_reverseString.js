function reverse(str) {
    reversed = "";
    for (let character of str) {
      reversed = character + reversed;
    }
    return reversed;
}

console.log(reverse("Josh"))