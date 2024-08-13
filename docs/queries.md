# Queries
Queries to the database are made in JSON format. The following operators are supported:

- `$eq`: Matches documents where the value of a field equals the specified value.
- `$gt`: Matches documents where the value of a field is greater than the specified value.
- `$gte`: Matches documents where the value of a field is greater than or equal to the specified value.
- `$lt`: Matches documents where the value of a field is less than the specified value.
- `$lte`: Matches documents where the value of a field is less than or equal to the specified value.
- `$ne`: Matches documents where the value of a field does not equal the specified value.
- `$in`: Matches any of the values specified in an array.
- `$nin`: Matches none of the values specified in an array.
- `$exists`: Matches documents where the specified field exists.
- `$regex`: Matches documents where the value of a field matches a regular expression.
- `$and`: Joins query clauses with a logical AND.
- `$or`: Joins query clauses with a logical OR.
- `$not`: Inverts the effect of a query expression.
- `$nor`: Joins query clauses with a logical NOR.

If no operator is specified for a value in a query, the `$eq` operator is assumed. For example, the query `{"name": "Alice"}` is equivalent to `{"name": {"$eq": "Alice"}}`.
Logical operators only support two operands. To combine more than two operands, you can nest logical operators.

Here are some examples of queries:

- Fetch documents where the `name` field is equal to "Alice": `{"name": "Alice"}`
- Fetch documents where the `age` field is greater than 18: `{"age": {"$gt": 18}}`
- Fetch documents where the `name` field is equal to "Alice" and the `age` field is greater than 18: `{"$and": [{"name": "Alice"}, {"age": {"$gt": 18}}]}`
- Fetch documents where the `name` field is equal to "Alice" or the `age` field is greater than 18: `{"$or": [{"name": "Alice"}, {"age": {"$gt": 18}}]}`
- Fetch documents where the `name` field is not equal to "Alice": `{"name": {"$ne": "Alice"}}`
- Fetch documents where the `name` field does not exist: `{"name": {"$exists": false}}`
- Fetch documents where the `name` field matches the regular expression `/^A/`: `{"name": {"$regex": "^A"}}`