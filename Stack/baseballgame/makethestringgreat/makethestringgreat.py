'''  Explanation

📝 Problem Understanding

We are given a string s containing lowercase and uppercase letters.

We need to remove adjacent pairs where the letters are the same ignoring case, but with opposite cases.  

Example: 'aA' or 'Bb' → should be removed.

We keep doing this until no such adjacent pairs exist.

⚡ Rules

- If two adjacent letters are the same but with different cases → remove them.
- Repeat this process until the string is "good" (no bad adjacent pairs remain).

👨‍🏫 How the Code Works (Like a Teacher Explains)

We use a stack to keep track of the "good" part of the string so far.

Go through each character in the string:

- If the stack is not empty and the top element and current character form a bad pair → pop from stack.
- Otherwise → push current character onto stack.

At the end, join all characters in the stack to get the resulting "good" string.

📌 Example Walkthrough

Suppose input is:

"leEeetcode"

Start: stack = []

'l' → stack = ['l']

'e' → stack = ['l', 'e']

'E' → top = 'e', current = 'E' → bad pair → remove 'e' → stack = ['l']

'e' → stack = ['l', 'e']

't' → stack = ['l', 'e', 't']

'c' → stack = ['l', 'e', 't', 'c']

'o' → stack = ['l', 'e', 't', 'c', 'o']

'd' → stack = ['l', 'e', 't', 'c', 'o', 'd']

'e' → stack = ['l', 'e', 't', 'c', 'o', 'd', 'e']

Join stack → "leetcode" ✅
'''

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for ch in s:
            # Check if last character forms a bad pair with current
            if stack and stack[-1] != ch and stack[-1].lower() == ch.lower():
                stack.pop()  # remove bad pair
            else:
                stack.append(ch)  # keep character

        return "".join(stack)


if __name__ == "__main__":
    # Example test case
    s = "leEeetcode"
    print("Input:", s)
    solution = Solution()
    print("Good String:", solution.makeGood(s))
