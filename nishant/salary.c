#include<stdio.h>
void main()
{
  int grossal;
  double DA,HRA,IT,PF,TA;
  printf("Enter Emp grossal:\n");
  scanf("%d",&grossal);
  DA= grossal*0.5;
  HRA= grossal*0.4;
  IT= grossal*0.2;
  PF= grossal*0.9;
  TA= grossal*0.75;
  double totsal=DA+HRA+IT+PF+TA;
  printf(".................********...............");
  printf("DA is:%lf\n",DA );
  printf("HRA is:%lf\n",HRA );
  printf("IT is:%lf\n",IT );
  printf("PF is:%lf\n",PF );
  printf("TA is:%lf\n",TA );
  printf("totsal is:%lf\n",totsal);
}
