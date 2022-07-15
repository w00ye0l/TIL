#include <stdio.h>
void pr_(int n){
    for(int i=0; i<n*4; i++){
		printf("_");
	}
}

int fac1(int n, int temp){
	pr_(temp);
	printf("\"재귀함수가 뭔가요?\"\n");
	pr_(temp);
	printf("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n");
	pr_(temp);
	printf("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n");
	pr_(temp);
	printf("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"\n");
	
	temp++;
	
	if(n==1){
		pr_(temp);
		printf("\"재귀함수가 뭔가요?\"\n");
		pr_(temp);
		printf("\"재귀함수는 자기 자신을 호출하는 함수라네\"\n");
		
		return temp;
	}
	return fac1(n-1, temp);
}

int fac2(int temp){
	pr_(temp);
	printf("라고 답변하였지.\n");
	temp--;
	
	if(temp==-1){
		return 0;
	}
	return fac2(temp);
}

int main(){
	int n;
	scanf("%d", &n);
	int temp=0;
	
	printf("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n");
	
	fac2(fac1(n, temp));
}
