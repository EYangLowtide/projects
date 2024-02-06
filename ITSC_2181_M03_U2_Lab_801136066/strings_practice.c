#include <stdio.h>
#include <ctype.h> 

// Function declaration
void capitalize(char str[]);

int main() {
    // Test string 1
    char the_str[] = "test";
    capitalize(the_str);
    printf("%s\n", the_str);

    // Test string 2
    char the_str2[] = "This IS a tesT!";
    capitalize(the_str2);
    printf("%s\n", the_str2);

   // Test string 3
   char the_str3[] = "tEsT Is tHiS WoRkInG";
   capitalize(the_str3);
   printf("%s\n", the_str3);

  // Test string 4
  char the_str4[] = "fhalshdflahsdfkahsdfkahs";
  capitalize(the_str4);
  printf("%s\n", the_str4);
    return 0;
}

// Function definition
void capitalize(char str[]) {
    int i = 0;
    // Loop through each character until the null terminator is found
    while (str[i] != '\0') {
        // Check if the current character is an alphabetic character
        if (isalpha(str[i])) {
            // Convert to uppercase if it is an alphabetic character
            str[i] = toupper(str[i]);
        }
        i++; // Move to the next character
    }
}
