#include <stdio.h>
int main(){
	int l, p;
	scanf("%d %d", &l, &p);
	
	int sum=l*p;
	int arr[6];
	for(int i=0; i<5; i++){
		scanf("%d", &arr[i]);
	}
	for(int i=0; i<5; i++){
		printf("%d ", arr[i]-sum);
	}
}
