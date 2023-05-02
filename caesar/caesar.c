#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

char rotate(char letter, int number);

int main(int argc, string argv[])
{
    // Counting command-line arguments
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Checking the Key
    string str = argv[1];
    for (int i = 0, n = strlen(str); i < n; i++)
    {
        if (!isdigit(str[i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int num = atoi(argv[1]);

    // Prompting for plaintext
    string text = get_string("plaintext:  ");
    printf("ciphertext: ");

    // Calling rotate on each char of plaintext
    // Outputting ciphertext
    for (int j = 0, m = strlen(text); j < m; j++)
    {
        char cipher = rotate(text[j], num);
        printf("%c", cipher);
    }
    printf("\n");
}

// rotating given letter by number times if alphabetical
char rotate(char letter, int number)
{
    char ciphertext;
    if (isupper(letter))
    {
        ciphertext = (((letter - 65) + number) % 26) + 65;
    }
    else if (islower(letter))
    {
        ciphertext = (((letter - 97) + number) % 26) + 97;
    }
    else
    {
        ciphertext = letter;
    }
    return ciphertext;
}