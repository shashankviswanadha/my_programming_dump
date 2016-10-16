#include<stdio.h>
void main()
{
  int i,j,k,l;
  int arr [10] = {10,9,8,7,6,5,4,3,2,1};
 for (i = 0; i<10; i++)
    {
      for (j = i+1; j<10; j++)
        {
          if (arr[j] < arr[i])
                       {
                         int a = arr[j];
                         arr[j] = arr[i];
                         arr[i] = a;
                           }
        }
    }
  for (l = 0; l < 10; l++ ) {
      printf("Element[%d] = %d\n", l, arr[l] );
   }
 
 }
