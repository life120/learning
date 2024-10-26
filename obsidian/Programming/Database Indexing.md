What is Database Indexing?
Indexing in the database is the way to get an unordered table into an order that will maximize the query's efficiency while searching. 

Context
When a user sends a query to a database, what happens is that the program will search through all the rows in the database of the column to check if that particular column meets the query before the action is complete. This is not suitable if the number of rows grows exponentially. There is a need to optimize the query performance so that you can return the results in the least amount of time required.
![[Pasted image 20240821100553.png]]
How does indexing work?
Indexing is done on a column. To index a column, the database will create a data structure on a specific column. For all variation values in the column, the database will arrange the values in ascending/descending order and will store the 'pointer' or 'home address' on the memory disk. 
When you want to index a column, the database will create a new table
![[Pasted image 20240821101047.png]]
In this example, if I am querying to retrieve the results where the company_id = 18, the database will look through the index table, will go to the first row that contains the company_id of 18, and then will iterate through the next few rows until the company_id value changes to 19, and then it will stop querying and return the results. So instead of searching through all 17 rows (in this example) to find the matching query, it will only need to read through 4 rows only. 
Resources
https://www.atlassian.com/data/databases/how-does-indexing-work