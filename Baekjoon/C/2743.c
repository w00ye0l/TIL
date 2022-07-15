#include <stdio.h>
#include <string.h>
int main(){
	char arr[101];
	scanf("%[^\n]", &arr);
	
	printf("%d", strlen(arr));
}
