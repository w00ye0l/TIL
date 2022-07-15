#include <stdio.h>
int N[20000001];
int M[20000001];

int main(){
	int n, m;
	scanf("%d", &n);
	for(int i=0; i<n; i++){
		int x;
		scanf("%d", &x);
		N[x]=1;
	}
	
	scanf("%d", &m);
	for(int i=0; i<m; i++){
		scanf("%d", &M[i]);
	}
	
	for(int i=0; i<m; i++){
		printf("%d ", N[M[i]]);
	}
}
