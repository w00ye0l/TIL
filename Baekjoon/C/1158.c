#include <stdio.h>
int main(){
	int n, k, cnt=0;
	scanf("%d %d", &n, &k);
	int arr[n];
	
	for(int i=0; i<n; i++){
		arr[i]=i+1;
	}
	
	int t=k-1;
	printf("<%d", arr[t]);
	arr[t]=0;
	
	for(int i=0; i<n-1; i++){
		while(1){
			t++;
			if(t==n){
				t-=n;
			}
			if(arr[t]!=0){
				cnt++;
			}
			if(cnt==k){
				printf(", %d", arr[t]);
				arr[t]=0;
				cnt=0;
				break;
			}
		}
	}
	printf(">");
}
