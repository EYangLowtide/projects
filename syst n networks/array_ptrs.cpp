//edward yang
#include <iostream>
using namespace std;

int main() {
    const int SIZE = 4;
    int my_ints[SIZE] = {25,7,1,10}; // Pre-defined values
    int* my_ptrs[SIZE];

    // Initialize my_ptrs to point to my_ints elements
    for (int i = 0; i < SIZE; ++i) {
        my_ptrs[i] = &my_ints[i];
    }

    // Bubble Sort: Sort the pointers in my_ptrs based on the values they point to
    for (int i = 0; i < SIZE - 1; ++i) {
        for (int j = 0; j < SIZE - i - 1; ++j) {
            if (*my_ptrs[j] > *my_ptrs[j + 1]) {
                // Swap pointers
                int* temp = my_ptrs[j];
                my_ptrs[j] = my_ptrs[j + 1];
                my_ptrs[j + 1] = temp;
            }
        }
    }

    // Print the values pointed to by my_ptrs
    cout << "Sorted values:" << endl;
    for (int i = 0; i < SIZE; ++i) {
        cout << *my_ptrs[i] << " ";
    }
    cout << endl;

    // Sanity check: Print my_ints to ensure it's unchanged
    cout << "Original array (my_ints):" << endl;
    for (int i = 0; i < SIZE; ++i) {
        cout << my_ints[i] << " ";
    }
    cout << endl;

    return 0;
}