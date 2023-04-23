#include <stdio.h>
int main(){
FILE* p=fopen("新建文本文档.txt","r");
 
double People[90][3]={0};//起始人口 
double tmpPeople[90][3]={0};
double SYL[90][3]={0};//各个年龄段生育率 
double SWL[90][3]={0};
double Qianyi[90][6]={0};
double a;
for(int n=0;n<3;n++){
 for(int i=0;i<90;i++){
 fscanf(p,"%lf",&People[i][n]);
 }
}
for(int n=0;n<3;n++){
for(int i=0;i<90;i++){
 fscanf(p,"%lf",&SYL[i][n]);
}
}
for(int n=0;n<3;n++){
for(int i=0;i<90;i++){
 fscanf(p,"%lf",&SWL[i][n]);
}
}
for(int n=0;n<6;n++){
for(int i=0;i<90;i++){
 fscanf(p,"%lf",&Qianyi[i][n]);
}
}
for(int n=0;n<3;n++){
for(int i=0;i<90;i++){
 
 SYL[i][n]/=1000.0; 
 SWL[i][n]/=1000.0;
 
}
}
for(int n=0;n<6;n++){
for(int i=0;i<90;i++){
 Qianyi[i][n]/=100.0;
}
}
//各个年龄段死亡率 
 for(int i=0;i<50;i++){//50年 
  for(int n=0;n<3;n++){
   double T=0;
   for(int m=0;m<90;m++){
   T+=People[m][n]*SYL[m][n];
  }
   tmpPeople[0][n]=T;
   for(int m=0;m<89;m++){
   tmpPeople[m+1][n]=People[m][n]*(1-SWL[m][n]);
  }
  for(int m=0;m<90;m++){
   People[m][n]=tmpPeople[m][n];
  }
   
  }
  for(int n=0;n<3;n++){
   for(int m=0;m<90;m++){
   if(n==0){
    
    People[m][n]=People[m][n]+tmpPeople[m][2]*Qianyi[m][2]+tmpPeople[m][1]*Qianyi[m][3];
    People[m][n]=People[m][n]-tmpPeople[m][0]*Qianyi[m][0]-tmpPeople[m][0]*Qianyi[m][5];
   }
   else if(n==1){
    People[m][n]=People[m][n]+tmpPeople[m][2]*Qianyi[m][4]+tmpPeople[m][0]*Qianyi[m][0];
    People[m][n]=People[m][n]-tmpPeople[m][1]*Qianyi[m][1]-tmpPeople[m][1]*Qianyi[m][3];
   }
   else if(n==2){
    People[m][n]=People[m][n]+tmpPeople[m][0]*Qianyi[m][5]+tmpPeople[m][1]*Qianyi[m][1];
    People[m][n]=People[m][n]-tmpPeople[m][2]*Qianyi[m][2]-tmpPeople[m][2]*Qianyi[m][4];
   }
   
  }
  
  }
  printf("Year:%d\n",i);
 for(int n=0;n<3;n++){
 printf("City:%d\n",n);
 double TotalP=0.0;
 for(int i=0;i<90;i++){
  
  TotalP+=People[i][n];
 }
 printf("%lf \n",TotalP);
 
 }
  
 }
  
  
  //printf("\n");
 
 

 return 0;}
