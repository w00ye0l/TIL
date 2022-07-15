#include <stdio.h>
int main(){
	int n;
	scanf("%d", &n);
	
	int five=n/5;
	int r=n%5;
	int cnt=0;
	
	if(r%2==1){
		five--;
		r+=5;
	}
	if(five<0){
		printf("-1");
	}
	else{
		cnt=five+r/2;
		printf("%d", cnt);
	}
}
