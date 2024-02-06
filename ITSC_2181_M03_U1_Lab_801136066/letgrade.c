#include <stdio.h>

char getLetterGrade(int numGrade) {
    if (numGrade >= 90)
        return 'A';
    else if (numGrade >= 80)
        return 'B';
    else if (numGrade >= 70)
        return 'C';
    else if (numGrade >= 60)
        return 'D';
    else
        return 'F';
}

int main() {
    int numGrade;
    char letterGrade;

    printf("Please enter your grade: ");
    if (scanf("%d", &numGrade) != 1) {
        printf("Failed to read the grade.\n");
        return 1;
    }

    letterGrade = getLetterGrade(numGrade);

    printf("Your Grade is: %c.\n", letterGrade);

    return 0;
}
