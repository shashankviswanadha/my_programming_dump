#include <stdio.h>
#include <stdlib.h>
void main()
{ int n;           
  printf("Enter number of random numbers that need to be generated:  " );
  scanf("%d",&n);
  int r,i,j,l,flag = 0,tf = 0,count = 0;
  int arr[n],range = n*100;
  for (i = 0; i < n; i++){
    while (flag == 0){
      r = (int)(rand() % range);
      for (j = 0; j < count ; j++){
        if (arr[j] == r){
          tf = 1;
          break;
        }
      }
        if (tf == 0)
        {
          arr[count] = r;
            flag = 1;
            count = count + 1;
        }
        else
          {
            tf = 0;
            }
        
    }  
    flag = 0;

  }
  for (l = 0; l < count; l++ ) {
      printf("Element[%d] = %d\n", l+1, arr[l] );
      }
  
}
