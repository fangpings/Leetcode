"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        times, left = n // 4, n % 4
        total = 0
        tmp = [' '] * 4
        i = -1
        for i in range(times):
            k = read4(tmp)
            buf[i*4:(i+1)*4] = tmp
            total += k
            if k < 4:
                return total
        k = read4(tmp)
        actual_last_read = min(k, left)
        buf[(i+1)*4:(i+2)*4] = tmp
        return total + actual_last_read