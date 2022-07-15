#include <stdio.h>
#include <math.h>
int main(){
	int d, h, w;
	scanf("%d %d %d", &d, &h, &w);
	
	double dd=pow(d,2);
	double hh=sqrt(dd/(pow(h,2)+pow(w,2)))*h;
	double ww=hh*w/h;
	
	printf("%.0f %.0f", floor(hh), floor(ww));
}
