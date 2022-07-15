#include <stdio.h>
#define MAX 81
long long arr[81]={0};
int main(){
	int n;
	scanf("%d", &n);
	
	arr[1]=1;
	arr[2]=1;
	for(int i=3; i<=n; i++){
		arr[i]=arr[i-1]+arr[i-2];
	}
	
	long long round=0;
	
	if(n==1){
		round=arr[1]*4;
	}else if(n==2){
		round=arr[1]*3+(arr[2]*3);
	}else if(n==3){
		round=(arr[1]*2)+(arr[2]*2)+(arr[3]*3);
	}else{
		round=(arr[n]*3)+(arr[n-1]*2)+(arr[n-2]*2)+arr[n-3];
	}
	
	printf("%lld", round);
}
