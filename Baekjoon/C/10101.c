#include <stdio.h>
int main(){
	int a, b, c;
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);
	
	if(a+b+c!=180){
		printf("Error");
	}else{
		if(a==b){
			if(a!=c){
				printf("Isosceles");
			}else{
				printf("Equilateral");
			}
		}else{
			if(a==c){
				printf("Isosceles");
			}else if(b==c){
				printf("Isosceles");
			}else{
				printf("Scalene");
			}
		}
	}
}
