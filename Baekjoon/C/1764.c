#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char N[1000000][21];
char C[500000][21];

int compare(const void *a, const void *b){
	return strcmp((char *)a, (char *)b);
}

int main(){
	int n, m, cnt=0;
	scanf("%d %d", &n, &m);
	
	for(int i=0; i<n+m; i++){
		scanf("%s", &N[i]);
	}
	
	qsort((void *)N, n+m, sizeof(N[0]), compare);
	
	for(int i=0; i<n+m; i++){
		if(strcmp(N[i], N[i+1])==0){
			strcpy(C[cnt], N[i]);
			i++;
			cnt++;
		}
	}
	
	printf("%d\n", cnt);
	for(int i=0; i<cnt; i++){
		printf("%s\n", C[i]);
	}
}
