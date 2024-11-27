> COMP 424 Applied Computing: **Homework 4, Week 13**

### Purpose
- Gain more practice object-orientation and processing files.
- Use test-driven incremental development to document, test, design, implement, and debug functions
- Use and analyze real data. In this homework, we use Kiva Lending Data. See more information 
at https://runestone.academy/ns/books/published/COMP424M1/Projects/kiva_statistics.html in the
Runestone textbook. 


### Guidelines
#### Read
- Read the docstrings and the code in the `kivastats.py` module. What does it contain? 
- Read the docstrings and the code the `test_kivastats.py` module. What does it contain?
- Check code analysis and style warning and errors
  - Fix them, if you find fixable errors at this examination step.
- Examine the content of all text files (extension `.csv`, comma-separated-values text files)
- Discuss and clarify in class:
  - What problems do the instance methods in `KivaStats` class address?
  - How does the testing work and how do you run the program?
  - What other questions do you have?

#### Document
- Document the docstrings of both Pyhton files by writing your name as developer. 
- Document the `DESIGN.md` file with your name. 

#### Incremental Development
- **Test**: in `test_kivastats.py`
  - Write the code of the testing functions as instructed in the docstring of each `kivastats.py` function. . 

- **Design**: in `DESIGN.md`
- Write the algorithmic steps that solve the problem for each of the instance methods in the  `KivaStats` class.

- **Implement and debug**: In `kivastats.py`
  - Write the implementation of each instance method in the `KivaStats` class based on the design. 

  ### Evaluation
- Documentation: 9%
  - 3% for each module docstring
  - 3% for `DESIGN.md`
- Testing: 36%
    - There are 5 testing functions, with different nunmber of test cases (12 tests cases total, 3% per test case)
    - Testing of the first three methods require 3 test cases (using the 3 .CSV files): `total_loan()`, `avg_lenders()`, and `smallest_loan_country()`
    - Testing of `time_per_dollar()` has 2 tests cases (using `data_1.csv` and `data_5.csv`)
    - Testing of `write_data()` has 1 test case (using `data_25.csv`)
- Design: 35%, 7% for each function
- Implementation: 10%, 2% for each function
- Code analysis and tyling: 10%

### Submission
#### GitHub
- Use the `Add File --> Upload` and choose your local files for uploading:
  - `kivastats.py`
  - `test_kivastats.py`
  - `DESIGN.md`
  - All three CSV files
- Upload ONLY the files, do NOT upload the entire `h4` directory.

#### Canvas
- Upload to the submission link the PDF of `DESIGN.md`
