#include <stdio.h>
int main(){
	while(1){
		int a, b, n=0;
		scanf("%d %d", &a, &b);
		
		if((a==0) && (b==0))
			return 0;
		
		if(a<b){
			for(int i=1; a*i<=b; i++){
				if(a*i==b){
					n=1;
					break;
				}
			}
		}else if(a>b){
			for(int i=1; b*i<=a; i++){
				if(b*i==a){
					n=2;
					break;
				}
			}
		}
		if(n==0)
			printf("neither\n");
		else if(n==1)
			printf("factor\n");
		else if(n==2)
			printf("multiple\n");
	}
}
