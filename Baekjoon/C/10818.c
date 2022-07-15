#include <stdio.h>
#include <stdlib.h>
int compare(const void* a, const void* b){
	return *(int *)a>*(int *)b?1:(*(int *)a<*(int *)b?-1:0);
}

int main(){
	int num;
	scanf("%d", &num);
	
	int arr[num];
	for(int i=0; i<num; i++){
		scanf("%d", &arr[i]);
	}
	
	qsort(arr, num, sizeof(int), compare);
	
	printf("%d %d", arr[0], arr[num-1]);
}
