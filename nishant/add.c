#include<stdio.h>
int add(int a,int b)
{
  int c = a + b;
  return c;
}
void main()
{
  int a = 5;
  int b = 6;
  int c = add(a,b);
  printf("%d \n", c);
}
