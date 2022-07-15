#include <stdio.h>
#include <stdlib.h>
int nArr[100000];
int mArr[100000];

int bs(int arr[], int key, int size){
	int first=0;
	int last=size-1;
	int middle;
	
	while(first<=last){
		middle=(first+last)/2;
		
		if(arr[middle]==key)
			return 1;
		
		if(arr[middle]<key)
			first=middle+1;
		else
			last=middle-1;
	}
	return 0;
}

int compare(const void* a, const void* b){
	return *(int*)a>* (int*)b?1:(*(int*)a<*(int*)b?-1:0);
}

int main(){
	int n;
	scanf("%d", &n);
	for(int i=0; i<n; i++){
		scanf("%d", &nArr[i]);
	}
	
	int m;
	scanf("%d", &m);
	for(int i=0; i<m; i++){
		scanf("%d", &mArr[i]);
	}
	
	qsort(nArr, n, sizeof(int), compare);
	
	for(int i=0; i<m; i++){
		printf("%d\n", bs(nArr, mArr[i], n));
	}
}
