#
# @lc app=leetcode id= lang=python3
#
# [] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars) -> int:
        write_index = 0  # Index to write the compressed characters
        count = 1  # Initialize count of consecutive characters
        n = len(chars)

        # Iterate from the second character to the end
        for i in range(1, n + 1):
            if i < n and chars[i] == chars[i - 1]:
                count += 1
            else:
                chars[write_index] = chars[i - 1]  # Write the character

                # Write the count if it is greater than 1
                if count > 1:
                    count_str = str(count)
                    for j in range(len(count_str)):
                        chars[write_index + j + 1] = count_str[j]
                    write_index += len(count_str)

                write_index += 1
                count = 1

        return write_index

        
        
        
# @lc code=end
