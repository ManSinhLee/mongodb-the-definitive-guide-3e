Must learn: python, golang, javascript, java

// Function to generate random status
const getRandomStatus = () => {
  const statuses = ['READY', 'RUNNING', 'DONE'];
  const randomIndex = Math.floor(Math.random() * statuses.length);
  return statuses[randomIndex];
};

// Function to generate random priority (integer between 1 and 10)
const getRandomPriority = () => Math.floor(Math.random() * 10) + 1;

// Function to generate 10 documents
const generateDocuments = () => {
  const documents = [];

  for (let i = 0; i < 10; i++) {
    const document = {
      _id: ObjectId(),
      status: getRandomStatus(),
      priority: getRandomPriority()
    };

    documents.push(document);
  }

  return documents;
};

// Insert the generated documents into the collection
db.processes.insertMany(generateDocuments());

// Display the inserted documents
db.processes.find().pretty();


db.users.insertOne(  {
    username: 'Annie',
    age: 26,
    email: 'annie@abc.com',
    favorite_books: [ 'To Kill a Mockingbird', '1984', 'Pride and Prejudice' ],
    registered: ISODate('2023-12-20T03:33:55.679Z')
  })