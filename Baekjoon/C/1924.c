#include <stdio.h>
int main(){
	int month, day, sum=0;
	scanf("%d %d", &month, &day);
	
	int arr[12]={0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30};
	char *dayName[]={"MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"};
	
	sum+=day-1;
	for(int i=0; i<month; i++){
		sum+=arr[i];
	}
	
	for(int i=0; i<3; i++){
		printf("%c", *(dayName[sum%7]+i));
	}
}
