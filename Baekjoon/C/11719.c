#include <stdio.h>
int main(){
	char arr[101];
	
	while(fgets(arr, 101, stdin)){
		printf("%s", arr);
	}
}
