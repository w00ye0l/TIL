#include <stdio.h>
#include <math.h>
double time[100001][2]={0};

int compare (const void *pa, const void *pb) {
	const double (*a)[2] = pa;
	const double (*b)[2] = pb;
    if((*a)[1]<(*b)[1])
		return -1;
    if((*a)[1]>(*b)[1])
		return 1;
	if((*a)[1]==(*b)[1]){
		if((*a)[0]<(*b)[0])
			return -1;
		if((*a)[0]>(*b)[0])
			return 1;
	}
    return 0;
}

int main(){
	int n;
	scanf("%d", &n);
	
	for(int i=0; i<n; i++){
		int x, y, v;
		scanf("%d %d %d", &x, &y, &v);
		double dis=sqrt(pow(x,2)+pow(y,2));
		double ver=v;
		time[i][0]=i+1;
		time[i][1]=dis/ver;
	}
	
	qsort(time, n, sizeof time[0], compare);
	
	for(int i=0; i<n; i++){
		printf("%d\n", (int)time[i][0]);
	}
}
