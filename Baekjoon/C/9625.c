#include <stdio.h>
int a[45]={0};
int b[45]={0};

int main(){
	int n;
	scanf("%d", &n);
	
	a[1]=0;
	b[1]=1;
	a[2]=1;
	b[2]=1;
	
	for(int i=3; i<=n; i++){
		a[i]=a[i-1]+a[i-2];
		b[i]=b[i-1]+b[i-2];
	}
	
	printf("%d %d", a[n], b[n]);
}
