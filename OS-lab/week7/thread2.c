#include <stdio.h>
#include <pthread.h>
#include <assert.h>
#include <stdlib.h>
#include<string.h>

typedef struct __myarg_t 
{
  int a;
  char *b;
} myarg_t;

typedef struct __myret_t 
{
  int x;
  char *y;
} myret_t;

typedef struct _third_t{
  struct myret_t * first;
  struct myret_t * second;

} third_t;

void * mythread(void * arg) {

myarg_t * m = (myarg_t * ) arg;
int print_index=0;
for(print_index=0; print_index<m->a; print_index++)
{
printf("Printing %d th character %c\n", print_index, *(m->b+print_index));


}
myret_t * r = malloc(sizeof(myret_t));
r->x = 1;
r->y = m->b;
return (void * ) r;
}

void * mythread2(void * arg){
  third_t * t = (third_t *) arg;
  myret_t * r = malloc(sizeof(myret_t));
  r->x = 3;
  r->y = strcat(t->first->y,t->second->y);
  return (void * ) r;
}




int  main(int argc, char * argv[]) 
{
  //int rc;
  pthread_t p1,p2,p3;
  myret_t * m1;
  myret_t * m2;
  myret_t * m3;
  myarg_t args1,args2;
  third_t args3;
  args1.a= strlen(argv[1]);
  args1.b=(char *)malloc(strlen(argv[1]));
  strcpy(args1.b,  argv[1]);

  args2.a= strlen(argv[2]);
  args2.b=(char *)malloc(strlen(argv[2]));
  strcpy(args2.b,  argv[2]);

  pthread_create(&p1, NULL, mythread, &args1);
  pthread_join(p1, (void ** ) &m1);
  printf("returned %d %s\n", m1->x, m1->y);
  pthread_create(&p2, NULL, mythread, &args2);
  pthread_join(p1, (void ** ) &m2);
  printf("returned %d %s\n", m2->x, m2->y);
  args3.first = &m1;
  args3.second = &m2;
  pthread_create(&p3, NULL, mythread2, &args3);
  pthread_join(p3, (void ** ) &m3);
  printf("returned %d %s\n", m3->x, m3->y);
  return 0;

}
