#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char arr[100001];

int compare(const void* a, const void* b){
	char f=*(char *)a;
	char s=*(char *)b;
	
	if(f>s)
		return -1;
	else if(f<s)
		return 1;
	else
		return 0;
}

int main(){
	int sum=0, i=0;
	scanf("%s", arr);
	
	if(strchr(arr, '0')==NULL || arr[0]=='0'){
		printf("-1");
		return 0;
	}
	
	while(arr[i]!=NULL){
		sum+=arr[i]-48;
		i++;
	}
	if(sum%3!=0 || sum==0){
		printf("-1");
	}else{
		qsort(arr, sizeof(arr)/sizeof(char), sizeof(char), compare);
		printf("%s", arr);
	}
}
