#include <stdio.h>
#include <string.h>
int main(){
	char arr[101];
	int al[26]={0,};
	scanf("%s", &arr);
	
	int len=strlen(arr);
	int ch;
	
	for(int i=0; i<len; i++){
		ch=arr[i]-97;
		al[ch]++;
	}
	
	for(int i=0; i<26; i++){
		printf("%d ", al[i]);
	}
}
