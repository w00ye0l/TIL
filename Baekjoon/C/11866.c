#include <stdio.h>
int main(){
	int n, k;
	scanf("%d %d", &n, &k);
	
	int arr[n+1];
	for(int i=0; i<n; i++){
		arr[i]=i+1;
	}
	int re[n+1];
	
	int zero=0, cnt=0, ch=0;
	
	while(1){
		for(int i=0; i<n; i++){
			if(arr[i]==0){
				zero++;
			}
			
		}
		if(zero==n){
			break;
		}
		
		/*if((ch+1)%k==0){
			re[cnt]=arr[ch];
			arr[ch]=0;
			cnt++;
		}else{
			ch++;
		}*/
	}
	
	for(int i=0; i<n; i++){
		printf("%d, ", re[i]);
	}
}
