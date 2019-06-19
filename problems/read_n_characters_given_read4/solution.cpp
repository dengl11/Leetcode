// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) {
        int read = 0;
        while (n - read >= 4) {
            int r = read4(buf + read);
            if (r == 0) {
                break;
            } else {
                read += r;
            }
        }
        if (read < n) {
            int r = n - read;
            char buff[4];
            int x = read4(buff);
            memcpy(buf + read, buff, r > x ? x : r);
            read += x < r ? x : r;
        }
        return read;
    }
};