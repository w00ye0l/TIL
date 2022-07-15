#include <stdio.h>
#include <math.h>
int main(){
	int t;
	scanf("%d", &t);
	
	while(t--){
		int x1, y1, x2, y2, cnt=0;
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		int arr[51][4];
		int n;
		scanf("%d", &n);
		for(int i=0; i<n; i++){
			scanf("%d %d %d", &arr[i][0], &arr[i][1], &arr[i][2]);
		}
		
		for(int i=0; i<n; i++){
			if(sqrt(pow(x1-arr[i][0], 2)+pow(y1-arr[i][1], 2))<arr[i][2]){
				if(sqrt(pow(x2-arr[i][0], 2)+pow(y2-arr[i][1], 2))>arr[i][2]){
					cnt++;
				}
			}
			if(sqrt(pow(x1-arr[i][0], 2)+pow(y1-arr[i][1], 2))>arr[i][2]){
				if(sqrt(pow(x2-arr[i][0], 2)+pow(y2-arr[i][1], 2))<arr[i][2]){
					cnt++;
				}
			}
			
		}
		printf("%d\n", cnt);
	}
}
