#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{
    //one command line argument
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    //check for valid input
    string key = argv[1];
    int length = strlen(key);

    for (int i = 0; i < length; i++)
    {
        if (!isdigit(key[i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    //print plaintext
    string plaintext = get_string("plaintext:  ");

    int j = 0;
    char ciphertext[strlen(plaintext) + 1];

    while (plaintext[j] != '\0')
    {
        char currChar = plaintext[j];

        int currAscii = currChar;

        int keyInt = atoi(key);

        //check if it's english
        if (isalpha(currChar))
        {
            if (isupper(currChar))
            {
                currAscii = currAscii - 65;
            }
            else
            {
                currAscii = currAscii - 97;
            }

            int outAscii = (currAscii + keyInt) % 26;

            //check uppercase
            if (isupper(currChar))
            {
                outAscii = outAscii + 65;
            }
            else
            {
                outAscii = outAscii + 97;
            }
            //transfer
            char outChar = outAscii;

            ciphertext[j] = outChar;
        }
        else
        {
            ciphertext[j] = currChar;
        }

        j++;

    }
    //print
    ciphertext[strlen(plaintext)] = '\0';

    printf("ciphertext: %s\n", ciphertext);

    return 0;

}