#include <stdio.h>
#include <string.h>
#include <math.h>
int main(){
	char arr[6];
	scanf("%s", arr);
	
	int sum=0, cnt=0;
	int len=strlen(arr);
	
	for(int i=len-1; i>=0; i--){
		if(arr[i]>=48 && arr[i]<=57){
			sum+=(arr[i]-48)*pow(16, cnt);
		}else if(arr[i]>=65 && arr[i]<=70){
			sum+=(arr[i]-65+10)*pow(16, cnt);
		}
		cnt++;
	}
	printf("%d", sum);
}
