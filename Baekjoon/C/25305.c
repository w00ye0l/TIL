#include <stdio.h>
#include <stdlib.h>
int arr[1001];

int compare(const void* a, const void* b){
	return *(int *)b-*(int *)a;
}

int main(){
	int n, k;
	scanf("%d %d", &n, &k);
	
	for(int i=0; i<n; i++){
		scanf("%d", &arr[i]);
	}
	
	qsort(arr, n, sizeof(int), compare);
	
	printf("%d", arr[k-1]);
}
