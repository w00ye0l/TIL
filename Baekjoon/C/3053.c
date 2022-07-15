#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h>
int main(){
	int r;
	scanf("%d", &r);
	
	printf("%6f\n", M_PI*r*r);
	printf("%6f", (double)2*r*r);
} 
