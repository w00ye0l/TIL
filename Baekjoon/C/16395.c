#include <stdio.h>
int main(){
	int n, k;
	scanf("%d %d", &n, &k);
	
	int arr[31][31]={0};
	
	for(int i=0; i<n; i++){
		arr[i][0]=1;
	}
	
	for(int i=1; i<n; i++){
		for(int j=1; j<=i; j++){
			arr[i][j]=arr[i-1][j-1]+arr[i-1][j];
		}
	}
	
	printf("%d", arr[n-1][k-1]);
}
