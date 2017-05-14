#include <stdio.h>

void hello(int n);



void
hello(int n)
{
    int i;

    for (i = 0;i<n;i++)
    {
        printf("C says hello\n");
    }
}
