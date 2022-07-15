#include <stdio.h>
int main(){
	int n;
	scanf("%d", &n);
	
	for(int i=0; i<n-1; i++){
		for(int j=i; j>0; j--){
			printf(" ");
		}
		for(int k=2*(n-i)-1; k>0; k--){
			printf("*");
		}
		printf("\n");
	}
	
	for(int i=1; i<n+1; i++){
		for(int j=n-i; j>0; j--){
			printf(" ");
		}
		for(int k=2*i-1; k>0; k--){
			printf("*");
		}
		printf("\n");
	}
}
