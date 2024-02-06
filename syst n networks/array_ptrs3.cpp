//edward yang
#include <iostream>
using namespace std;

int main() {
    int my_ints[4]; // Define an array of integers with size 4
    int* my_ptrs[4]; // Define an array of pointers of the same size

    // Populate my_ints with user input
    for (int i = 0; i < 4; ++i) {
        cout << "Enter integer " << i + 1 << ": ";
        cin >> my_ints[i];
        my_ptrs[i] = &my_ints[i]; // Initialize pointers
    }

    // Sort the pointers in my_ptrs based on the integers they point to
    for (int i = 0; i < 4; ++i) {
        for (int j = i + 1; j < 4; ++j) {
            if (*my_ptrs[i] > *my_ptrs[j]) {
                // Swap pointers
                int* temp = my_ptrs[i];
                my_ptrs[i] = my_ptrs[j];
                my_ptrs[j] = temp;
            }
        }
    }

    // Print the values pointed to by each pointer in my_ptrs
    cout << "\nThe sorted values are: ";
    for (int i = 0; i < 4; ++i) {
        cout << *my_ptrs[i] << "\t";
    }

    // Sanity check: print the contents of my_ints
    cout << "\nOriginal array (my_ints): ";
    for (int i = 0; i < 4; ++i) {
        cout << my_ints[i] << "\t";
    }

    return 0;
}
