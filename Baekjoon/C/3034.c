#include <stdio.h>
#include <math.h>
int main(){
	int n, w, h;
	scanf("%d %d %d", &n, &w, &h);
	
	while(n--){
		int t;
		scanf("%d", &t);
		
		if(t<=sqrt(pow(w,2)+pow(h,2)))
			printf("DA\n");
		else
			printf("NE\n");
	}
}
