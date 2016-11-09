#include<stdio.h>
#include<stdlib.h>
#include <pthread.h>

typedef struct __sort_t {
  int** matrix;
  int order;
  int sort_index;
} sort_t;

typedef struct __add_t {
  int** A;
  int** B;
  int** C;
  int order;
  int sort_index;
} add_t;

pthread_mutex_t lock;
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

void * initialize_matrix(void * arg,int flag) {
  if (flag == 0){
    sort_t * m = (sort_t * ) arg;
    int i,j;
    for (i = 0; i < m->order; i++){
      for (j = 0; j < m->order; j++){
        m->matrix[i][j] = (int)(rand() % 100);
        printf("%d\n",m->matrix[i][j]);
      }
    }
  }
  else if (flag == 1){
    add_t * m = (add_t * ) arg;
    int i,j;
    for (i = 0; i < m->order; i++){
      for (j = 0; j < m->order; j++){
        m->A[i][j] = (int)(rand() % 100);
        m->B[i][j] = (int)(rand() % 100);
        //printf("%d\n",m->matrix[i][j]);
      }
    }
  }
  return NULL;
}

void * sort(void * arg) {
  sort_t * m = (sort_t * ) arg;
  int i,j,temp,ind;
  //if (m->count < m->MAX){
  pthread_mutex_lock(&lock);
  ind = m->sort_index;
  m->sort_index ++;
  pthread_mutex_unlock(&lock);
  for (i = 0; i < m->order; i++){
    for (j = i + 1; j < m->order; j++){
      if (m->matrix[i][ind] > m->matrix[j][ind]){
        temp = m->matrix[i][ind];
        m->matrix[i][ind] = m->matrix[j][ind];
        m->matrix[j][ind] = temp;
      }
      else break;
    }
      }

  return NULL;
}


void * add(void * arg) {
  add_t * m = (add_t * ) arg;
  int i,ind;
  pthread_mutex_lock(&lock);
  ind = m->sort_index;
  m->sort_index ++;
  pthread_mutex_unlock(&lock);
  for (i = 0; i < m->order; i++){
    m->C[i][ind] =m->A[i][ind] + m->B[i][ind];
  }

  return NULL;
}

int main() {

  sort_t args;
  add_t add_args;
  int i,j;
  int N;
  char *ps, s[100];
  while (fgets(s, sizeof(s), stdin)) {
    N = strtol(s, &ps, 10);
    if (ps == s || *ps != '\n') {
      printf("Please enter an integer: ");
    } else break;
  }
  pthread_t p_sort[N],p_add[N];  
  args.order = N;
  add_args.order = N;
  args.sort_index = 0;
  add_args.sort_index = 0;
  args.matrix = (int**)malloc(N * sizeof(int*));
  for(i = 0; i < N; i++){
    args.matrix[i] = (int*)malloc(N * sizeof(int));
  }
  add_args.A = (int**)malloc(N * sizeof(int*));
  for(i = 0; i < N; i++){
    add_args.A[i] = (int*)malloc(N * sizeof(int));
  }
  add_args.B = (int**)malloc(N * sizeof(int*));
  for(i = 0; i < N; i++){
    add_args.B[i] = (int*)malloc(N * sizeof(int));
  }
  add_args.C = (int**)malloc(N * sizeof(int*));
  for(i = 0; i < N; i++){
    add_args.C[i] = (int*)malloc(N * sizeof(int));
  }
  initialize_matrix(&args,0);
  initialize_matrix(&add_args,1);
  for (i = 0; i < N; i++){
    pthread_create(&p_sort[i], NULL, sort, &args);
    pthread_join(p_sort[i],NULL);
  }

  printf("printing sorted array :\n");
  for (i = 0; i < N; i++){
    for (j = 0; j < N; j++){
      printf("%d\n",args.matrix[i][j] );
    }
  }
  for (i = 0; i < N; i++){
    pthread_create(&p_add[i], NULL, add, &add_args);
    pthread_join(p_add[i],NULL);
  }
  printf("printing sorted array :\n");
  for (i = 0; i < N; i++){
    for (j = 0; j < N; j++){
      printf("%d + %d = %d\n",add_args.A[i][j],add_args.B[i][j],add_args.C[i][j] );
    }
  }
  return 0;
}


