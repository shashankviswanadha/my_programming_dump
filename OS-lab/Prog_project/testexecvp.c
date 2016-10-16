#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void main(){
  char* arg[] = {"ls", "-l", NULL};
  execvp(arg[0],arg);
}
