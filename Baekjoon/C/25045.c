#include <stdio.h>
#include <stdlib.h>
int compare1(const void *a, const void *b){
	return *(long long *)a-*(long long *)b;
}
int compare2(const void *a, const void *b){
	return *(long long *)b-*(long long *)a;
}

int main(){
	int n, m;
	scanf("%d %d", &n, &m);
	
	int min;
	long long sum=0;
	if(n>=m)
		min=m;
	else
		min=n;
	
	long long a[n];
	long long b[m];
	
	for(int i=0; i<n; i++){
		scanf("%lld", &a[i]);
	}
	for(int i=0; i<m; i++){
		scanf("%lld", &b[i]);
	}
	
	qsort(a, n, sizeof(long long), compare2);
	qsort(b, m, sizeof(long long), compare1);
	
	for(int i=0; i<min; i++){
		if(a[i]-b[i]>0){
			sum+=a[i]-b[i];
		}
	}
	
	printf("%lld", sum);
}
