#include <stdio.h>
#include <string.h>
int stack[10001]={0};
int f=0;
int b=-1;

int main(){
	int n;
	scanf("%d", &n);
	
	while(n--){
		char arr[6];
		scanf("%s", arr);
		
		if(!strcmp(arr, "push")){
			int x;
			scanf("%d", &x);
			b++;
			stack[b]=x;
		}else if(!strcmp(arr, "pop")){
			if(f>b){
				printf("-1\n");
			}else{
				printf("%d\n", stack[f]);
				f++;
			}
		}else if(!strcmp(arr, "size")){
			printf("%d\n", b-f+1);
		}else if(!strcmp(arr, "empty")){
			if(f>b){
				printf("1\n");
			}else{
				printf("0\n");
			}
		}else if(!strcmp(arr, "front")){
			if(f>b){
				printf("-1\n");
			}else{
				printf("%d\n", stack[f]);
			}
		}else if(!strcmp(arr, "back")){
			if(f>b){
				printf("-1\n");
			}else{
				printf("%d\n", stack[b]);
			}
		}
	}
}
