#include <stdio.h>
double factorial(int n){
	if(n==0)
		return 1;
	return n*factorial(n-1);
}

int main(){
	int t;
	scanf("%d", &t);
	
	while(t--){
		int n, m;
		scanf("%d %d", &n, &m);
		
		printf("%.lf\n", factorial(m)/(factorial(n)*factorial(m-n)));
	}
}
