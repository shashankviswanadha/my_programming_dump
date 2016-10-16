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


int *random_integers(int size,int rn)
{ int n;           
  n = size;
  int r,i,j,l,flag = 0,tf = 0,count = 0;
  int *arr;
  int range = rn;
  arr = (int *)malloc(size);
  for (i = 0; i < n; i++){
    while (flag == 0){
      r = (int)(rand() % range);
      for (j = 0; j < count ; j++){
        if (arr[j] == r){
          tf = 1;
          break;
        }
      }
        if (tf == 0)
        {
          arr[count] = r;
            flag = 1;
            count = count + 1;
        }
        else
          {
            tf = 0;
            }
        
    }  
    flag = 0;

  }
  return arr;
  
}



struct page_table_entry {
  int frame_number;
  int valid,present,read,write,execute,dirty,user_kernel;
};

int extract_vpn(int virtual_address){
  int VPN_MASK = 64512;
  int SHIFT = 10;
  //Extract the VPN from the virtual address  
  int VPN = (virtual_address & VPN_MASK) >> SHIFT;
  return VPN;
}

int extract_offset(int virtual_address){
  int OFFSET_MASK = 1023;
  int OFFSET = (virtual_address & OFFSET_MASK);
  return OFFSET;
}

int get_frame_number(struct page_table_entry *pte,int virtual_address){
  int vpn = extract_vpn(virtual_address);
  return (pte[vpn].frame_number);

}
int get_physical_address(int fr_num,int off){
  int SHIFT = 10;
  int f_num = fr_num << SHIFT;
  int frr_num = f_num | off;
  return frr_num;
 
  }


/*void set_page_table_entry(struct page_table_entry pte,int fn,int valid,int protected,int present,int dirty,int user_kernel,int read,int write,int execute){
  pte.frame_number = fn;
  pte.valid = valid;
  pte.protected = protected;
  pte.present = present;
  pte.dirty = dirty;
  pte.user_kernel = user_kernel;
  pte.read = read;
  pte.write = write;
  pte.execute = execute;

  }*/

void main(){
  struct page_table_entry *page_table;
  page_table = (struct page_table_entry*)malloc(sizeof(struct page_table_entry) * 64);
  int *random_num;
  int i;
  random_num = random_integers(64,16777216);
  for (i = 0; i < 64; i++){
    page_table[i].frame_number = random_num[i];
    //printf("%d\n",page_table[i].frame_number );
  }

  page_table[20].frame_number = 16777215; 
  //20480 is the virtual address for vpn 20
  int t = extract_vpn(20480);
  int f = extract_offset(20480);
  int fn = get_frame_number(page_table,20480);
  int ph = get_physical_address(fn,f);
  printf("The virtual address:  %zu\n",to_binary(20480) );
  printf("VPN:  %zu\n",to_binary(t));
  printf("Offset:  %zu\n",to_binary(f));
  printf("Frame number:  %zu\n",to_binary(fn));
  printf("Physical address:  %zu\n",to_binary(ph));
 
}


