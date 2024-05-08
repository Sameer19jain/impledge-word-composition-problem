# impledge-word-composition-problem
Overview
This program, implemented in Python, is designed to identify compound words within a text file. Compound words are words formed by combining two or more separate words. The program utilizes a specialized data structure known as a trie to efficiently store and search for words in the text.

Execution Steps
Setup Environment: The Environment can be set up in, any of the IDE, which can be PyCharm or Visual Studio Code, I, personally have used Visual Studio Code to code this algorithm.
Downloading the Code: Get the Python script (test.py) and the input files (Input_01.txt) and (Input_02.txt) in the same directory.
Choosing the File you want your code to run on : There are two files,  (Input_01.txt) and (Input_02.txt) hence you can use any of the files over which the code can run, and you just have to, change the file_name ="", and write which ever file you want to run the algorithm on.
Run Program: Either you can, run directly from the VS Code or, open a terminal-> navigate to the directory-> and execute the code.

Program Overview
Word and WordStructure Classes:
The Word class represents a node in the trie data structure. Each node contains a dictionary of children nodes representing characters and a boolean flag indicating if it marks the end of a word.
The WordStructure class represents the trie structure itself. It contains methods for inserting words into the trie and finding suffixes of words.
Longest Word Function:
The longest_word function reads the input file line by line, splits each line into words, and inserts them into the trie structure.
It then iteratively finds compound words by checking for suffixes of each word in the trie.
The function returns the longest compound word, the second longest compound word, and the processing time in milliseconds.

Design Approach
Efficient Data Structure: The trie data structure is chosen for its efficiency in storing and searching for words, particularly for prefix-based searches like identifying compound words.
Algorithmic Strategy: A breadth-first search strategy is employed, using a queue to traverse the trie structure and identify compound words.
Optimization: The program aims to minimize processing time by efficiently organizing and searching through the trie structure.

Conclusion
This Python program offers a robust solution for identifying compound words within a text file. By leveraging a trie data structure and employing efficient algorithms, it delivers accurate results while minimizing computational overhead.
