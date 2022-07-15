#include <stdio.h>
#include <stdlib.h>
int compare(const void *a, const void *b){
	return *(int *)a-*(int *)b;
}

int main(){
	int n, m, sum=0;
	scanf("%d %d", &n, &m);
	int pack[m];
	int piece[m];
	
	for(int i=0; i<m; i++){
		scanf("%d %d", &pack[i], &piece[i]);
	}
	
	qsort(pack, m, sizeof(int), compare);
	qsort(piece, m, sizeof(int), compare);
	
	if(pack[0]<=(n%6)*piece[0]){
		sum+=n/6*pack[0];
		sum+=pack[0];
	}else if(pack[0]>6*piece[0]){
		sum+=n*piece[0];
	}else{
		sum+=n/6*pack[0];
		sum+=(n%6)*piece[0];
	}
	
	printf("%d", sum);
}
