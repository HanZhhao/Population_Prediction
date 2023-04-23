#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void cal_short(void){
 for(int k1=0; k1 <= 6; k1++){
  float result = 0.7245*sqrt(k1) + 0.2039*sqrt(6-k1);
  printf("k1=%d、k2=%d的时候, 结果为%f\n", k1, 6-k1, result);
 }
}
void cal_long(void){
 float max=0;
 int k1_m, k2_m, k3_m;
 for(int k1=0; k1 <= 6; k1++){
  for(int k2=0; k2 <= 6-k1; k2++){
   double result = pow(0.95, -0.7245*sqrt(k1) - 0.2039*sqrt(k2))*pow(0.2*log(20)/pow(6-k1-k2+1,0.25), - 0.2039);
   if(result > max){
    max = result;
    k1_m = k1;
    k2_m = k2;
    k3_m = 6 - k1 - k2;
   }
   printf("k1=%d、k2=%d、k3=%d的时候, 结果为%lf\n", k1, k2, 6-k1-k2, result);
  }
 }
 printf("当k1=%d,k2=%d,k3=%d时，生育意愿取到最大值",k1_m,k2_m,k3_m);
}

int main(){
 cal_short();
}
