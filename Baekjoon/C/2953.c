#include <stdio.h>
int main(){
	int sum[5]={0};
	int score[5];
	int maxIndex=0, max=0;
	
	for(int i=0; i<5; i++){
		for(int j=0; j<4; j++){
			scanf("%d", &score[j]);
			sum[i]+=score[j];
			
			if(max<sum[i]){
				max=sum[i];
				maxIndex=i;
			}
		}
	}
	printf("%d %d", maxIndex+1, max);
}
