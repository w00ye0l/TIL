#include <stdio.h>
int main(){
	int n, max=0, sn=0;
	scanf("%d", &n);
	
	int arr[10]={0,};
	
	while(n>0){
		int k=n%10;
		arr[k]++;
		n/=10;
	}
	
	for(int i=0; i<10; i++){
		if(i!=6 && i!=9 && max<arr[i])
			max=arr[i];
	}
	
	if((arr[6]+arr[9])%2!=0){
		sn=(arr[6]+arr[9])/2+1;
	}else{
		sn=(arr[6]+arr[9])/2;
	}
	
	if(max<sn){
		max=sn;
	}
	printf("%d", max);
}
