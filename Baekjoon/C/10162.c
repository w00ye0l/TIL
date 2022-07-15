#include <stdio.h>
int main(){
	int t;
	scanf("%d", &t);
	
	int a=0, b=0, c=0;
	while(t){
		if(t>=300){
			a++;
			t-=300;
		}else if(t>=60){
			b++;
			t-=60;
		}else if(t>=10){
			c++;
			t-=10;
		}else{
			printf("-1");
			return 0;
		}
	}
	printf("%d %d %d", a, b, c);
}
