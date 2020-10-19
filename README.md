@Author Hongsheng Zhong

github: [joking-clock](https://github.com/joking-clock)

# Introduction
This is the Python solution to solve the problem of * Last-Writer-Wins (LWW) Element Set*.

## What is included
1.Implementation using Python: **my_CRDT.py**, which implements the following methods
- Init a new LWW Element Set
- Add an element into LWW Element Set
- Remove an element into LWW Element Set
- Check if an element in current LWW Element Set
- Retrive all the elements.

Along with unit tests in **test_my_CRDT.py**

2.Implementation using Redis and redis-py: **redis_CRDT.py**, which implements the following methods
- Init a new LWW Element Set
- Add an element into LWW Element Set
- Remove an element into LWW Element Set

The Python client for Redis used here is *redis-py*.

Along with unit tests in **test_redis_CRDT.py**

3.git commit history

## Execute tests
run `python -m unittest discover -s . -p "test*.py"` in current working directory


# Note:
- Concurrency and parallelism support is not implemented, which is an assumption that the external caller would achieve concurrency and parallelism.
- The Redis version of CRDT can add config module (planned to use YAML) to externally configure redis server, port, etc., which was not added because short of time.

# References:
Medium post: [CRDT: Conflict-free Replicated Data Types](https://medium.com/@amberovsky/crdt-conflict-free-replicated-data-types-b4bfc8459d26)
Wiki: [Conflict-free replicated data type](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type#cite_note-2011CRDTSurvey-2)