#include<stdio.h>
#include <pthread.h>

 typedef struct __myarg_t {
 int a;
 char *b;
 } myarg_t;
int f=0;

 void * mythread(void * arg) {
 myarg_t * m = (myarg_t * ) arg;
 printf("%d %s\n", m->a, m->b);
 f=1;
 return NULL;
 }

int main(int argc, char * argv[]) {
pthread_t p;
myarg_t args;
args.a = 10;
args.b = "hello world";

pthread_create(&p, NULL, mythread, &args);
while(f==0){


}
return 1;
 }

