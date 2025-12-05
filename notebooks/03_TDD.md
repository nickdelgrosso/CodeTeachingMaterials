
# Test-Driven Development (TDD)


## Project Work Options:

### Option 1. Add automated tests to one of your own projects.

 thi

### Option 2. Do the DNA Transcription Kata with your partner, following Test-Driven-Development practices


Repository to Clone: https://github.com/nickdelgrosso/dna-transcription-kata


    Test-Driven Development is a software development approach where you write tests *before* writing the implementation code. The cycle follows three steps:

    1. **Red**: Write a failing test for the next small piece of functionality
    2. **Green**: Write just enough code to make the test pass
    3. **Refactor**: Clean up the code while keeping tests passing

    This practice helps ensure your code is testable, encourages simple designs, and provides immediate feedback on correctness.


Reference Slides 18-25 in [Reference_TestDrivenDevelopment_PairProgramming.pdf](Reference_TestDrivenDevelopment_PairProgramming.pdf) for examples of how this goes in practice. 

Note: This is often a tricky practice to learn, so don't worry if your group abandons it and instead finds yourselves writing "source code, then test".  The key here is to get used to thinking about the source code from two sides as part of development--the **implementation** (what's inside the function), and the **interface** (what the code calling it sees).

Stuck on how to start?  Here's a simple first test that might get the group moving:

```python
def test_transcribe_single_adenine_to_uracil():
    assert transcribe_rna("A") == "U"
```
