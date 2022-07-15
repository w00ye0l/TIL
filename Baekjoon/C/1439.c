#include <stdio.h>
#include <string.h>
#include <math.h>
int main(){
	char arr[1000000];
	int zero=0, one=0;
	scanf("%s", &arr);
	
	for(int i=0; i<strlen(arr); i++){
		if(arr[i]=='0'){
			if(arr[i+1]!='0'){
				zero++;
			}
		}else{
			if(arr[i+1]!='1'){
				one++;
			}
		}
	}
	
	if(zero<one){
		printf("%d", zero);
	}else{
		printf("%d", one);
	}
}
