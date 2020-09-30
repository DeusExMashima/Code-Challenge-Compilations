/**
 * @param {string[][]} paths
 * @return {string}
 * Example 1:
 * Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
 * Outpit: "Sao Paolo"
 *
 * Example 2:
 * Input: paths = [["B","C"],["D","B"],["C","A"]]
 * Outpit = A
 *
 *Example 3:
 *Input: paths = [["A","Z"]]
 * Output: "Z"
 */
var destCity = function (paths) {
  let start = [];
  let destination = null;
  paths.forEach((route) => {
    start.push(route[0]);
  });
  paths.forEach((route) => {
    if (!start.includes(route[1])) {
      destination = route[1];
    }
  });
  //O(2N) => O(N)
  return destination;
};

const path1 = [
  ["London", "New York"],
  ["New York", "Lima"],
  ["Lima", "Sao Paulo"],
];
const path2 = [
  ["B", "C"],
  ["D", "B"],
  ["C", "A"],
];
const path3 = [["A", "Z"]];

console.log(destCity(path1));
console.log(destCity(path2));
console.log(destCity(path3));
