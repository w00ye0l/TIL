#include <stdio.h>
int main(){
	int asc=0;
	int des=0;
	
	int arr[9];
	for(int i=0; i<8; i++){
		scanf("%d", &arr[i]);
	}
	
	for(int i=0; i<9; i++){
		if(i+1 == arr[i])
			asc++;
	}
	
	for(int i=8; i>0; i--){
		if(i == arr[8-i])
			des++;
	}
	
	if(asc==8)
		printf("ascending");
	else if(des==8)
		printf("descending");
	else
		printf("mixed");
}
