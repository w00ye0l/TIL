#include <stdio.h>
int main(){
	int n;
	scanf("%d", &n);
	
	for(int i=0; i<n; i++){
		for(int j=i+1; j>0; j--){
			printf("*");
		}
		printf("\n");
	}
	for(int i=n-1; i>0; i--){
		for(int j=i; j>0; j--){
			printf("*");
		}
		printf("\n");
	}
}
