class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        walker, runner = 0,0
        while runner < len(chars):
            # Initially each of the counts are set to 1
            count = 1

            # Set the walker and runner to the same character
            chars[walker] = chars[runner]

            # We make sure to not go past the last character and check if the next character is equal to our current character. If so, we add 1 to count and move the runner pointer 1
            while runner + 1 < len(chars) and chars[runner] == chars[runner+1]:
                count += 1
                runner += 1
            
            # If the count is greater than 1, we can compress the string
            if count > 1:
                # We loop through each count, we increment the walker to REFERENCE the next position since that is the position where the digit will be written. We then increase the walker pointer so that the walker pointer can point to the next digit.
                for c in str(count):
                    chars[walker+1] = c
                    walker += 1
            # We increase both the walker and runner pointers by 1 to adjust the walker for the NEXT CHARACTER
            walker += 1
            runner += 1
        # Walker wil be the pointer of the last digit or character, which is the length of the array
        return walker