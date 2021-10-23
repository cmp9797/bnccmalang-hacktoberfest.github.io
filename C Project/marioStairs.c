/*  Ahmad Naufal A.A
Basically this is a program that will make stair in Super Mario */

#include <stdio.h>

//prototype
int height();

int main (void)
{
    int row, coloumn, cpart1, cpart2, cpart3;
    int n = height(); //passing array
    int coloumnnum = 4 + 2 * (n -1);

    for (row=0; row < n ; row++)
    {
        //left side
        for (cpart1=0; cpart1 < n; cpart1++)
           {
                if (cpart1 + row < n - 1 )
                {
                    printf(" ");
                }

                else
                {
                    printf("#");
                }
           }

         //center side
        for (cpart2=0; cpart2 < 2; cpart2++ ) 
           {
               printf (" ");
           }

        //right side
        for (cpart3=0; cpart3 <  row +1; cpart3++)
           {
               printf ("#");
           }

        printf ("\n");
    }
}

int height()
{
    int n;
    do
    {
        //make height in 1-90 range//
        printf ("Insert Height: ");
        scanf (" %d", &n);
        if (n < 1 || n > 8)
        {
            printf("Outranged Input!\n");
        }
    }
    while (n < 1 || n > 90);
    return n;
}