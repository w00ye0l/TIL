#include <stdio.h>

int arr[1000000]={0};

void primeChk(){
	for(int i=2; i*i<=1000000; i++){
		if(arr[i]==0){
			for(int j=i*i; j<=1000000; j+=i){
				arr[j]=1;
			}
		}
	}
}

int main(){
	int n;
	primeChk();
	
	while(1){
		scanf("%d", &n);
		if(n==0)
			break;
		
		int a=0;
		
		for(int i=3; i<=n/2; i+=2){
			if(arr[i]==0 && arr[n-i]==0){
				printf("%d = %d + %d\n", n, i, n-i);
				a++;
				break;
			}
		}
		if(a==0)
			printf("Goldbach's conjecture is wrong.\n");
	}
}
