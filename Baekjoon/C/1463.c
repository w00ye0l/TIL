#include <stdio.h>
int compare(int a, int b){
	if(a>=b){
		return b;
	}else{
		return a;
	}
}
int main(){
	int n, tmp;
	scanf("%d", &n);
	
	int arr[n+1];
	for(int i=0; i<=n; i++){
		arr[i]=0;
	}
	
	for(int i=2; i<=n; i++){
		arr[i]=arr[i-1]+1;
		if(i%3==0){
			tmp=arr[i/3]+1;
			arr[i]=compare(arr[i], tmp);
		}
		if(i%2==0){
			tmp=arr[i/2]+1;
			arr[i]=compare(arr[i], tmp);
		}
	}
	printf("%d", arr[n]);
}
