#include <stdio.h>
#include <math.h>
int main(){
	int i=0;
	while(1){
		i++;
		double a, b, c;
		scanf("%lf %lf %lf", &a, &b, &c);
		
		if(a==0 && b==0 && c==0)
			break;
		
		printf("Triangle #%d\n", i);
		if(c==-1){
			c=sqrt(pow(a,2)+pow(b,2));
			printf("c = %.3lf\n\n", c);
		}else if(a==-1){
			if(pow(c,2)>pow(b,2)){
				a=sqrt(pow(c,2)-pow(b,2));
				printf("a = %.3lf\n\n", a);
			}
			else{
				printf("Impossible.\n\n");
			}
		}else if(b==-1){
			if(pow(c,2)>pow(a,2)){
				b=sqrt(pow(c,2)-pow(a,2));
				printf("b = %.3lf\n\n", b);
			}
			else{
				printf("Impossible.\n\n");
			}
		}
	}
}
