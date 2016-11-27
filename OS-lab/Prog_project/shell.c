#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/resource.h>

int pidd(char (*allnames)[100],int allpids[100],int no_all,char (*currnames)[100],int currpids[100],int no_curr,char* arguments[100]){
  int i = 0;
  if (arguments[1] == NULL){
    printf("command name: ./a.out  process id: %d\n",(int)getpid() );
    return 0;
  }
  else {
    if (strcmp(arguments[1],"current") == 0){
        printf("List of currently executing processes spawned from this shell:\n");
        for (i = 0;i < no_curr; i++){
          printf("command name: %s   process id: %d\n",currnames[i],currpids[i] );
        }
        return 0;
      
      }
      if (strcmp(arguments[1],"all") == 0){
          printf("List of all processes spawned from this shell:\n");
          for (i = 0;i < no_all; i++){
            printf("command name: %s   process id: %d\n",allnames[i],allpids[i] );
          }
          return 0;
      
        }
      
      return 1;
  }



}

int hist(char (*allnames)[100],int allpids[100],int no_all,char* arguments[100]){
  int i;
  if (arguments[1] == NULL){
    for (i = 0;i < no_all; i++){
      printf("%s\n",allnames[i]);
    }
    return 0;
  }
  else{
    int j = *arguments[1] - '0';
    for (i = no_all - j; i<no_all; i++){
      printf("%s\n",allnames[i]);
    }
  }

}

char (*curr_names)[100];
int curr_pid[100];
int CURR_COUNT ; 

/*void unregister_child(int pid){
  int i,hit = CURR_COUNT;
  for (i = 0; i < CURR_COUNT; i++){
    if (curr_pid[i] = (int)pid){
      printf("yyyyyy\n");
      hit = i;
      break;
    }
  }
  for (i = hit; i < CURR_COUNT - 1; i++){
    curr_pid[i] = curr_pid[i+1];
    *curr_names[i] = *curr_names[i+1];
    
  }
  CURR_COUNT--;
  return;
  }*/


void my_sigchld_handler(int sig,siginfo_t *si, void *context){
  int i;
  if(sig == SIGCHLD){
    //printf("%d\n",CURR_COUNT);
    //printf("%d\n",curr_pid[0]);
    //printf("%s\n",curr_names[0] );
    //printf("%d\n",si->si_pid);
    for( i = 0 ; i < CURR_COUNT ; i++){
            if( si->si_pid == curr_pid[i]){
                int pid;
                while (pid>0) {
                    waitpid(curr_pid[i],NULL,0);
                } 
                printf("\n%s with pid %d exited\n",curr_names[i],si->si_pid);
                //pidcurrcount -- ;
                waitpid(-1,NULL,0);
            }
            }
   }
}

void sig_handler(){
}



/*void handler(){ //printf("yolo\n");
  int wstat;
  //union wait wstat;
  pid_t pid;
  int status;
  int i,hit = CURR_COUNT;
  printf("%s\n",curr_names[0]);
  printf("%d\n",curr_pid[0] );
  while (1) {
    pid = wait3 (&wstat, WNOHANG, (struct rusage *)NULL  );
    if (pid == 0)
      return;
    else if (pid == -1)
      return;
    else{
      //printf("%d  %d\n",pid,CURR_COUNT );
      for (i = 0; i < CURR_COUNT ; i++){
        if (curr_pid[i] = (int)pid){
          printf("yyyyyy\n");
          hit = i;
          break;
        }
      }
      for (i = hit; i < CURR_COUNT - 1; i++){
        curr_pid[i]= curr_pid[i+1];
        *curr_names[i] = *curr_names[i+1];
    
      }
      CURR_COUNT --;
      return ;
    }
  }

  }*/

void set_read(int* lpipe)
{
    dup2(lpipe[0], STDIN_FILENO);
    close(lpipe[0]); // we have a copy already, so close it
    close(lpipe[1]); // not using this end
    return;
}
  
void set_write(int* rpipe)
{   printf("right\n" );
    dup2(rpipe[1], STDOUT_FILENO);
    close(rpipe[0]); // not using this end
    close(rpipe[1]); // we have a copy already, so close it
    return;
}

struct in
{int c;
  
};

int fork_and_chain(int* lpipe, int* rpipe, struct in *b, char* arg[100])
{   int ret ;
    int j;
    char* temp[100];
    int pid = fork();
    if (pid == 0)
      { printf("yolyo\n");
        if(lpipe != NULL) {// there's a pipe from the previous process
            set_read(lpipe);
        }
        // else you may want to redirect input from somewhere else for the start
        
        printf("gooo\n");
        
        if (b->c==0){
          strcpy(temp[0],arg[0]);
          for (j = 1;j < 100; j++){
            if (strcmp(arg[j],"|") != 0){
              strcpy(temp[j],arg[j]);
            }
            else {
              break;
            }
          }
          printf("jolo:%d\n",j );
          b->c = j;
          temp[j] = NULL;
          execvp(arg[0],temp);
        }    
        else{
          strcpy(temp[0],arg[b->c]);
          for (j = b->c + 1;j < 100; j++){
            if (strcmp(arg[j],"|") != 0 || arg[j] != NULL){
              strcpy(temp[j - b->c],arg[j]);
            }
            else {
              break;
            }
          }
          ret = b->c;
          b->c = j;
          printf("J : %d\n",j );
          temp[b->c - ret] = NULL;
          execvp(temp[0],temp);
        }
        if(rpipe != NULL){ // there's a pipe to the next process
            set_write(rpipe);
            
        }
        
        // else you may want to redirect out to somewhere else for the end

        // blah do your stuff
        // and make sure the child process terminates in here
        // so it won't continue running the chaining code
      }
    else {
      
    
    int status = 0;
    //printf("%d\n",pid );
    if (waitpid(pid,&status,0) == -1){
      perror( "waitpid" );
    }
    printf("ret:%d\n",b->c );
    printf("%s\n",temp[0] );
    return ret;

    
   
    }
}

struct sigaction sig;

void main(){
  //signal(SIGCHLD, my_sigchld_handler);
  char* username = getenv("USER");
  char hostname[30];
  gethostname(hostname, 30);
  char* args[100];
  char* args1[100];
  char *token;
  char inp[1024];
  int ex = 1;
  int background = 0;
  pid_t pid;
  char (*hist_names)[100] = malloc(sizeof *hist_names * 1024);
  int hist_pid[100];
  int PROCESS_COUNT = 0;
  curr_names = malloc(sizeof *curr_names * 1024);
  int curr_pid[100];
  int CURR_COUNT = 0;
  char cwd[1024];
  char pd[1024];
  char *strLocation;
  getcwd(pd,sizeof(pd));
  pid_t p;
  int   status,pipe_count = 0;
  void my_sigchld_handler(int sig,siginfo_t *si, void *context);
  sig.sa_flags = SA_SIGINFO;
  sig.sa_sigaction = my_sigchld_handler;
  sigaction(SIGCHLD, &sig, NULL);
  struct in *b = malloc(sizeof(struct in));


  int pip[2];
  while(1){
    pid_t p;
    int status;
    pipe_count = 0;
    if (getcwd(cwd,sizeof(cwd)) != NULL){
      if (strcmp(pd,cwd) == 0){
        fprintf(stdout,"%s@%s ~ > ",username,hostname);
      }
      else {
        strLocation = strstr(cwd,pd);  
        if (strLocation != NULL){
          strcpy (strLocation, strLocation + strlen (pd));
          fprintf(stdout,"%s@%s ~ %s> ",username,hostname,strLocation);
        }
        else {
          fprintf(stdout,"%s@%s ~ %s> ",username,hostname,cwd);
          
        }
      }
    }
    fgets(inp,1024,stdin);
    size_t length = strlen(inp);
    if (inp[0] == '\n'){
      continue; 
    }
    else if (inp[length - 1] == '\n'){
      inp[length - 1] = '\0';    
    }

    token = strtok(inp," ");
    int len=0;
    while(token){
      if (strcmp(token,"|") == 0){
        pipe_count ++;
      }
      if (strcmp(token,"quit") != 0){
        args[len] = token;
        token = strtok(NULL," ");
        len++;
      }
      else{
        ex = 0;
        break;
      }
    }
    if (ex == 0){
      int p = (int)getpid();
      int i;
      for (i = 0; i < CURR_COUNT; i++){
        kill(curr_pid[i],SIGKILL);
      }
      kill(p,SIGKILL);
    }
    else if (strcmp(args[len-1],"&") == 0){
      args[len-1] = NULL;
      background = 1;
    }
    else{
      args[len] = NULL;
    }
    if (pipe_count > 0){
      int lpipe[2], rpipe[2];
      pipe(rpipe);
      pipe(lpipe);
      int prop;
      b->c = 0;
      // first child takes input from somewhere else
      fork_and_chain(NULL, rpipe,b,args);

      // output pipe becomes input for the next process.
      lpipe[0] = rpipe[0];
      lpipe[1] = rpipe[1];

      // chain all but the first and last children
      int i;
      for(i = 1; i < pipe_count; i++){
        printf("loop\n");
        pipe(rpipe); // make the next output pipe
        fork_and_chain(lpipe,rpipe,b,args);
        close(lpipe[0]); // both ends are attached, close them on parent
        close(lpipe[1]);
        lpipe[0] = rpipe[0]; // output pipe becomes input pipe
        lpipe[1] = rpipe[1];
      }

      // fork the last one, its output goes somewhere else      
      fork_and_chain(lpipe, NULL,b,args);
      close(lpipe[0]);
      close(lpipe[1]);
      
      strcpy(hist_names[PROCESS_COUNT],args[0]);
      hist_pid[PROCESS_COUNT] = pid;
      PROCESS_COUNT++;
      continue;
      }
      
      
    if(strcmp(args[0],"!hist") == 0) {
      args[0] = hist_names[(*args[1] - '0') - 1];
      args[1] = NULL;
    }
    if (strcmp(args[0],"pid") == 0 || strcmp(args[0],"hist") == 0){
      if (strcmp(args[0],"pid") == 0){
        pidd(hist_names,hist_pid,PROCESS_COUNT,curr_names,curr_pid,CURR_COUNT,args);
      }
      else{
        hist(hist_names,hist_pid,PROCESS_COUNT,args);
      }
    }
          
    else{
      pid = fork();
      if(pid == 0){
        if (strcmp(args[0],"cd") != 0){
          execvp(args[0],args);
          fprintf(stderr, "Child process could not do execvp\n");
          //exit(0);
        }
        exit(0);
      }
      else{
        if (strcmp(args[0],"cd") == 0){
          chdir(args[1]);
          //exit(0);
        }
        if(background == 0){
          int status = 0;
          //printf("%d\n",pid );
          if (waitpid(pid,&status,0) == -1){
            perror( "waitpid" );
          }
        }
        strcpy(hist_names[PROCESS_COUNT],args[0]);
        hist_pid[PROCESS_COUNT] = pid;
        PROCESS_COUNT++;
        if (background == 1){
          strcpy(curr_names[CURR_COUNT],args[0]);
          curr_pid[CURR_COUNT] = pid;
          CURR_COUNT++;
          background = 0;
        }
        //printf("%d  %d\n",PROCESS_COUNT,CURR_COUNT );
        //printf("Child exited\n");
        
        //printlinkedlist(root);
      }
    }
    
  }
   
}
