#include<stdio.h>

void main()
{ int number;
  printf("Type in a number \n");
  scanf("%d", &number);
  int reverse = 0,digit;
  int n = number;
  while(n > 0)
    {
      digit = n%10;
      reverse = reverse*10 + digit;
      n = n/10;
    }
  if (number == reverse)
    {
      printf("%d is a palindrome\n", number );
    }
  else
 {
    printf("%d is not a palindrome\n", number );
  }
  



}
