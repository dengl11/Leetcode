// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
    char tmp[4];
    int len = 0;
    
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) {
        // printf("n = %d, len = %d\n", n, len);
        if (n <= len) {
            memcpy(buf, tmp, n);
            len -= n;
            if (len > 0) {
                memmove(tmp, tmp+n, len);
            }
            return n;
        } else {
            memcpy(buf, tmp, len);
            n -= len;
            int offset = len;
            len = 0;
            while (n >= 4) {
                int read = read4(buf + offset);
                if (read == 0) break;
                n -= read;
                offset += read;
            }
            if (n > 0) {
                len = read4(tmp);
                if (len == 0) return offset;
                return offset + read(buf + offset, n);
            }   
            return offset;
        }
    }
};