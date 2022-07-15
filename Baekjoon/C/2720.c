#include <stdio.h>
int main(){
	int t;
	int arr[5]={25,10,5,1};
	int re[5]={0};
	scanf("%d", &t);
	
	while(t--){
		int c;
		scanf("%d", &c);
		for(int i=0; i<4; i++){
			re[i]=c/arr[i];
			c%=arr[i];
		}
		for(int i=0; i<4; i++){
			printf("%d ", re[i]);
		}
		printf("\n");
	}
}
