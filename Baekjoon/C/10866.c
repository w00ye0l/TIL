#include <stdio.h>
#include <string.h>
int arr[10000]={0};
int front=5000;
int back=4999;
char str[10];

int main(){
	int n;
	scanf("%d", &n);
	
	while(n--){
		scanf("%s", &str);
		
		if(strcmp(str,"push_front")==0){
			int x;
			scanf("%d", &x);
			arr[(--front+10000)%10000]=x;
		}else if(strcmp(str,"push_back")==0){
			int x;
			scanf("%d", &x);
			arr[(++back+10000)%10000]=x;
		}else if(strcmp(str,"pop_front")==0){
			if(back-front+1!=0){
				printf("%d\n", arr[front]);
				arr[front]=0;
				front++;
			}else{
				printf("-1\n");
			}
		}else if(strcmp(str,"pop_back")==0){
			if(back-front+1!=0){
				printf("%d\n", arr[back]);
				arr[back]=0;
				back--;
			}else{
				printf("-1\n");
			}
		}else if(strcmp(str,"size")==0){
			printf("%d\n", back-front+1);
		}else if(strcmp(str,"empty")==0){
			if(back-front+1==0){
				printf("1\n");
			}else{
				printf("0\n");
			}
		}else if(strcmp(str,"front")==0){
			if(back-front+1!=0){
				printf("%d\n", arr[front]);
			}else{
				printf("-1\n");
			}
		}else if(strcmp(str,"back")==0){
			if(back-front+1!=0){
				printf("%d\n", arr[back]);
			}else{
				printf("-1\n");
			}
		}
	}
}
