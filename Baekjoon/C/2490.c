#include <stdio.h>
int main(){
	for(int i=0; i<3; i++){
		int arr[4];
		int cnt=0;
		for(int i=0; i<4; i++){
			scanf("%d", &arr[i]);
		}
		for(int i=0; i<4; i++){
			if(arr[i]==0){
				cnt++;
			}
		}
		if(cnt==0){
			printf("E\n");
		}else{
			printf("%c\n", cnt+64);
		}
	}
}
