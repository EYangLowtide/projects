#include <stdio.h>

int main() {
    int hot1, hot2, hot3;
    int maxTemp, maxDay;

    printf("You will be asked to enter the daily high temperature for 3 consecutive days.\n");

    // Read temperatures for three days
    printf("Enter a high temperature for day 1: ");
    scanf("%d", &hot1);
    maxTemp = hot1;
    maxDay = 1;

    printf("Enter a high temperature for day 2: ");
    scanf("%d", &hot2);
    if (hot2 >= maxTemp) {
        maxTemp = hot2;
        maxDay = 2;
    }

    printf("Enter a high temperature for day 3: ");
    scanf("%d", &hot3);
    if (hot3 >= maxTemp) {
        maxTemp = hot3;
        maxDay = 3;
    }

    // Display the result
    printf("The highest recorded temperature in the 3-day period was: %d degrees\n", maxTemp);
    printf("Recorded on day #%d\n", maxDay);

    return 0;
}
