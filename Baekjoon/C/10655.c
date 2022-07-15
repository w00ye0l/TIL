#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int x[100001];
int y[100001];
int bdis[100001];
int adis[100001];
int sub[100001];

int compare(const void *a, const void *b){
	return *(int *)b-*(int *)a;
}

int main(){
	int n;
	scanf("%d", &n);
	int len=0;
	
	for(int i=0; i<n; i++){
		scanf("%d %d", &x[i], &y[i]);
	}
	
	for(int i=0; i<n-1; i++){
		len+=abs(x[i+1]-x[i])+abs(y[i+1]-y[i]);
	}
	
	for(int i=1; i<n-1; i++){
		bdis[i-1]=abs(x[i-1]-x[i])+abs(y[i-1]-y[i])+abs(x[i+1]-x[i])+abs(y[i+1]-y[i]);
		adis[i-1]=abs(x[i-1]-x[i+1])+abs(y[i-1]-y[i+1]);
		sub[i-1]=bdis[i-1]-adis[i-1];
	}
	
	qsort(sub, sizeof(sub)/sizeof(int), sizeof(int), compare);
	
	len-=sub[0];
	
	printf("%d", len);
}
