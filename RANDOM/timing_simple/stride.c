/* stride.c
   Stride access pattern: walks an array with a fixed stride (in bytes).
   Compile: gcc -O0 -static -o stride stride.c
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define SIZE 1000
int arr[SIZE];
int main(){
  int sum=0;
  for(int i=0;i<100000;i++){
    for(int j=0;j<64;j++){
     sum+=arr[(j+i)%64];
    }
  }
  printf("%d\n",sum);
  return 0;
}

