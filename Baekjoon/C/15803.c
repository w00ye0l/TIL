#include <stdio.h>
int main(){
	int x[4];
	int y[4];
	
	for(int i=0; i<3; i++){
		scanf("%d %d", &x[i], &y[i]);
	}
	
	if((y[1]-y[0])*(x[2]-x[0])==(y[2]-y[0])*(x[1]-x[0])){
		printf("WHERE IS MY CHICKEN?");
	}else{
		printf("WINNER WINNER CHICKEN DINNER!");
	}
}
