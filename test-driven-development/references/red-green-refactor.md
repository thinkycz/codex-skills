# Red Green Refactor

Use this default loop unless the repo or task requires a different sequence:

1. write a failing test for the intended behavior
2. confirm it fails for the right reason
3. make the smallest production change that turns it green
4. clean up the code and tests while keeping behavior fixed
5. run a slightly broader confidence pass

## Pacing Rules

- one behavior at a time
- one meaningful failing test at a time
- one narrow fix at a time

If the test does not fail first, the loop is not giving trustworthy feedback.
