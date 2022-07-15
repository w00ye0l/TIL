#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct{
	int age;
	char name[101];
	int idx;
} human;

human sort[100000];

void merge(human* arr, int first, int mid, int last){
	int i=first;
	int j=mid+1;
	int k=first;
	
	while(i <= mid && j <= last){
		if(arr[i].age < arr[j].age)
			sort[k++]=arr[i++];
		else if(arr[i].age > arr[j].age)
			sort[k++]=arr[j++];
		else{
			if(arr[i].idx < arr[j].idx)
				sort[k++]=arr[i++];
			else
				sort[k++]=arr[j++];
		}
	}
	
	if(i > mid){
		while(j <= last)
			sort[k++]=arr[j++];
	}else{
		while(i <= mid)
			sort[k++]=arr[i++];
	}
	for(k=first; k<=last; k++){
		arr[k]=sort[k];
	}
}

void mergesort(human* arr, int first, int last){
	int mid;
	
	if(first<last){
		mid=(first+last)/2;
		mergesort(arr, first, mid);
		mergesort(arr, mid+1, last);
		merge(arr, first, mid, last);
	}
}

int main(){
	int n;
	scanf("%d", &n);
	
	human member[n];
	
	for(int i=0; i<n; i++){
		scanf("%d %s", &member[i].age, member[i].name);
		member[i].idx=i;
	}
	
	mergesort(member, 0, n-1);
	
	for(int i=0; i<n; i++){
		printf("%d %s\n", member[i].age, member[i].name);
	}
}
