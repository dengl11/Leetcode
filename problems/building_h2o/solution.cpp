using namespace std;
class H2O {
    condition_variable cv;
    mutex mu;
    int h, o;
public:
    H2O() {
        h = o = 0;
    }

    void hydrogen(function<void()> releaseHydrogen) {
        unique_lock<mutex> lg(mu);
        cv.wait(lg, [this]{return this->h != 2;});
        h ++;
        releaseHydrogen();
        form();
        cv.notify_all();
    }
    
    void form() {
        if (o > 0 and h >= 2 * o) {
            o --;
            h -= 2;
        }
    }

    void oxygen(function<void()> releaseOxygen) {
        unique_lock<mutex> lg(mu);
        cv.wait(lg, [this]{return this->h >= (this->o + 1) * 2;});
        o ++;
        releaseOxygen();
        form();
        cv.notify_all();
    }
};