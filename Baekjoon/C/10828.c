#include <stdio.h>
#include <string.h>
int stack[10001]={0};
int t=-1;

int main(){
	int n;
	scanf("%d", &n);
	
	while(n--){
		char arr[6];
		scanf("%s", arr);
		
		if(!strcmp(arr, "push")){
			int x;
			scanf("%d", &x);
			t++;
			stack[t]=x;
		}else if(!strcmp(arr, "pop")){
			if(t<0){
				printf("-1\n");
			}else{
				printf("%d\n", stack[t]);
				t--;
			}
		}else if(!strcmp(arr, "size")){
			printf("%d\n", t+1);
		}else if(!strcmp(arr, "empty")){
			if(t==-1){
				printf("1\n");
			}else{
				printf("0\n");
			}
		}else if(!strcmp(arr, "top")){
			if(t<0){
				printf("-1\n");
			}else{
				printf("%d\n", stack[t]);
			}
		}
	}
}
