# put-IT-lab1
Repository for PUT's Information Theory lab1 assignment - approximating natural languages

## Evaluation / running the program
Even though I provide exemplary files generated using this program, if you'd like to try it out and generate files yourself, the program can be run with a short:
```python
python3 main.py
```
Answers for questions asked in the assignment can be found in answers.txt

Approximations generated by Markov sources take long to run, so to counter it, the contents of norms provided by the lecturer are by default shortened.
- for third-order Markov approximation, contents are shortened to 2000 characters
- for fifth-order Markov approximation, contents are shortened to 1000 characters

These can be altered or removed in the source code, but too big limit (and especially no limit) are discouraged due to long runtime.

## Problems and thoughts
Because of shortened samples, the program may be prone to generating cycles of some specific sequences, or even outputting single letter all over again and again (in my case, it was usually the letter 'q'.

Why is that? There's simply not enough input samples data processed and the program:
- cycles - there are either no or very little other options to choose from
- repeating single letter - no other similar occurrence OR no matching sequence from the corpus at all

I tried to solve the issue by adding an additional check whether given sequence of characters has any possibility to choose from and generating some character randomly if not, but the chances of generating a sensible sequence which occurred in the shortened sample input is so low, the effect was just more or less random sequence, so I ditched the idea.

There's no problem with the program, as the Markov approximations are quite good (especially the fifth-order one). This can be improved by simply increasing the input sample to analyze and get the probabilities out of, but I assume the main goal of the assignment was understanding and successful implementation. That's why I choose to stay with limited input - to save on computation time.
