#include <stdio.h>
#include <stdlib.h>
int compare(const void *a, const void *b){
	int first=*(int *)a;
	int second=*(int *)b;
	
	if(first<second){
		return 1;
	}else if(first>second){
		return -1;
	}else{
		return 0;
	}
}

int main(){
	int n;
	scanf("%d", &n);
	
	int arr[n];
	for(int i=0; i<n; i++){
		scanf("%d", &arr[i]);
	}
	qsort(arr, sizeof(arr)/sizeof(int), sizeof(int), compare);
	
	long long sum=arr[0]*1;
	for(int i=0; i<n; i++){
		if(sum<arr[i]*(i+1))
			sum=arr[i]*(i+1);
	}
	printf("%d", sum);
}
