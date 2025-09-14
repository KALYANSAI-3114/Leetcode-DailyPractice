'''  Explanation


📝 Problem Understanding

We are given a list of operations.

Some are numbers → which mean scores.

Some are special commands → "C", "D", "+".

We need to calculate the final score after applying all the rules.

⚡ Rules

Number → just add it as a score.

"C" → cancel the last score (remove it).

"D" → double the last score and add it.

"+" → take the last two scores, add them, and store the result.

Finally, we add all scores and return the total.

👨‍🏫 How the Code Works (Like a Teacher Explains)

We start with an empty list called result.
This will store all the valid scores after each operation.

Then we go through each operation one by one.

If it’s a number → put it in result.

If it’s "C" → remove the last score from result.

If it’s "D" → take the last score, double it, and add it.

If it’s "+" → take the last two scores, add them, and store the result.

At the end, we just take the sum of all numbers in result.

📌 Example Walkthrough

Suppose input is:

["5", "2", "C", "D", "+"]


Start: result = []

"5" → it’s a number → result = [5]

"2" → it’s a number → result = [5, 2]

"C" → cancel last score → remove 2 → result = [5]

"D" → double last score (5×2=10) → result = [5, 10]

"+" → add last two (10+5=15) → result = [5, 10, 15]

Now add them: 5 + 10 + 15 = 30.

So, Final Score = 30 ✅'''


from typing import List

def calPoints(operations: List[str]) -> int:
    operators = ["C", "D", "+"]
    result = []
    for val in operations:
        if val not in operators:
            result.append(int(val))
        elif val == "C":
            result.pop()
        elif val == "D":
            new_val = int(result[-1]) * 2
            result.append(new_val)
        elif val == "+":
            new_val = int(result[-1]) + int(result[-2])
            result.append(new_val)
    return sum(result)


if __name__ == "__main__":
    # Example test case
    operations = ["5", "2", "C", "D", "+"]
    print("Operations:", operations)
    print("Final Score:", calPoints(operations))
