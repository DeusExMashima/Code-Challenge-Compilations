// https://leetcode.com/problems/robot-return-to-origin/

//still working on it

/**
 * @param {string} moves
 * @return {boolean}
 *
 * Example 1:
 * Input: moves = "UD"
 * Output: true
 *
 * Example 2:
 * Input: moves = "LL"
 * Output: false
 *
 * Constraints - 1 <= moves.length <= 2 * 10^4
 * moves only contains the characters 'U', 'D', 'L' and 'R'.
 *
 */
var judgeCircle = function (moves) {
  let moveArray = moves.split("");
  let direction = {
    U: "D",
    D: "U",
    L: "R",
    R: "L",
  };
  let moveStack = [];
  console.log(moveArray);
  moveArray.forEach((move) => {
    console.log(moveStack);
    if (direction[move] === moveStack[-1]) {
      moveStack.pop();
    } else {
      moveStack.push(move);
    }
  });
  return moveStack.length === 0 ? true : false;
};

console.log(judgeCircle("UD"));
console.log(judgeCircle("LL"));
