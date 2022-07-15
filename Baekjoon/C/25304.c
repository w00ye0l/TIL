#include <stdio.h>
int main(){
	int x;
	scanf("%d", &x);
	
	int n;
	scanf("%d", &n);
	
	int result=0;
	
	for(int i=0; i<n; i++){
		int a, b;
		scanf("%d %d", &a, &b);
		result+=a*b;
	}
	
	if(result==x){
		printf("Yes");
	}else{
		printf("No");
	}
}
