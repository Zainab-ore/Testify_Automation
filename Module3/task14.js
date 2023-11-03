const books = {
    title: "Star Wars",
    description: "A novel about the Epic space battles involving fleets of ships and jedi",
    numberOfPages: 9990,
    author: "Author X",
    reading: true,

    toggleReadingStatus: function () 
    {
     if(books.reading===true)
     {
      books.reading===false;
     }
    }
  };
  
  books.toggleReadingStatus();

  console.log("The status, of my book reading is currently: " + books.reading + " :for a reading status");
  

  