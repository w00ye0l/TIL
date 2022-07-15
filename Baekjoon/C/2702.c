#include <stdio.h>
int main(){
	int t;
	scanf("%d", &t);
	
	while(t--){
		int a, b;
		int arr[1001]={0};
		int max=0, min=1;
		
		scanf("%d %d", &a, &b);
		
		for(int i=1; i<=a; i++){
			if(a%i==0)
				arr[i]++;
		}
		for(int i=1; i<=b; i++){
			if(b%i==0)
				arr[i]++;
		}
		for(int i=0; i<1001; i++){
			if(arr[i]==2)
				max=i;
		}
		min=max*(a/max)*(b/max);
		
		printf("%d %d\n", min, max);
	}
}
