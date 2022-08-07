# HackBackpackers_AshwinRaja
Problem Statements
Problem Statement 1 - Lineage problem statement
# Description
It is required to fetch the table and column(metadata) of the SQL query that would be input to the program

# Prerequisite
I have used the GCP Big Query Console to input data, and execute a query that fetches the table and column details from query.

# How to run

Steps
1. Import the emp_sal and emp_det csv files into a big query table. It was done via console and CSV files were uploaded.
2. Based on the 3 parameters, both input tables and a template SQL query, we need to run a query.
3. Query is attached working_query.sql, which needs to executed on Big Query console.

# Any other points to mention
None
Problem Statement 2 - Functions problem statement
# Description
We need to convert the existing data stage functions into ADF functions. The output should return the same output as Datastage. But we need to use only ADF functions.

# Prerequisite
NA

# How to run

Steps
1. As I do not have ADF , I have written the function in a text file "adf_funtions.txt"
2. Please open the file and run the fuctions one by one in ADF

# Any other points to mention
NA

Problem Statement 3 - XML problem statement
# Description
The approach is to :
  - Parse data from xml file using Python.
  - Search for the Tags - TRANSFORMATION, INSTANCE. This will give the immediate flow of data from one stage to another.
  - The individual tags are checked, and text between tags is loaded to a variable.
  - Search for field name in the variables i.e variable for TRANSFORMATION and variable for INSTANCE.
  - If it returns a match print the source and target field names.

# Prerequisite
Big Query, Python

# How to run
<Write steps to run your solution>
Steps
1. Execute the script "Problem_Statement_3_WF_Extract.py". 
2. Ensure that the xml file is placed in same location.
  

# Any other points to mention
  None
