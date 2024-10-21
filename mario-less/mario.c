#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //imput for height 1-8
    int n;
    do
    {
        n= get_int("Height: ");
    }
    while (n<1 || n>8);
//loop through each row
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n-i-1; j++)
        {
            printf(" ");
        }
//print #
        for(int k=0; k<=i; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}