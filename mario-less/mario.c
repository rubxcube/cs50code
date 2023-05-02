#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // prompting user for input
    int number = get_int("Height: ");

    // prompting unless user inputs numbers between 1 and 8 (inclusive)
    if (number < 1 || number > 8)
    {
        main();
    }
    else
    {
        // loop for new line
        for (int i = 0; i < number; i++)
        {
            // loop for spaces
            for (int k = 1; k < number - i; k++)
            {
                printf(" ");
            }
            // loop for hashes
            for (int j = 0; j < i + 1; j++)
            {
                printf("#");
            }
            printf("\n");
        }
    }
}
