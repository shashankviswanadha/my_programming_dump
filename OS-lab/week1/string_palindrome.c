#include<stdio.h>
#include <string.h>
int main()
{ int l;
  printf("Enter the length of the string : ");
  scanf("%d",&l);
  char st[l];
  printf("Enter the string : ");
  scanf("%s",st);
  int len = (int)strlen(st);
  int i;
  int flag = 0;
  for (i = 0 ; i < len/2 ; i++){
    if (st[i] != st[len-1-i]){
        flag = 1;
        break;
      }
  }
  if (flag == 0)
  {
     printf("%s is a palindrome \n",st );
   }
 else
   {
     printf("%s is not a palindrome \n",st );  
     }
}
