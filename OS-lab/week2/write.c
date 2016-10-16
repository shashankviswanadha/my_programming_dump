#include <stdio.h>

void main()
{
  FILE *f,*fp,*fr;
  int arr[20];
  int j;
  f = fopen("numbers.txt","w");
  for (j = 0; j < 15; j++){
    arr[j] = j + 1;
  }
  //fputs(arr,f);
  fwrite(arr, sizeof(int),sizeof(arr), f);
  fclose(f);


  int buffer[20],i;
  fp = fopen("numbers.txt","r");
  fread(buffer,sizeof(int),sizeof(buffer), fp);
  printf("The first 5 numbers in the file are\n");
  for (i= 0 ; i < 5; i++){ 
    printf("%d\n", buffer[i]);
  }
  fclose(fp);

  //int bf[6];
  fr = fopen("numbers.txt","w");
  int l =0;
  for (j = 20; j < 26; j++){
    arr[l] = j ;
    l = l+1;
  }
  fwrite(arr, sizeof(int),sizeof(arr), fr);
  fclose(fr);
  
  int br[20];
  int a[10];
  fp = fopen("numbers.txt","r");
  fread(br, sizeof(int),sizeof(br), fp);
  int dum = 0;
  for (i= 0 ; i < 16; i++){
    //printf("\n%d\n",br[i] );
    if (br[i] > 9){
      a[dum] = br[i];
      dum ++;
  }
  }
  fclose(fp);
  printf("The numbers in the file greater than 9 are:\n");
  for (l = 0; l < 12; l++ ) {
      printf("Element[%d] = %d\n", l+1, a[l] );
      }
}
