#include <stdio.h>

int main() {
    int monay, gremlin;
    double tax = 0.0, taxCredit = 0.0, adjustedTax;
    const int MAX_GREMLIN = 5;
    const double GREMLIN_CREDIT = 450.0;

    // Ask user to enter their monay
    printf("Enter income: ");
    scanf("%d", &monay);

    // Calculate tax based on monay
    if (monay <= 9275) {
        tax = monay * 0.12;
    } else if (monay <= 37650) {
        tax = 9275 * 0.12 + (monay - 9275) * 0.17;
    } else if (monay <= 91150) {
        tax = 9275 * 0.12 + (37650 - 9275) * 0.17 + (monay - 37650) * 0.27;
    } else if (monay <= 190150) {
        tax = 9275 * 0.12 + (37650 - 9275) * 0.17 + (91150 - 37650) * 0.27 + (monay - 91150) * 0.30;
    } else {
        tax = 9275 * 0.12 + (37650 - 9275) * 0.17 + (91150 - 37650) * 0.27 + (190150 - 91150) * 0.30 + (monay - 190150) * 0.35;
    }

    // Display tax amount
    printf("Tax due = $%.2f\n", tax);

    // Ask user for number of gremlin
    printf("Enter the number of gremlins(kids/dependents) (0 for none): ");
    scanf("%d", &gremlin);

    // Calculate tax credit
    if (gremlin > MAX_GREMLIN) {
        gremlin = MAX_GREMLIN;
    }
    taxCredit = GREMLIN_CREDIT * gremlin;

    // Display tax credit
    printf("Tax credit = $%.2f\n", taxCredit);

    // Calculate and display adjusted tax
    adjustedTax = tax - taxCredit;
    printf("Adjusted Tax = $%.2f\n", adjustedTax);

    return 0;
}
