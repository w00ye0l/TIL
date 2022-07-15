#include <stdio.h>
#include <string.h>
int main(){
	int n;
	scanf("%d", &n);
	
	char arr[51][51]={0};
	
	for(int i=0; i<n; i++){
		scanf("%s", &arr[i]);
	}
	
	int len=strlen(arr[0]);
	
	if(n==1){
		printf("%s", arr[0]);
		
		return 0;
	}
	
	for(int i=0; i<len; i++){
		for(int j=0; j<n; j++){
			if(arr[j][i]!=arr[0][i]){
				arr[0][i]='?';
			}
		}
	}
	printf("%s", arr[0]);
}
