#include <stdio.h>
#define MAX_NODES 1001
int DFS_V[MAX_NODES]={0};
int BFS_V[MAX_NODES]={0};
int graph[MAX_NODES][MAX_NODES]={0};
int queue[MAX_NODES];

void dfs(int v, int nodes){
	DFS_V[v]=1;
	printf("%d ", v);
	for(int w=1; w<=nodes; w++){
		if(graph[v][w]==1 && DFS_V[w]==0){ // 연결되어있냐, 방문했냐 
			dfs(w, nodes);
		}
	}
}

void bfs(int v, int nodes){
	int front=0, rear=0, pop;
	printf("%d ", v);
	BFS_V[v]=1;
	queue[0]=v;
	rear++;
	while(front<rear){
		pop=queue[front];
		front++;
		for(int w=1; w<=nodes; w++){
			if(graph[pop][w]==1 && BFS_V[w]==0){
				printf("%d ", w);
				queue[rear]=w;
				rear++;
				BFS_V[w]=1;
			}
		}
	}
}

int main(){
	int nodes, edges, node;
	scanf("%d %d %d", &nodes, &edges, &node);
	
	while(edges--){
		int i, j;
		scanf("%d %d", &i, &j);
		graph[i][j]=1;
		graph[j][i]=1;
	}
	
	dfs(node, nodes);
	printf("\n");
	bfs(node, nodes);
}
