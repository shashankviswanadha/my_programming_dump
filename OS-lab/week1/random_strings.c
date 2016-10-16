#include <stdio.h>
#include <stdlib.h>
void main()
{ int n;           
  printf("Enter number of random strings to need to be generated:  " );
  scanf("%d",&n);
  int r,i,j,l,asc,count = 0;
  char arr[n][11];
  for (i = 0; i < n; i++){
    r = ((int)(rand() % 10)) + 1;
      char ch[r];
      //printf("%d\n\n",r );
      for (j = 0; j < r ; j++){
        asc = (rand() % (126 + 1 - 32)) + 32;
        ch[j] = asc;
      }
      printf("Element[%d] = %s\n", i+1, ch );
        //arr[i] = ch;
      
  }
  for (l = 0; l < count; l++ ) {
      printf("Element[%d] = %s\n", l+1, arr[l] );
      }
  
}

