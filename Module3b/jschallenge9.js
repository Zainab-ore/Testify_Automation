function vowelsCount(letters) {
  const vowels = "aeiouAEIOU";
  let counts = 0;

  for (let i=0; i< letters.length; i++) {
    if (vowels.includes(letters[i])) {
      counts++;
    }
  }

  return counts;
}


const sampleLetter = "MATHEMATICS";
console.log("Number of vowels in " +sampleLetter+ " is " +vowelsCount(sampleLetter));
