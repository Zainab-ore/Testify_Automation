// Create an array of book objects
const books = [
    {
      title: "New General Mathematics",
      description: "Book 1 is a math textbook",
      numberOfPages: 5000,
      author: "Author 1",
      reading: false
    },
    {
      title: "Essential Physics",
      description: "Book 2 is a physics textbook",
      numberOfPages: 6000,
      author: "Author 2",
      reading: true
    },
    {
      title: "Use of English",
      description: "Book 3 is a english",
      numberOfPages: 7000,
      author: "Author 3",
      reading: false
    },
    {
      title: "Mordern Biology",
      description: "Book 4 is a biology textbook",
      numberOfPages: 8000,
      author: "Author 4",
      reading: false
    },
    
    {
      title: "Mordern chemistry",
      description: "Book 5 is a biology textbook",
      numberOfPages: 9000,
      author: "Author 5",
      reading: true
    }
  ];
  
  // Using a for-loop to log books with reading status set to true
  for (let i = 0; i < books.length; i++) {
    if (books[i].reading === true) {
      console.log("Book Title:" + books[i].title);
      console.log("Description:" + books[i].description);
      console.log("Number of Pages:" + books[i].numberOfPages);
      console.log("Author:" + books[i].author);
      console.log("Reading: Yes");
      console.log(" ");

    }
  }
  