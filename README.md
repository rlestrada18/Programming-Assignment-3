# Programming-Assignment-3
Problem 1

1. I started by importing the pandas library since it’s the standard tool for handling CSV data.

2. I loaded the dataset file cars.csv into a DataFrame named cars using pd.read_csv().

3. To check that the dataset was correctly loaded and to get familiar with its structure, I displayed the first five rows using cars.head().

4. I also displayed the last five rows using cars.tail() to make sure I could see both the beginning and end of the dataset.

5. I saved my script into a file named Estrada_Pandas-P1.py using the %%writefile command in Jupyter Notebook.

6. I ran the script in a separate cell using %run Estrada_Pandas-P1.py to verify that the outputs matched the requirements.

7. The result confirmed that the dataset loaded properly, and I was able to inspect both ends of the table as required.

Problem 2

1. I started by importing pandas and loading the dataset cars.csv into a DataFrame named cars.

2. I focused on using subsetting, slicing, and indexing operations as required in the problem.

3. For part (a), I displayed the first five rows but only odd-numbered columns by applying slicing with iloc.

4. For part (b), I extracted the row that contains the model “Mazda RX4” using Boolean indexing.

5. For part (c), I checked how many cylinders (cyl) the model “Camaro Z28” has by filtering the row and selecting the cyl column.

6. For part (d), I displayed both the cylinders and gear type for the models:

Mazda RX4 Wag

Ford Pantera L

Honda Civic

7. by using .isin() to filter multiple rows and selecting only the necessary columns.

8. I saved my script into a file named Estrada_Pandas-P2.py using %%writefile in Jupyter Notebook.

9. Just like Problem 1, I ran the script using %run Estrada_Pandas-P2.py to confirm that the outputs were correct.

10. The results matched the requirements and showed the correct rows and values for each question.
