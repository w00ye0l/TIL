#include <stdio.h>
void pr_(int n){
    for(int i=0; i<n*4; i++){
		printf("_");
	}
}

int fac1(int n, int temp){
	pr_(temp);
	printf("\"����Լ��� ������?\"\n");
	pr_(temp);
	printf("\"�� ����. �������� �� �� ����⿡ �̼��� ��� ������ ����� ������ �־���.\n");
	pr_(temp);
	printf("���� ������� ��� �� ���ο��� ������ ������ �߰�, ��� �����Ӱ� ����� �־���.\n");
	pr_(temp);
	printf("���� ���� ��κ� �ǾҴٰ� �ϳ�. �׷��� ��� ��, �� ���ο��� �� ���� ã�ƿͼ� ������.\"\n");
	
	temp++;
	
	if(n==1){
		pr_(temp);
		printf("\"����Լ��� ������?\"\n");
		pr_(temp);
		printf("\"����Լ��� �ڱ� �ڽ��� ȣ���ϴ� �Լ����\"\n");
		
		return temp;
	}
	return fac1(n-1, temp);
}

int fac2(int temp){
	pr_(temp);
	printf("��� �亯�Ͽ���.\n");
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
	
	printf("��� �� ��ǻ�Ͱ��а� �л��� ������ �������� ã�ư� ������.\n");
	
	fac2(fac1(n, temp));
}
