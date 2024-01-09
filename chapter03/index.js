// index.js

const faker = require('faker');

// Function to generate random data for each document
const generateRandomUserData = () => {
  return {
    username: faker.internet.userName(),
    age: faker.datatype.number({ min: 18, max: 80 }),
    email: faker.internet.email(),
    registered: faker.date.past(),
    fatal_weakness: faker.random.words(),
    user_id: faker.datatype.number(),
    id_num: faker.datatype.number(),
    name: faker.name.findName(),
    favorite_books: [faker.random.word(), faker.random.word(), faker.random.word()],
    address: {
      street: faker.address.streetAddress(),
      city: faker.address.city(),
      state: faker.address.state(),
      zip: faker.address.zipCode(),
    },
  };
};

// Generate and print random user data


const randomUserData = generateRandomUserData();
console.log(JSON.stringify(randomUserData, null, 2));
