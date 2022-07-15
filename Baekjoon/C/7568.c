#include <stdio.h>
int main(){
	int num;
	scanf("%d", &num);
	
	int arr[num][2];
	for(int i=0; i<num; i++){
		scanf("%d %d", &arr[i][0], &arr[i][1]);
	}
	
	int rank[num];
	for(int i=0; i<num; i++){
		rank[i]=1;
	}

	for(int i=0; i<num; i++){
		for(int j=i+1; j<num; j++){
			if(arr[i][0]<arr[j][0] && arr[i][1]<arr[j][1])
				rank[i]++;
			else if(arr[i][0]>arr[j][0] && arr[i][1]>arr[j][1])
				rank[j]++;
		}
	}
	for(int i=0; i<num; i++){
		printf("%d ", rank[i]);
	}
}
