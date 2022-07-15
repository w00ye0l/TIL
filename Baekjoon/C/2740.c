#include <stdio.h>
int main(){
	int n, m, k;
	scanf("%d %d", &n, &m);
	int arr1[n][m];
	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			scanf("%d", &arr1[i][j]);
		}
	}
	
	scanf("%d %d", &m, &k);
	int arr2[m][k];
	for(int i=0; i<m; i++){
		for(int j=0; j<k; j++){
			scanf("%d", &arr2[i][j]);
		}
	}
	
	for(int i=0; i<n; i++){
		for(int j=0; j<k; j++){
			int sum=0;
			for(int l=0; l<m; l++){
				sum+=arr1[i][l]*arr2[l][j];
			}
			printf("%d ", sum);
		}
		printf("\n");
	}
}
