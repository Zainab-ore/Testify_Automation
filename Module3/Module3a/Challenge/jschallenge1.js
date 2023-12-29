function calculateSum(numbers) {
    
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum = sum + numbers[i];

  }
  return sum;
}


const numbers = [10, 20];


const total = calculateSum(numbers);

console.log("The sum of all the numbers is:", total);
