#include <stdio.h>
int arr[100001]={0};

int main(){
	int n, m, num;
	scanf("%d %d", &n, &m);
	
	for(int a = 1; a <= n; a++){
		scanf("%d", &num);
		arr[a] = arr[a - 1] + num;
	}
	
	while(m--){
		int i, j;
		scanf("%d %d", &i, &j);
		
		
		printf("%d\n", arr[j] - arr[i-1]);
	}
}
