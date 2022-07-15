#include <stdio.h>
int have[20000001];
int find[20000001];
int main(){
	int n;
	scanf("%d", &n);
	
	for(int i=0; i<n; i++){
		int x;
		scanf("%d", &x);
		
		have[x+10000000]++;
	}
	
	int m;
	scanf("%d", &m);
	
	for(int i=0; i<m; i++){
		scanf("%d", &find[i]);
	}
	
	for(int i=0; i<m; i++){
		printf("%d ", have[find[i]+10000000]);
	}
}
