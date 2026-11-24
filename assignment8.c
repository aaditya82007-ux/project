#include <stdio.h>

// Function to swap speeds using pointers (Call by Reference)
void swapSpeeds(float *motor1, float *motor2) {
    float temp = *motor1;
    *motor1 = *motor2;
    *motor2 = temp;
}

int main() {
    float speed1, speed2;

    // Input speeds of the two robot motors
    printf("Enter speed of Robot Motor 1: ");
    scanf("%f", &speed1);

    printf("Enter speed of Robot Motor 2: ");
    scanf("%f", &speed2);

    // Display speeds before swapping
    printf("\n--- Before Control Assignment Swap ---\n");
    printf("Motor 1 Speed: %.2f\n", speed1);
    printf("Motor 2 Speed: %.2f\n", speed2);

    // Exchange speed values using pointers
    swapSpeeds(&speed1, &speed2);

    // Display speeds after swapping
    printf("\n--- After Control Assignment Swap ---\n");
    printf("Motor 1 Speed: %.2f\n", speed1);
    printf("Motor 2 Speed: %.2f\n", speed2);

    return 0;
}