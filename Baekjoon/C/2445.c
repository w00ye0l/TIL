#include <stdio.h>
int main(){
	int n;
	scanf("%d", &n);
	
	for(int i=1; i<n; i++){
		for(int j=0; j<i; j++){
			printf("*");
		}
		for(int k=2*(n-i); k>0; k--){
			printf(" ");
		}
		for(int j=0; j<i; j++){
			printf("*");
		}
		printf("\n");
	}
	for(int i=n; i>0; i--){
		for(int j=i; j>0; j--){
			printf("*");
		}
		for(int k=2*(n-i); k>0; k--){
			printf(" ");
		}
		for(int j=i; j>0; j--){
			printf("*");
		}
		printf("\n");
	}
}
