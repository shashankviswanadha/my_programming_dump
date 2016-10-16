#include <stdio.h>
#include <stdlib.h>
#include <math.h>

long to_binary(long decimal){
  int count = 0;
  long bin = 0;
  while (decimal > 1){
    bin = bin + (long)((decimal % 2) * (long)pow (10,count));
    decimal = decimal/2;
    count++;
  }
  bin = bin + (long)((decimal % 2) * (long) pow (10,count));
  return bin;
}


void main(){
  long test = to_binary(1024);
  printf("%zu\n",test );
}
