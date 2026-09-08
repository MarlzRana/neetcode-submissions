'''
TC: O(n) 
SC: O(n)

Problem:
- Not a security question
- Send multiple strings as a single string, be able to get from that single string back to the list os stirns

Constraints:
- You may get 0 strings
- You may get the empty string
- Strings can be any ascii character including the empty space
- Case matters

My initial thinking:
Isn't this what URL encoding basically does; can we introduce a special character separator, and escape it when encoding, and understand the escape it when decoding.

Let's %20 to separate strings

Edges cases to think about:
An actual %20 should be escaped to \%20
What happens if the user has \%20 in the string - escape it again? \\%20

The decoder should TLDR drop any \ that pre-pend 20% in the final strings

Scratch pad:
[len(word) - 3, len(word) - 2, len(word) - 1]
'\` -> '\\'
["\\", "Yo"] -> "\\\\%20Yo" -> 
["\\%20", "Yo:] -> '\\\\\%20%20Yo" -> 

something about odd and even escaping
If it is even, you were only trying to escape the escape char
If it is odd, you were trying to escape the special symbol 
'''

class Solution:
    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for word in strs:
            for i in range(len(word)):
                # Lookahead two chars and if it is %20, escape it with a \
                if word.startswith("%20", i):
                    final_str += "\\"
                # If the char is backslash, escape it
                if word[i] == "\\":
                    final_str += "\\"
                # Else add regularly to the string
                final_str += word[i]
            final_str += "%20"
        return final_str
            
    def decode(self, s: str) -> List[str]:
        words = []
        curr_word = ""

        i = 0
        while i < len(s):
            # Lookahead a char, and if it is a double slash, capture the single slash it represents
            if s.startswith("\\\\", i):
                curr_word += "\\"
                i += 2
                continue
            # Lookahead three chars, and if it is a percentage 20, capture the single slash it represents
            if s.startswith("\\%20", i):
                curr_word += "%20"
                i += 4
                continue
            # Lookahead two chars, and if it is a percentage 20, it represents a space
            if s.startswith("%20", i) :
                words.append(curr_word)
                curr_word = ""
                i += 3
                continue
            curr_word += s[i]
            i += 1 
        
        return words
            
            

        
