#include <stdio.h>
#include <string.h>
int main(){
	while(1){
		char arr[100000];
		int cnt=0;
		scanf("%s", &arr);
		
		if(arr[0]==48)
			return 0;

		int len=strlen(arr);
		
		for(int i=0; i<len/2; i++){
			if(arr[i]==arr[len-i-1]){
				cnt++;
			}
		}
		if(cnt==len/2)
			printf("yes\n");
		else
			printf("no\n");
	}
}
