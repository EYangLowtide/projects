// Edward Yang

#include <iostream>

// Function to swap two integers using pointers
void swapInts(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int num1, num2;

    // Ask for two integer values
    std::cout << "Enter first integer: ";
    std::cin >> num1;
    std::cout << "Enter second integer: ";
    std::cin >> num2;

    // Calling the swap function
    swapInts(&num1, &num2);

    // Printing the swapped values
    std::cout << "After swapping:" << std::endl;
    std::cout << "First integer: " << num1 << std::endl;
    std::cout << "Second integer: " << num2 << std::endl;

    return 0;
}
