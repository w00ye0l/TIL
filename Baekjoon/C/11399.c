#include <stdio.h>
#include <stdlib.h>
int compare(const void *a, const void *b){
	return *(int *)a-*(int *)b;
}

int main(){
	int n, sum=0;
	scanf("%d", &n);
	int t[n];
	
	for(int i=0; i<n; i++){
		scanf("%d", &t[i]);
	}

	qsort(t, sizeof(t)/sizeof(int), sizeof(int), compare);
		
	for(int i=1; i<=n; i++){
		for(int j=0; j<i; j++){
			sum+=t[j];
		}
	}
	
	printf("%d", sum);
}
