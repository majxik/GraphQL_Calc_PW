# GraphQL_Calc_PW
GraphQL Calculator Test Automation written with Playwright & PyTest
@author: Martin Maiksnar

This project is for demonstration of basic test automation skills on GraphQL Calculator running in local docker. 

Prerequisites:
calculator-frontend running on 3001
calculator-frontend running on 4000

To Run all the test: Run 'pytest' from terminal without specifying file names. Pytest will automatically discover all files prefixed with test_.
To Run particular test suits, run the following command: 'pytest test_multiply.py test_addition.py'