#include<stdio.h>
#include<stdlib.h>
int main(int argc, char* argv[]){
int *x;

 printf("Printing x: %d \n", x);

 x=(int *)malloc(sizeof(int));

printf("Printing x:%d, *x: %d\n ",  x, *x);


}
