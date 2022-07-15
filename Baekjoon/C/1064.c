#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int compare(const void *a, const void *b){		// double qsort Áß¿ä! 
	return (*(double *)b-*(double *)a>0)?1:-1;
}

int main(){
	double x[4], y[4];
	for(int i=0; i<3; i++){
		scanf("%lf %lf", &x[i], &y[i]);
	}
	
	if((y[1]-y[0])*(x[2]-x[0])==(y[2]-y[0])*(x[1]-x[0])){
		printf("-1.0");
	}else{
		double len[3];
		for(int i=0; i<3; i++){
			if(i==2){
				len[i]=sqrt(pow(x[i]-x[0],2)+pow(y[i]-y[0],2));
			}else{
				len[i]=sqrt(pow(x[i]-x[i+1],2)+pow(y[i]-y[i+1],2));
			}
		}
		
		qsort(len, sizeof(len)/sizeof(double), sizeof(double), compare);
		
		printf("%.15lf", 2*(len[0]-len[2]));
	}
}
