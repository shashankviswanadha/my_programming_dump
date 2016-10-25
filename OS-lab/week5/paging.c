#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <signal.h>

long to_binary(long decimal){
  int count = 0;
  long bin = 0;
  while (decimal > 1){
    bin = bin + (long)((decimal % 2) * (long)pow (10,count));
    decimal = decimal/2;
    count++;
  }
  bin = bin + (long)((decimal % 2) * (long)pow (10,count));
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


struct tlb_entry{
  int vpn,pfn,valid,read,write,execute;
};

struct page_directory_entry{
  int pte_address,valid;
};

int extract_vpn(int virtual_address){
  int VPN_MASK = 64512;
  int SHIFT = 10;
  //Extract the VPN from the virtual address  
  int VPN = (virtual_address & VPN_MASK) >> SHIFT;
  return VPN;
}

int extract_pdi(int vpn){
  int PDI_MASK = 60;
  int SHIFT = 2;
  int PDI = (vpn & PDI_MASK) >> SHIFT;
  return PDI;
}


int extract_pte_offset(int virtual_address){
  int MASK = 3072;
  int SHIFT = 10;
  int PDI = (virtual_address & MASK) >> SHIFT;
  return PDI;
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

int access_memory(struct page_table_entry *pte,int virtual_address){  //access directly from page table
  int vpn = extract_vpn(virtual_address);
  int off = extract_offset(virtual_address);
  int fn,pa;
  if (pte[vpn].valid == 0){
    //raise(SIGSEGV);
    //RaiseException(SEGMENTATION_FAULT);
  }
  else{
    fn = get_frame_number(pte,virtual_address);
    pa = get_physical_address(fn,off);
    return pa;  
  }

}

int access_mem(struct tlb_entry *tl,struct page_table_entry *pte,int virtual_address){//access from TLB
  int vpn = extract_vpn(virtual_address);
  int off = extract_offset(virtual_address);
  int fn,pa;
  int i;
  for (i = 0; i<16; i++){
    if (pte[vpn].valid == 0){
    //raise(SIGSEGV);
    //RaiseException(SEGMENTATION_FAULT);
    }
    else{
      if (tl[i].vpn == vpn){
        //printf("%d%s\n",tl[i].vpn,"yoo" );
        return get_physical_address(tl[i].pfn,off);
      }
    }
  }
  if (pte[vpn].valid != 0){
    fn = get_frame_number(pte,virtual_address);
    int j;
    for (j = 0;j <15; j++){
      tl[j] = tl[j+1];
    }
    tl[15].vpn = vpn;
    tl[15].pfn = fn;
    //printf("%d%s\n",tl[15].vpn,"yoyo");
    
    //raise(SIGSEGV);
    //RaiseException(SEGMENTATION_FAULT);
    
    return get_physical_address(tl[15].pfn,off);
  }
}

int AccessMemory(struct page_directory_entry *pd,struct tlb_entry *tl,struct page_table_entry *pte,int virtual_address){
  int vpn = extract_vpn(virtual_address);
  int off = extract_offset(virtual_address);
  int fn,pa;
  int i;
  for (i = 0; i<16; i++){
    if (pte[vpn].valid == 0){
    //raise(SIGSEGV);
    //RaiseException(SEGMENTATION_FAULT);
    }
    else{
      if (tl[i].vpn == vpn){
        //printf("%d%s\n",tl[i].vpn,"yoo" );
        return get_physical_address(tl[i].pfn,off);
      }
    }
  }
  int pdi = extract_pdi(vpn);
  printf("%s%d\n","pdi:",pdi );
  if (pd[pdi].valid == 0){
    //raise(SIGSEGV);
    //RaiseException(SEGMENTATION_FAULT);

  }
  else {
    int pte_off = extract_pte_offset(virtual_address);
    printf("pteoff:%d\n",pte_off);
    int pti = pd[pdi].pte_address + pte_off;
    printf("pti:%d\n",pti );
    fn = get_frame_number(pte,virtual_address);
    if (pte[pti].valid != 0){
      int j;
      for (j = 0;j <15; j++){
        tl[j] = tl[j+1];
      }
      tl[15].vpn = pti;
      tl[15].pfn = fn;
      //printf("%d%s\n",tl[15].vpn,"yoyo");
      
      //raise(SIGSEGV);
      //RaiseException(SEGMENTATION_FAULT);
      return get_physical_address(tl[15].pfn,off);
    }

    
  }
  

}
  

void main(){
  struct page_table_entry *page_table;
  struct tlb_entry *tlb;
  struct page_directory_entry *page_dir;
  page_table = (struct page_table_entry*)malloc(sizeof(struct page_table_entry) * 64);
  tlb = (struct tlb_entry*)malloc(sizeof(struct tlb_entry) * 16);
  page_dir = (struct page_directory_entry*)malloc(sizeof(struct page_directory_entry) * 16);
  int *random_num;
  int i;
  random_num = random_integers(64,64); //6
  for (i = 0; i < 64; i++){
    page_table[i].frame_number = random_num[i];
    //printf("%d\n",page_table[i].frame_number );
  }
  int j = 0;
  int c ;
  for (c = 0; c < 16 ; c++){
    page_dir[c].pte_address = j;
    j = j + 4;
  }

  page_table[20].frame_number = 50; 
  page_table[20].valid = 1;
  page_table[21].frame_number = 51;
  page_table[21].valid = 1;

  int k,l;
  for(k = 0; k < 16; k++){
    int flag = 0;
    for (l = 0; l < 4; l++){
      if (page_table[(4*k)+l].valid == 1){
        page_dir[k].valid = 1;
        flag = 1;
        break;
      }
    }
    if (flag == 0){
      page_dir[k].valid = 0;
    }
  }


  //20480 is the virtual address for vpn 20
  int ph = AccessMemory(page_dir,tlb,page_table,20480);
  int tr = AccessMemory(page_dir,tlb,page_table,21504);
  //long t = (long)extract_vpn(20481);
  //long f = (long)extract_offset(20481);
  //long fn = (long)get_frame_number(page_table,20481);
  //long ph = (long)get_physical_address(fn,f);
  //printf("The virtual address:  %zu\n",to_binary(20481) );
  //printf("VPN:  %zu\n",to_binary(t));
  //printf("Offset:  %zu\n",to_binary(f));
  //printf("Frame number:  %zu\n",to_binary(fn));
  printf("Physical address:  %zu\n",to_binary(ph));
  int t = AccessMemory(page_dir,tlb,page_table,20480);
  printf("Physical address:  %zu\n",to_binary(tr));
  //printf("%d%s\n",tlb[14].vpn,"oooo");
}


