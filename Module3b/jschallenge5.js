function reverseArray(number) {
  const reversedArray = [];
  for (let i = number.length - 1; i >= 0; i--) {
    reversedArray.push(number[i]);
  }
  return reversedArray;
}


const originalArray = [1, 3, 5, 7, 9];
const reversedArray = reverseArray(originalArray);

console.log("Original Array:", originalArray);
console.log("Reversed Array:", reversedArray);
