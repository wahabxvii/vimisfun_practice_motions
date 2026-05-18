<m+B> to mark this line
  v
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    srand(time(NULL));
    
    int secret = rand() % 100 + 1;
    int guess, attempts = 0;
    
    printf("I'm thinking of a number between 1 and 100.\n");
    
    while (1) {
        printf("Your guess? ");
        scanf("%d", &guess);
        
        if (guess < secret)
            printf("Too low!\n");
        else if (guess > secret)
            printf("Too high!\n");
        else {
            attempts++;
            printf("You got it in %d tries! 🎉\n", attempts);
            break;
        }
        
        attempts++;
    }
    
    return 0;
}
