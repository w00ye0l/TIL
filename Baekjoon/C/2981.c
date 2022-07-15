#include <stdio.h>
#include <stdlib.h>
int compare(const void* a, const void* b){
	int f=*(int *)a;
	int s=*(int *)b;
	
	if(f>s)
		return 1;
	else if(f<s)
		return -1;
	else
		return 0;
}
int main(){
	int n;
	scanf("%d", &n);
	
	long long arr[n];
	for(int i=0; i<n; i++){
		scanf("%lld", &arr[i]);
	}
	
	qsort(arr, sizeof(arr)/sizeof(int), sizeof(int), compare);
	
	for(int i=1; i<n; i++){
		for(int j=0; j<arr[0]; j++){
			mod=arr[j]%i;
		}
	}
}
