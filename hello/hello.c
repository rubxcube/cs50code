// including libraries to access functions
#include <stdio.h>
#include <cs50.h>

// creating a function
int main(void)
{
    // getting user input
    string user_name = get_string("What's your name? ");
    // printing user name
    printf("Hello, %s\n", user_name);
}
