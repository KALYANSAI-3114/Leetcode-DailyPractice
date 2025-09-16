'''  Explanation

📝 Problem Understanding

We are given a string `s` consisting of lowercase English letters.

Our task:

1. Find the **vowel** with the maximum frequency in the string.
2. Find the **consonant** with the maximum frequency in the string.
3. Return the **sum** of these two frequencies.

⚡ Rules

- Vowels: 'a', 'e', 'i', 'o', 'u'
- Consonants: all other letters
- If multiple vowels or consonants have the same frequency, just consider the maximum frequency.
- If there are no vowels or no consonants, treat their max frequency as 0.

👨‍🏫 How the Code Works (Like a Teacher Explains)

1. Create a **set of vowels** to quickly check if a character is a vowel.
2. Use two dictionaries:
   - `vowel_freq` → counts occurrences of vowels
   - `consonant_freq` → counts occurrences of consonants
3. Traverse the string:
   - If character is a vowel → increment in `vowel_freq`
   - Else → increment in `consonant_freq`
4. Find the **maximum value** in each dictionary:
   - `max_vowel` → maximum frequency among vowels
   - `max_consonant` → maximum frequency among consonants
5. Return the sum: `max_vowel + max_consonant`

📌 Example Walkthrough

Suppose input is:

"s = 'leetcode'"

- Vowels in string: 'e', 'e', 'o', 'e' → frequencies: {'e': 3, 'o': 1} → max_vowel = 3  
- Consonants: 'l', 't', 'c', 'd' → frequencies: {'l': 1, 't': 1, 'c': 1, 'd': 1} → max_consonant = 1  

Sum → 3 + 1 = 4 ✅

'''

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set("aeiou")
        vowel_freq = {}
        consonant_freq = {}
        
        for ch in s:
            if ch in vowels:
                vowel_freq[ch] = vowel_freq.get(ch, 0) + 1
            else:
                consonant_freq[ch] = consonant_freq.get(ch, 0) + 1
        
        max_vowel = max(vowel_freq.values(), default=0)
        max_consonant = max(consonant_freq.values(), default=0)
        
        return max_vowel + max_consonant


if __name__ == "__main__":
    s = "leetcode"
    solution = Solution()
    print("Input String:", s)
    print("Max Frequency Sum:", solution.maxFreqSum(s))
