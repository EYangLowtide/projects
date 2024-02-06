#include <stdio.h>

int main() {
    int maxTemp = -1; // Initialize to a low value that's likely to be lower than any input
    int temp;
    int day = 0; // To keep track of the current day
    int maxTempDay = 0; // To keep track of the day with the highest temperature

    printf("You will be asked to enter the daily high temperature for 10 consecutive days.\n");

    for (int i = 1; i <= 10; i++) {
        printf("Enter a high temperature: ");
        scanf("%d", &temp);

        // Check if the current temperature is greater than or equal to the max temperature found so far
        if (temp >= maxTemp) {
            maxTemp = temp;
            maxTempDay = i; // Update the day of the max temperature
        }
    }

    printf("The highest recorded temperature in the 10-day period was: %d degrees\n", maxTemp);
    printf("Last recorded on: Day %d\n", maxTempDay);

    return 0;
}
