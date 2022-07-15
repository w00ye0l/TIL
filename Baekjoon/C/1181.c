#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct{
	char name[51];
	int len;
} word;

word sort[20001];

void merge(word* arr, int first, int mid, int last){
	int i=first;
	int j=mid+1;
	int k=first;
	
	while(i<=mid && j<=last){
		if(arr[i].len < arr[j].len)
			sort[k++]=arr[i++];
		else if(arr[i].len > arr[j].len)
			sort[k++]=arr[j++];
		else{
			if(strcmp(arr[i].name, arr[j].name)<0)
				sort[k++]=arr[i++];
			else
				sort[k++]=arr[j++];
		}
	}
	if(i>mid){
		while(j<=last)
			sort[k++]=arr[j++];
	}else{
		while(i<=mid)
			sort[k++]=arr[i++];
	}
	for(k=first; k<=last; k++)
		arr[k]=sort[k];
}

void mergesort(word* arr, int first, int last){
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
	
	word arr[n];
	for(int i=0; i<n; i++){
		scanf("%s", arr[i].name);
		arr[i].len=strlen(arr[i].name);
	}
	
	mergesort(arr, 0, n-1);
	
	printf("%s\n", arr[0].name);
	for(int i=1; i<n; i++){
		if(strcmp(arr[i-1].name, arr[i].name)!=0)
		printf("%s\n", arr[i].name);
	}
}
