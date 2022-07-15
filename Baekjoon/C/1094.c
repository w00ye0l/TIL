#include <stdio.h>
int main(){
	int x, count=0;
	scanf("%d", &x);
	
	int arr[7]={64, 32, 16, 8, 4, 2, 1};
	for(int i=0; i<7; i++){
		if(x>=arr[i]){
			x-=arr[i];
			count++;
		}
		if(x==0){
			printf("%d", count);
			return 0;
		}
	}
}
