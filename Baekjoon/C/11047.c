#include <stdio.h>
int main(){
	int n, k, cnt=0;
	scanf("%d %d", &n, &k);
	
	int coin[n];
	for(int i=n-1; i>=0; i--){
		scanf("%d", &coin[i]);
	}
	
	for(int i=0; i<n; i++){
		if(k/coin[i]!=0){
			cnt+=k/coin[i];
			k=k%coin[i];
		}
	}
	
	printf("%d", cnt);
}
