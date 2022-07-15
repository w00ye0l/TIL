#include <stdio.h>
#include <string.h>
#include <stdlib.h>
char s[1001];
char s1[1001][1001];
char temp[1001];

int main(){
	scanf("%s", s);
	int len=strlen(s);
	
	for(int i=0; i<len; i++){
		for(int j=i; j<len; j++){
			s1[i][j-i]=s[j];
		}
	}
	
	for(int i=0; i<len-1; i++){
		for(int j=0; j<len-1-i; j++){
			if(strcmp(s1[j], s1[j+1])>0){
				strcpy(temp, s1[j]);
				strcpy(s1[j], s1[j+1]);
				strcpy(s1[j+1], temp);
			}
		}
	}
	
	for(int i=0; i<len; i++){
		printf("%s\n", s1[i]);
	}
}
