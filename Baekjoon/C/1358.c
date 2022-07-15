#include <stdio.h>
#include <math.h>
int main(){
	int w, h, x, y, p;
	int cnt=0;
	scanf("%d %d %d %d %d", &w, &h, &x, &y, &p);
	
	while(p--){
		int xx, yy;
		scanf("%d %d", &xx, &yy);
		
		if(xx<x){
			if(pow(xx-x,2)+pow(yy-y-h/2,2)<=pow(h/2,2)){
				cnt++;
			}
		}else if(xx>x+w){
			if(pow(xx-x-w,2)+pow(yy-y-h/2,2)<=pow(h/2,2)){
				cnt++;
			}
		}else if(xx>=x && xx<=x+w){
			if(yy>=y && yy<=y+h){
				cnt++;
			}
		}
	}
	
	printf("%d", cnt);
}
