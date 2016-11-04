#include<stdio.h>
#include <pthread.h>
#include <stdlib.h>

typedef struct __myarg_t {
  int count;
  int MAX;
  int* array;
} myarg_t;

pthread_mutex_t lock;
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

void * mythread(void * arg) {
  myarg_t * m = (myarg_t * ) arg;
  int ra,j;
  //if (m->count < m->MAX){
  pthread_mutex_lock(&lock);
    ra = (int)(rand() % 100);
    for (j = 0; j<m->MAX; j++){
      if (m->array[j] == NULL){
        printf("%d\n",ra );
        m->array[j] = ra;
        //m->count ++;
        break;
      }

    } 
    pthread_mutex_unlock(&lock);
    //}
  return NULL;
}

int main() {
  pthread_t p;  
  myarg_t args;
  int i;
  args.count = 0;
  args.MAX = 10;
  args.array = (int*)malloc(sizeof(int) * args.MAX);
  for (i = 0; i < args.MAX; i++){
    args.array[i] = NULL;
  }
  for (i = 0; i < args.MAX ; i++){
    pthread_create(&p, NULL, mythread, &args);
    pthread_join(p,NULL);
  }
  printf("printing array :\n");
  for (i = 0; i < args.MAX; i++){
    printf("%d\n",args.array[i] );

  }
  return 0;
}
