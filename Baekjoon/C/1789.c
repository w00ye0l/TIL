#include <stdio.h>
int main(){
	long s;
	scanf("%d", &s);
	
	long re=0;
	long start=1;
	long end=s;
	
	while(start<=end){
		long mid=(start+end)/2;
		printf("mid:%d\n", mid);
		if(mid*(mid+1)/2 <= s){
			re=mid;
			start=mid+1;
		}else{
			end=mid-1;
		}
	}
	printf("%d", re);
}
