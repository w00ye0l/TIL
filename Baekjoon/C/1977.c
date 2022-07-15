#include <stdio.h>
#include <math.h>
int main(){
	int m, n, sum=0, j=0, min;
	scanf("%d\n %d", &m, &n);
	
	for(int i=m; i<=n; i++){
		int a=sqrt(i);
		if(i==pow(a, 2)){
			sum+=i;
			if(j==0){
				min=i;
			}
			j++;
		}
	}
	if(sum==0){
		printf("-1");
	}else{
		printf("%d\n", sum);
		printf("%d", min);
	}
}
