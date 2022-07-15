#include <stdio.h>
int gcd(int a, int b){
	if(b==0)
		return a;
	return gcd(b, a%b);
}

int main(){
	int n;
	scanf("%d", &n);
	int arr[n];
	for(int i=0; i<n; i++){
		scanf("%d", &arr[i]);
	}
	int arr2[n][2];
	for(int i=1; i<n; i++){
		arr2[i][1]=arr[0]/gcd(arr[0], arr[i]);
		arr2[i][0]=arr[i]/gcd(arr[0], arr[i]);
	}
	
	for(int i=1; i<n; i++){
		printf("%d/%d\n", arr2[i][1], arr2[i][0]);
	}
}
