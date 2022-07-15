#include <stdio.h>
int main(){
	int n;
	scanf("%d", &n);
	
	int i=1;
	while(i<=n){
		int a, b, c, max;
		scanf("%d %d %d", &a, &b, &c);
		
		int check=a*a+b*b+c*c;
		
		if(a>b){
			if(a>c)
				max=a;
			else
				max=c;
		}else{
			if(b>c)
				max=b;
			else
				max=c;
		}
		printf("Scenario #%d: \n", i);
		if(check-max*max==max*max){
			printf("yes\n\n");
		}else{
			printf("no\n\n");
		}
		i++;
	}
}
