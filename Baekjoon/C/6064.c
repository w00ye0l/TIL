#include <stdio.h>
int gcd(int a, int b){
	while(b!=0){
		int r=a%b;
		a=b;
		b=r;
	}
	return a;
}

int lcm(int a, int b){
	return a*b/gcd(a, b);
}

int main(){
	int t;
	scanf("%d", &t);
	
	while(t--){
		int m, n, x, y;
		scanf("%d %d %d %d", &m, &n, &x, &y);
		int end=lcm(m, n);
		int cnt=x;
		while(cnt<=end){
			if(y%n==cnt%n){
				break;
			}
			cnt+=m;
		}
		if(cnt>end){
			printf("-1\n");
		}else{
			printf("%d\n", cnt);
		}
	}
}
