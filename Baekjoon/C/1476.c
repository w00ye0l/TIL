#include <stdio.h>
int main(){
	int e, s, m;
	scanf("%d %d %d", &e, &s, &m);
	
	for(int i=1; ; i++){
		if((i-e)%15==0){
			if((i-s)%28==0){
				if((i-m)%19==0){
					printf("%d", i);
					return 0;
				}
			}
		}
	}
}
