#include <stdio.h>
#include <stdlib.h>
int compare (const void *pa, const void *pb) {
	const double (*a)[2] = pa;
	const double (*b)[2] = pb;
    if((*a)[0]<(*b)[0])
		return -1;
    if((*a)[0]>(*b)[0])
		return 1;
	if((*a)[0]==(*b)[0]){
		if((*a)[1]<(*b)[1])
			return -1;
		if((*a)[1]>(*b)[1])
			return 1;
	}
    return 0;
}

int main(){
	int n, cnt=1;
	scanf("%d", &n);
	long long time[n][2];
	
	for(int i=0; i<n; i++){
		scanf("%lld %lld", &time[i][0], &time[i][1]);
	}
	
	qsort(time, n, sizeof time[0], compare);
	long long t=time[0][1];
	
	for(int i=1; i<n; i++){
		if(time[i][0]>=t){
			cnt++;
			t=time[i][1];
		}
	}
	
	printf("%d", cnt);
}
