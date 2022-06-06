class Solution:
    roman_numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToDecimal(self, S):
        decimal = 0
        current_value = 0
        next_value = 0
        for i in range(len(S) - 1):
            current_value = self.roman_numbers[S[i]]
            next_value = self.roman_numbers[S[i + 1]]
            # check if next value is greater or equal
            if current_value >= next_value:
                decimal += current_value
            else:
                decimal -= current_value

        return decimal + self.roman_numbers[S[len(S) - 1]]


ob = Solution()
print(ob.romanToDecimal("LIV"))
