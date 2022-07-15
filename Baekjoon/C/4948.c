#include <stdio.h>

int main(){
	int n;
	scanf("%d", &n);
	while(n--){
		int num, max;
		scanf("%d", &num);
		int arr[10000]={0, 1};
		int check[10000]={0};
		
		for(int i=2; i<=num; i++){
			for(int j=2; i*j<=num; j++){
				arr[i*j]=1;
			}
		}
		
		for(int i=2; i<num; i++){
			if(arr[i]!=1 && arr[num-i]!=1){
				check[i]=1;
			}
		}
		for(int i=0; i<=num/2; i++){
			if(check[i]==1)
				max=i;
		}
		printf("%d %d\n", max, num-max);
	}
}
