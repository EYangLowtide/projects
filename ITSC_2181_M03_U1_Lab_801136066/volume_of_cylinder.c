#include <stdio.h>

int main() {
    double radius, height, volume;
    const double PI = 3.14159;

    // Asking user to enter the radius and height
    printf("Enter radius: ");
    scanf("%lf", &radius);
    printf("Enter height: ");
    scanf("%lf", &height);

    // Calculating the volume
    volume = PI * radius * radius * height;

    // Displaying the result with two decimal points
    printf("Volume: %.2lf\n", volume);

    return 0;
}
