const books = {
    title: "Star Wars",
    description: "A novel about the Epic space battles involving fleets of ships and jedi",
    numberOfPages: 9990,
    author: "Author X",
    reading: true,
    toggleReadingStatus: function () {
      this.reading = ! this.reading; // Toggle the reading status
      console.log(`Reading status for "${this.title}" is now ${this.reading ? 'in progress' : 'not started'}.`);
    }
  };
  
 
  console.log(`Initial reading status: ${books.reading ? 'started' : 'not started'}`);
  books.toggleReadingStatus();
  console.log(`Updated reading status: ${books.reading ? 'started' : 'not started'}`);
  