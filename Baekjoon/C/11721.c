#include <stdio.h>
#include <string.h>
int main(){
	char arr[101];
	for(int i=0; i<101; i++){
		scanf("%[^\n]", &arr[i]);
	}
	
	for(int i=0; i<strlen(arr); i++){
		printf("%c", arr[i]);
		if(i%10==9)
			printf("\n");
	}
}
