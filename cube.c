#include <stdio.h>

float cube_volume(float side) { return side * side * side; } // float the volume of the cube

int main() {
  // float side = 5.0;

  float side; // declare the side of the cube
  
  printf("Enter the side length of the cube: "); // ask the user to input the side length of the cube
  
  scanf("%f", &side); // get the side length of the cube from the user
  
  float volume = cube_volume(side); // Call the function and store the result
  
  printf("The volume of the cube with side %.2f is %.2f.\n", side, volume); // print the volume of the cube
  
  return 0;
}
