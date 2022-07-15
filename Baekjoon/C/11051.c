#include <stdio.h>

int arr[1001][1001]={0};

int main(){
	int n, k;
	scanf("%d %d", &n, &k);
	
	
	for(int i=1; i<=n; i++){
		for(int j=0; j<=i; j++){
			if(i==j || j==0){
				arr[i][j]=1;
			}else{
				arr[i][j]=(arr[i-1][j-1]+arr[i-1][j])%10007;
			}
		}
	}
	printf("%d", arr[n][k]);
}
