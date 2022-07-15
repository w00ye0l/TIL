#include <stdio.h>
char stack[51];
int top=-1;

void push(char c){
	stack[top++]=c;
}
char pop(){
	return stack[--top];
}
int empty(){
	return top==-1;
}
int check(char *str){
	int result=1;
	for(int i=0; str[i]; i++){
		if(str[i]=='('){
			push(str[i]);
		}else{
			if(empty()){
				result=0;
				break;
			}else{
				pop();
			}
		}
	}
	if(!empty()){
		result=0;
	}
	while(!empty()){
		pop();
	}
	return result;
}

int main(){
	int t;
	scanf("%d", &t);
	
	while(t--){
		char arr[51];
		scanf("%s", arr);
		
		if(check(arr)){
			printf("YES\n");
		}else{
			printf("NO\n");
		}
	}
}
