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

void my_sigchld_handler(){
  pid_t pid;
  int   status;
  while ((pid = waitpid(-1, &status, WNOHANG)) != -1){
    printf("yoloo\n");//printf("%s\n",curr_names[0]);// Or whatever you need to do with the PID
  }
  return;
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


void main(){
  //signal(SIGCHLD, my_sigchld_handler);
  char* username = getenv("USER");
  char hostname[30];
  gethostname(hostname, 30);
  char* args[100];
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
  printf("%s\n",pd );
  pid_t p;
  int   status;

  while(1){
    pid_t p;
    int   status;
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
    if (inp[length - 1] == '\n'){
      inp[length - 1] = '\0';    
    }

    token = strtok(inp," ");
    int len=0;
    while(token){
      if (strcmp(token,"exit") != 0){
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
      exit(0);
    }
    if (strcmp(args[len-1],"&") == 0){
      args[len-1] = NULL;
      background = 1;
    }
    else{
      args[len] = NULL;
    }

    if(strcmp(args[0],"!hist") == 0) {
      args[0] = hist_names[(*args[1] - '0') - 1];
      args[1] = NULL;
    }
    else if (strcmp(args[0],"pid") == 0){
      pidd(hist_names,hist_pid,PROCESS_COUNT,curr_names,curr_pid,CURR_COUNT,args);
    }
    
    else if(strcmp(args[0],"hist") == 0 ){
      hist(hist_names,hist_pid,PROCESS_COUNT,args);
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

