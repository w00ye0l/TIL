#include <stdio.h>
long long stack[100000]={0};
int top=-1;

int main(){
	int k;
	long long sum=0;
	scanf("%d", &k);
	
	while(k--){
		long long n;
		scanf("%lld", &n);
		
		if(n==0){
			stack[top]=0;
			top--;
			continue;
		}
		top++;
		stack[top]=n;
	}

	for(int i=0; i<=top; i++){
		sum+=stack[i];
	}
	
	printf("%d", sum);
}
