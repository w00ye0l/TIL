#include <stdio.h>
int main(){
	int n, yes=0, no=0;
	scanf("%d", &n);
	
	int arr[n];
	for(int i=0; i<n; i++){
		scanf("%d", &arr[i]);
		if(arr[i]==1)
			yes++;
		else
			no++;
	}
	
	if(yes>no)
		printf("Junhee is cute!");
	else
		printf("Junhee is not cute!");
}
