#include <stdio.h>
#define SIZE 500001
int arr[SIZE];
int front=0, back=-1;

int main(){
	int n;
	scanf("%d", &n);
	
	for(int i=1; i<=n; i++){
		back++;
		arr[back]=i;
	}
	
	while(1){
		front=(front+1)%n;
		if(back==front)
			break;
		
		back=(back+1)%n;
		arr[back]=arr[front];
		front=(front+1)%n;
		
		if(back==front)
			break;
	}
	
	printf("%d", arr[front]);
}
