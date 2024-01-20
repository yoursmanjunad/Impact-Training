# Stacks and Queues
- [ ] Valid Parentheses
- [ ] Evaluate Reverse Polish Notation
- [ ] Next Greater Element
- [ ] Implement a Min Stack
- [ ] Decode String
### Decode String:

Given an encoded string, return its decoded string using a stack. The encoding rule is k[encoded_string], where the `encoded_string` inside the square brackets is repeated exactly `k` times.

#### Example:

**Input:**
```
s = "3[a]2[bc]"
```

**Output:**
```
"aaabcbc"
```

**Explanation:**
- The string "3[a]" is expanded to "aaa".
- The string "2[bc]" is expanded to "bcbc".
- Concatenating the results, the final decoded string is "aaabcbc".

#### Test Cases:

1. **Basic Test Case:**
   ```
   Input: s = "3[a]2[bc]"
   Output: "aaabcbc"
   ```

2. **Nested Encoding:**
   ```
   Input: s = "2[3[a]b]"
   Output: "aaabaaab"
   ```
   Explanation: The string inside the square brackets "3[a]" is expanded to "aaa", and then "2[aaa]b" is expanded to "aaabaaab".

3. **Multiple Digits:**
   ```
   Input: s = "10[a]"
   Output: "aaaaaaaaaa"
   ```
   Explanation: The string "10[a]" is expanded to "aaaaaaaaaa".

4. **Mixed Encoding:**
   ```
   Input: s = "3[a]2[b4[F]c]"
   Output: "aaabFFFcbbFFFc"
   ```
   Explanation: The string "3[a]" is expanded to "aaa", the string "2[b4[F]c]" is expanded to "bFFFc", and then concatenated.

5. **No Encoding:**
   ```
   Input: s = "abc"
   Output: "abc"
   ```
   Explanation: Since there are no square brackets, the output is the same as the input.

6. **Complex Encoding:**
   ```
   Input: s = "2[ab3[c]d]ef"
   Output: "abcccdabcccdef"
   ```
   Explanation: The string "2[ab3[c]d]" is expanded to "abcccdabccc", and then concatenated with "ef".

These test cases cover various scenarios, including nested encoding, multiple digits, and complex combinations. Working on these examples will help you understand how to implement a solution for the "Decode String" problem.
- [ ] 
