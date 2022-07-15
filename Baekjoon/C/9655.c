#include <stdio.h>
int main(){
	int n;
	scanf("%d", &n);
	
	int a, b;
	a=n/3;
	b=n%3;
	
	if((a+b)%2==0){
		printf("CY");
	}else{
		printf("SK");
	}
}
