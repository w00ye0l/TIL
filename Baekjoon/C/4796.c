#include <stdio.h>
int main(){
	int l, p, v;
	int i=1;
	while(1){
		int result=0;
		scanf("%d %d %d", &l, &p, &v);
		if(l==0 && p==0 && v==0){
			break;
		}
		
		result+=v/p*l;
		if(v%p<l){
			result+=v%p;
		}else{
			result+=l;
		}
		
		printf("Case %d: %d\n", i, result);
		
		i++;
	}
}
