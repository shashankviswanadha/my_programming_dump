#include<stdio.h>
#include<stdlib.h>
int main(int argc, char* argv[]){
int *x;
int **y;

printf("Printing x: %d \n", x);

x=(int *)malloc(sizeof(int));

y=&x;

printf("Printing x:%d, *x: %d, *y:%d,  **y:%d\n ", x, *x, *y, **y);

}
