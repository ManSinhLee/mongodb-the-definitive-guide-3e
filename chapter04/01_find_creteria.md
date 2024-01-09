MongoDB provides a variety of query criteria operators that can be used to filter documents based on specific conditions. Here are some commonly used query criteria operators:

### 1. `$lt` (less than):

This operator selects documents where the value of a field is less than the specified value.

```javascript
db.users.find({ age: { $lt: 30 } })
```

This query will return users with an age less than 30.

### 2. `$lte` (less than or equal to):

This operator selects documents where the value of a field is less than or equal to the specified value.

```javascript
db.users.find({ age: { $lte: 30 } })
```

This query will return users with an age less than or equal to 30.

### 3. `$gt` (greater than):

This operator selects documents where the value of a field is greater than the specified value.

```javascript
db.users.find({ age: { $gt: 30 } })
```

This query will return users with an age greater than 30.

### 4. `$gte` (greater than or equal to):

This operator selects documents where the value of a field is greater than or equal to the specified value.

```javascript
db.users.find({ age: { $gte: 30 } })
```

This query will return users with an age greater than or equal to 30.

### 5. `$and` (logical AND):

This operator combines multiple conditions and selects documents that satisfy all the conditions.

```javascript
db.users.find({ $and: [{ age: { $gte: 25 } }, { age: { $lte: 35 } }] })
```

This query will return users with an age between 25 and 35.

### 6. `$or` (logical OR):

This operator selects documents that satisfy at least one of the specified conditions.

```javascript
db.users.find({ $or: [{ age: { $lt: 25 } }, { age: { $gt: 35 } }] })
```

This query will return users with an age less than 25 or greater than 35.

### 7. `$in` (in array):

This operator selects documents where the value of a field is in the specified array.

```javascript
db.users.find({ age: { $in: [25, 30, 35] } })
```

This query will return users with an age of 25, 30, or 35.

### 8. `$not` (logical NOT):

This operator selects documents that do not match the specified condition.

```javascript
db.users.find({ age: { $not: { $gt: 30 } } })
```

This query will return users with an age not greater than 30.

These examples demonstrate the use of various query criteria operators with the given user template. Adjust the field names and values as needed based on your actual MongoDB collection and data.