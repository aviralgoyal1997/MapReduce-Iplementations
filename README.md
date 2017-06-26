# MapReduce-Iplementations
Problem 2

Create an Inverted index. Given a set of documents, an inverted index is a dictionary where each word is associated with a list of the document identifiers in which that word appears. Mapper Input

The input is a 2-element list: [document_id, text], where document_id is a string representing a document identifier and text is a string representing the text of the document. The document text may have words in upper or lower case and may contain punctuation. You should treat each token as if it was a valid word; that is, you can just use value.split() to tokenize the string. Reducer Output

The output should be a (word, document ID list) tuple where word is a String and document ID list is a list of Strings.

You can test your solution to this problem using books.json:

 python inverted_index.py books.json
You can verify your solution against inverted_index.json.

Problem 3

Implement a relational join as a MapReduce query

Consider the following query:

SELECT * FROM Orders, LineItem WHERE Order.order_id = LineItem.order_id

Your MapReduce query should produce the same result as this SQL query executed against an appropriate database.

You can consider the two input tables, Order and LineItem, as one big concatenated bag of records that will be processed by the map function record by record. Map Input

Each input record is a list of strings representing a tuple in the database. Each list element corresponds to a different attribute of the table

The first item (index 0) in each record is a string that identifies the table the record originates from. This field has two possible values:

"line_item" indicates that the record is a line item.
"order" indicates that the record is an order.
The second element (index 1) in each record is the order_id.

LineItem records have 17 attributes including the identifier string.

Order records have 10 elements including the identifier string. Reduce Output

The output should be a joined record: a single list of length 27 that contains the attributes from the order record followed by the fields from the line item record. Each list element should be a string.

You can test your solution to this problem using records.json:

$ python join.py records.json

You can can compare your solution with join.json.

Problem 4

Consider a simple social network dataset consisting of a set of key-value pairs (person, friend) representing a friend relationship between two people. Describe a MapReduce algorithm to count the number of friends for each person. Map Input

Each input record is a 2 element list [personA, personB] where personA is a string representing the name of a person and personB is a string representing the name of one of personA's friends. Note that it may or may not be the case that the personA is a friend of personB. Reduce Output

The output should be a pair (person, friend_count) where person is a string and friend_count is an integer indicating the number of friends associated with person.

You can test your solution to this problem using friends.json:

$ python friend_count.py friends.json

You can verify your solution by comparing your result with the file friend_count.json. 
Problem 5
The relationship "friend" is often symmetric, meaning that if I am your friend, you are my friend. Implement a MapReduce algorithm to check whether this property holds. Generate a list of all non-symmetric friend relationships. Map Input

Each input record is a 2 element list [personA, personB] where personA is a string representing the name of a person and personB is a string representing the name of one of personA's friends. Note that it may or may not be the case that the personA is a friend of personB. Reduce Output

The output should be all pairs (friend, person) such that (person, friend) appears in the dataset but (friend, person) does not.

You can test your solution to this problem using friends.json:

$ python asymmetric_friendships.py friends.json
