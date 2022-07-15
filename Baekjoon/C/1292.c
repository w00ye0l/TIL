#include <stdio.h>
int main(){
	int x, y;
	scanf("%d %d", &x, &y);
	
	int arr[1001]={0, };
	int cnt=0;
	
	for(int i=0; i<1001; i++){
		for(int j=0; j<i; j++){
			if(cnt==1001){
				break;
			}
			arr[cnt]=i;
			cnt++;
		}
	}
	
	for(int i=0; i<1001; i++){
		printf("%d ", arr[i]);
	}
	
	int sum=0;
	
	for(int i=x-1; i<y; i++){
		sum+=arr[i];
	}
	printf("%d", sum);
}
