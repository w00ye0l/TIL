#include <stdio.h>
int main(){
	int n;
	scanf("%d", &n);
	
	for(int i=1; i<=n; i++){
		for(int j=n-i; j>0; j--){
			printf(" ");
		}
		for(int k=1; k<=2*i-1; k++){
			printf("*");
		}
		printf("\n");
	}
	for(int i=1; i<n; i++){
		for(int j=0; j<i; j++){
			printf(" ");
		}
		for(int k=2*(n-i)-1; k>0; k--){
			printf("*");
		}
		printf("\n");
	}
}
