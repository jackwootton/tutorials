<h1>Notes</h1>

<h2>Syntax</h2>

- Use `for in` loop where possible. It's much tider than `range`.
  - Think: _Do I need to do something **for** each item **in**?_
- Initializing `return` list with first item before entering loop.
- Unpacking tuple with one line: `a, b = (2, 5)`

<h2>Big-O</h2>

<h3>Time</h3>

- `n*log(n)` - Best case sorting algorithm.
- `n` - Iterating over all meetings.
- `O(nlog(n))` - Dominant term is `n*log(n)`.

<h3>Space</h3>

- `n` - Worst-case scenario, no meetings overlap and a new list of the same
  length is created.
