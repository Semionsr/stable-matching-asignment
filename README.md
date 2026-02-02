Programming Assignment 1: Matching and Verifying

Tem Members
- My Name: Semion Reznik
-- my ufid: 73437964


Project Structure



src folder:
matcher.py
verifier.py
scalability.py

data folder:
example.in
example.out


scalability_graph.png

README.md




-- How to Run

for the Matcher run this command:

python3 src/matcher.py data/example.in


To save output to file:

python3 src/matcher.py data/example.in data/example.out












to run the Verifier

python3 src/verifier.py data/example.in data/example.out


to run the scalability 

python3 src/scalability.py

Requires matplotlib: `pip install matplotlib`

---

---       Example
This is how the inputs and ouytputs currently look like and hwo they should look if ur trying different examples

3
1 2 3
2 3 1
2 1 3
2 1 3
1 2 3
1 2 3








This is how the output should look

1 1
2 2
3 3




---    Task C: Scalability Analysis

Graph:
THe graph is in the data folder and is called scalability graph.

Things I noticed and observed:

What I noticed is that the graph has exponntial growth. Specifically when the number of hospitals increases the time increases by much more and the graph looks about exponential.










Assumptions


- ThEre is the proper amount of inputs to get an output
- Input files are properly formated

- Hospital and student IDs are 1-indexed

