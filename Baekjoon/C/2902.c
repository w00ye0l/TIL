#include <stdio.h>
#include <string.h>
int main(){
	char arr[101];
	scanf("%s", &arr);
	
	printf("%c", arr[0]);
	for(int i=0; i<strlen(arr); i++){
		if(arr[i]==45){
			printf("%c", arr[i+1]);
		}
	}
}
