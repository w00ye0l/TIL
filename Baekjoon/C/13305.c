#include <stdio.h>
long long dis[100001]={0};
long long pri[100001]={0};
int main(){
	long long n, cnt=0;
	scanf("%lld", &n);
	
	for(int i=0; i<n-1; i++){
		scanf("%lld", &dis[i]);
	}
	
	for(int i=0; i<n; i++){
		scanf("%lld", &pri[i]);
	}
	
	cnt+=dis[0]*pri[0];
	long long price=pri[0];
	
	for(int i=1; i<n-1; i++){
		if(pri[i]<price){
			price=pri[i];
		}
		
		cnt+=price*dis[i];
	}
	
	printf("%lld", cnt);
}
