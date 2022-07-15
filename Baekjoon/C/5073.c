#include <stdio.h>
int main(){
	while(1){
		int a, b, c;
		scanf("%d %d %d", &a, &b, &c);
		
		if(a==0 && b==0 && c==0){
			break;
		}
		
		int max=a;
		if(max<b){
			if(b<c){
				max=c;
			}else{
				max=b;
			}
		}else{
			if(max<c){
				max=c;
			}
		}
		
		if(a+b+c-max<=max){
			printf("Invalid\n");
		}else if(a==b && b==c && a==c){
			printf("Equilateral\n");
		}else{
			if(a!=b && b!=c && a!=c){
				printf("Scalene\n");
			}else{
				printf("Isosceles\n");
			}
		}
	}
}
