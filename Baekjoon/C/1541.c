#include <stdio.h>
#include <string.h>
int main(){
	char arr[51];
	scanf("%s", arr);
	int tmp=0, sum=0, flag=0;
	
	for(int i=0; i<=strlen(arr); i++){
		if(arr[i]=='+' || arr[i]=='-' || i==strlen(arr)){
			if(flag==0){
				sum+=tmp;
				tmp=0;
			}else{
				sum-=tmp;
				tmp=0;
			}
			if(arr[i]=='-')
				flag=1;
		}else{
			tmp*=10;
			tmp+=arr[i]-'0';
		}
	}
	printf("%d", sum);
}
