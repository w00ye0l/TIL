#include <stdio.h>
#include <math.h>
int main(){
	int i=1;
	
	while(1){
		int r, w, l;
		scanf("%d %d %d", &r, &w, &l);
		
		if(r==0){
			break;
		}
		
		if(2*r>=sqrt(pow(w,2)+pow(l,2)))
			printf("Pizza %d fits on the table.\n", i);
		else
			printf("Pizza %d does not fit on the table.\n", i);
			
		i++;
	}
}
