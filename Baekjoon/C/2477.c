#include <stdio.h>
int main(){
	int k;
	scanf("%d", &k);
	
	int arr[6]={0};
	int cnt, w=0, h=0, ww=0, hh=0;
	
	for(int i=0; i<6; i++){
		scanf("%d %d", &cnt, &arr[i]);
	}
	
	for(int j=0; j<6; j++){
		if(j%2==0){
			if(w<arr[j])
				w=arr[j];
		}else{
			if(h<arr[j])
				h=arr[j];
		}
	}
	
	for(int k=0; k<6; k++){
		if(k%2==0){
			if(h==arr[(k+5)%6]+arr[(k+1)%6])
				ww=arr[k];
		}else{
			if(w==arr[(k+5)%6]+arr[(k+1)%6])
				hh=arr[k];
		}
	}
	printf("%d", ((w*h)-(ww*hh))*k);
}
