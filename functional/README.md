# Functional Test 
In this session the objective is to verify functional requirements, functions and use cases by answering the question 
"does the application do what it should do?"

Given the characteristics of the api analyzed, data contansts and with few modifications, I will use the concepts of the Characterization Test to guarantee the current behavior.

This validation written in Python (pytest) will only perform the assertion of specific calls to api. Will not contemplate:
- Checking the json schema structure;
- Random and automatic generation of values for the query;

## Required
- Python 2.7


## Prepare
```
pip install -r requirements.txt 
export API_KEY=<Google API KEY>
```


## Run
```
pytest
```


## Reference
- [Characterization Test/Golden Master Testing](https://en.wikipedia.org/wiki/Characterization_test)
