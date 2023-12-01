


const numbersArray = [1, -1, -3, 0, -5, 4];

const filteredArray = numbersArray.filter(arrNegativeNumbers);
function arrNegativeNumbers(numbers){
    return numbers < 0
}

console.log("Original Array:", numbersArray);
console.log("Filtered Array (No Negative Numbers):", filteredArray);

