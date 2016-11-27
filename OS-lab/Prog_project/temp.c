        printf("count:%d\n",count);
        int temp = 0;
        if (count == 0){
          int i;
          for (i = 0; i < len; i++){
            if (strcmp(args[i],"|") == 0){
              args[i] = NULL;
              temp = i;
            }
          }
        }
        if (count > 0){
          int i;
          for (i = temp + 1; i < len; i++){
            strcmp(args[i - temp - 1],args[i]);
            printf("ylo%s\n",args[0] );
          }
        }


else {
              if (count == 0){
                close(pip[0]);    // close reading end in the child

                dup2(pip[1], 1);  // send stdout to the pipe
                
              
                close(pip[1]);
                execvp(args[0],args);
              }
              else {
                char buffer[1024];

                close(pip[1]);  // close the write end of the pipe in the parent
                
                while (read(pip[0], buffer, sizeof(buffer)) != 0){
                  //printf("%s\n",buffer );
                  strcpy(args[1],buffer);
                  args[2] = NULL;
                  execvp(args[0],args);
                  
                }
                
              }
