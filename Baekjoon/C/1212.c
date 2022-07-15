#include <stdio.h>
#include <string.h>
#include <math.h>
void binary(int n, int i){
	int s;
	if(i==0 && n<=3){
		if(n==1)
			s=0;
		else
			s=1;
	}else{
		s=2;
	}
	
	for(int i=s; i>=0; i--){
		if(n>=pow(2, i)){
			printf("1");
			n-=(int)pow(2, i);
		}else
			printf("0");
	}
}

int main(){
	char n[333334];
	scanf("%s", &n);
	
	int len=strlen(n);
	
	if(n[0]==48)
		printf("0");
	else{
		for(int i=0; i<len; i++){
			binary(n[i]-48, i);
		}
	}
}
