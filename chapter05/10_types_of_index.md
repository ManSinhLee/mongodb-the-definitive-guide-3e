In MongoDB, there are various types of indexes to optimize query performance. Let's discuss some of them with real-world examples using the citizens collection.

1. Single Field Index:
   - This is the most basic type of index, where an index is created on a single field. It can be useful for fields commonly used in queries.

   Example:
   ```javascript
   db.citizens.createIndex({ lastName: 1 })
   ```
   This creates an ascending index on the `lastName` field.

2. Compound Index:
   - A compound index includes more than one field. It's useful when queries involve multiple fields.

   Example:
   ```javascript
   db.citizens.createIndex({ lastName: 1, dateOfBirth: -1 })
   ```
   This creates a compound index on `lastName` (ascending) and `dateOfBirth` (descending).

3. Multikey Index:
   - MongoDB automatically creates a multikey index when indexing an array field. This type of index is useful for queries that match elements in the array.

   Example:
   ```javascript
   db.citizens.createIndex({ "interests": 1 })
   ```
   This creates an index on the `interests` array.

4. Text Index:
   - Text indexes are designed for text search. They allow for more advanced text search capabilities.

   Example:
   ```javascript
   db.citizens.createIndex({ "$": "text" })
   ```
   This creates a text index that covers all fields in the collection.

5. Hashed Index:
   - Hashed indexes are suitable for equality queries but not range queries. They can be useful for random access to documents.

   Example:
   ```javascript
   db.citizens.createIndex({ socialSecurityNumber: "hashed" })
   ```
   This creates a hashed index on the `socialSecurityNumber` field.

6. Wildcard Index (Wildcard Indexes are Deprecated):
   - In MongoDB 4.2 and later, wildcard indexes can be used for queries on fields within embedded documents.

   Example:
   ```javascript
   db.citizens.createIndex({ "emergencyContact.*": 1 })
   ```
   This creates an index on all fields within the `emergencyContact` subdocument.
   Note: Wildcard Indexes are deprecated in MongoDB 4.2 and later. It's recommended to use individual field names instead.

7. Partial Index:
   - Partial indexes only index the documents in a collection that meet a specified filter expression. They are useful when only a subset of documents needs to be indexed.

   Example:
   ```javascript
   db.citizens.createIndex(
     { "votingHistory.registered": 1 },
     { partialFilterExpression: { "votingHistory.registered": true } }
   )
   ```

   This creates an index on the `registered` field within `votingHistory`, but only for documents where `registered` is `true`.

8. Unique Index:
   - Unique indexes ensure that the indexed fields do not store duplicate values. They are commonly used for fields that should have unique values, such as usernames or email addresses.

   Example:
   ```javascript
   db.citizens.createIndex({ "socialSecurityNumber": 1 }, { unique: true })
   ```

   This creates a unique index on the `socialSecurityNumber` field, ensuring that each SSN is unique in the collection.

9. TTL Index (Time-To-Live Index):
    - TTL indexes automatically expire documents after a specified amount of time, which is useful for collections that store data with a limited lifespan.

    Example:
    ```javascript
    db.citizens.createIndex({ "votingHistory.lastVoted": 1 }, { expireAfterSeconds: 2592000 })
    ```

    This creates a TTL index on the `lastVoted` field within `votingHistory`, and documents will expire (be deleted) 30 days after the value of `lastVoted`.

Remember to carefully consider your application's query patterns and requirements when choosing which indexes to create. Unnecessary indexes can have a negative impact on write performance and storage.   

Please note that the decision to create an index should be based on the specific queries your application performs. It's important to balance the benefits of indexing with the additional storage and update costs associated with maintaining indexes.