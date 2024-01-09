Index administration in MongoDB involves managing, monitoring, and maintaining indexes to ensure optimal performance. Here are some key aspects of index administration:

1. Viewing Existing Indexes:
   - To view existing indexes on a collection, you can use the `getIndexes()` method.
     ```javascript
     db.citizens.getIndexes()
     ```

2. Creating Indexes:
   - Use the `createIndex()` method to create new indexes.
     ```javascript
     // Example: Creating an index on the firstName field
     db.citizens.createIndex({ firstName: 1 })
     ```

3. Dropping Indexes:
   - Use the `dropIndex()` method to remove an index.
     ```javascript
     // Example: Dropping the index on the firstName field
     db.citizens.dropIndex({ firstName: 1 })
     ```

4. Dropping All Indexes:
   - The `dropIndexes()` method can be used to remove all indexes on a collection.
     ```javascript
     db.citizens.dropIndexes()
     ```

5. Index Statistics:
   - MongoDB provides a `collStats` command to view statistics about a collection, including index usage.
     ```javascript
     db.citizens.stats()
     ```

6. Index Size:
   - To check the size of indexes on a collection, you can use the `totalIndexSize` field in the output of `collStats`.
     ```javascript
     db.citizens.stats().totalIndexSize
     ```

7. Index Optimization:
   - Regularly review and optimize indexes based on query patterns. Consider using the `explain()` method to analyze query execution plans and index usage.

8. Background Index Creation:
   - By default, index creation in MongoDB blocks other operations on a collection. Use the `background` option to create indexes in the background.
     ```javascript
     db.citizens.createIndex({ lastName: 1 }, { background: true })
     ```

9. Index Prefixes:
   - MongoDB can use index prefixes to satisfy queries, so ensure that indexes cover the most common query patterns.

10. Index Intersection:
    - Starting from MongoDB 4.2, multiple indexes can be used to satisfy a query using index intersection.

11. Index Rebuild:
    - In some cases, it may be necessary to rebuild an index. This can be done by dropping and recreating the index or using the `reIndex()` method.

Remember that effective index administration involves a balance between query performance and the overhead of maintaining indexes during write operations. Regularly monitor and analyze the usage of indexes to ensure they align with the application's access patterns.