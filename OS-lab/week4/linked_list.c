#include <stdlib.h>
#include <stdio.h>

struct node {
  int x;
  struct node *next;
};

struct node * find(struct node *root, int value ) {
  if (root -> x == value){
    return root;

  }
  else {
    if (root -> next != 0){
      find ((root -> next), value);
  
    }
    else{
      struct node *notfound;
      notfound = (struct node *) malloc( sizeof(struct node) );
      notfound->next = 0;
      notfound->x = 666;  
      return notfound;

    }

  }

}
void printlinkedlist(struct node *root){
  printf("%d\n",root->x );
  if (root->next != 0){
    root = root->next;
    printlinkedlist(root);
  }

}

                
void insert(struct node *root, int pos, int value){
  int count = 0;
  int flag = 0;
  struct node *temp, *new, *curr = root;
  new = (struct node *) malloc( sizeof(struct node) );
  if (pos == 0){
    pos = 1;
    flag = 1;
  }
  while (pos-1 != count){
    curr = curr->next;
    count ++;
  }
  new->x = value;
  temp = curr->next;
  curr->next = new;
  new->next = temp;
  if (flag == 1){
    int t = root->x;
    root->x = (root->next)->x;
    (root->next)->x = t;
  
  }
  
  }
  
//delete a node
void delete(struct node *root, int pos){
  int count = 0, flag = 0;
  struct node *temp, *curr = root;
  if (pos == 0){
    pos = 1;
    flag = 1;
  }
  if (flag == 1){
    int t = root->x;
    root->x = (root->next)->x;
    (root->next)->x = t;
  }

  while (pos-1 != count){
    curr = curr->next;
    count ++;
  }
  temp = curr->next;
  curr->next = (curr->next)->next;
  free(temp);
}




// delete entire list
void delete_all(struct node *root){
  struct node *temp, *curr = root;
  while (curr->next != 0){
    temp = curr->next;
    free(curr);
    curr = temp;

  }
  
  free(curr);


}
               

int main()
 
{   int val,ch;
    int value,pos,ex = 0;
    printf("Initializing:\n");
    printf("Enter the value of the first element in the linked list:\n" );
    scanf("%d",&val);
    struct node *root;      
    root = (struct node *) malloc( sizeof(struct node) ); 
    root->next = 0;
    root->x = val;
    while (ex == 0){
      printf("----------------------------------\n");
      printf("1: Insert\n");
      printf("2: Find\n");
      printf("3: Delete Element\n");
      printf("4: Delete List\n");
      printf("5: Print List\n");
      printf("6: Exit\n");
      printf("----------------------------------\n");
      printf("Enter your choice\n");
      scanf("%d",&ch);
      switch(ch){
        case 1: {
          int value,pos;
          printf("Enter the value to be inserted\n");
          scanf("%d",&value);
          printf("Enter the position to be inserted\n");
          scanf("%d",&pos);
          insert(root,pos,value);
          break;
    }
      
        case 2: {
          int value;
          printf("Enter the value to be searched\n");
          scanf("%d",&value);
          struct node *a = find(root,value);
          if ((a->x == 666) && (a->next == 0)){
            printf("%d not found\n",value);
          }
          else {
            printf("%p Element found :\n",a );
          }
          break;
    }
        case 3: {
          int pos;
          printf("Enter the position to be deleted\n");
          scanf("%d",&pos);
          delete(root,pos);
          break;
    }
        case 4: {
          delete_all(root);
          break;
    }
        case 5: {
          printf("Linked list:\n");
          printlinkedlist(root);
          printf("***********************************\n");
          break;
    }
        case 6: {
          ex = 1;
          break;
    }

      }
    }


}
