#include <stdio.h>

int main() {
    int i;
    int sum = 0;

    for(i = 0; i < 1000000; i++) {
        if(i % 2 == 0)
            sum += i;
        else
            sum -= i;
    }

    printf("%d\n", sum);
    return 0;
}
