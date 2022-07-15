#include <stdio.h>
int main(){
	for(int i=0; i<4; i++){
		int x1, y1, p1, q1, x2, y2, p2, q2;
		scanf("%d %d %d %d %d %d %d %d", &x1, &y1, &p1, &q1, &x2, &y2, &p2, &q2);
		
		if(x1<x2 && p1>x2){
			if(y1>y2){
				if(q1<q2 && q2>y1){
					printf("a\n");
				}else if(q2==y1){
					printf("b\n");
				}else{
					printf("d\n");
				}
			}
		}else if(x1>x2){
			if(y1>y2){
				if(q1<q2 && q2>y1){
					printf("a\n");
				}else if(q2==y1){
					printf("b\n");
				}else{
					printf("d\n");
				}
			}
		}
		
		
		else if(p2>x1 && p2<q1){
			if(y2>q1 && y2>y1){
				printf("a\n");
			}else if(y2==q1){
				printf("b\n");
			}
		}else if(x1==p2 && p1==x2){
			printf("c\n");
		}else if(p1<x2){
			printf("d\n");
		}
	}
}
