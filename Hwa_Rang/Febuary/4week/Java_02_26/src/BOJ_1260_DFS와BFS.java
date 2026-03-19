import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_1260_DFS와BFS {
	static int[][] graph;
	static boolean[] visited;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int v = Integer.parseInt(st.nextToken());
		
		graph = new int[n+1][n+1];
		visited = new boolean[n+1];
		
		for(int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			int mid = Integer.parseInt(st.nextToken());
			int next = Integer.parseInt(st.nextToken());
			
			graph[mid][next] = graph[next][mid] = 1;
		}
		
		dfs(v);
		System.out.println();
		visited = new boolean[n+1];
		bfs(v);
	}
	
	
	static void dfs(int v) {
		visited[v] = true;
		System.out.print(v+" ");
		
		if(v == graph.length) return;
		
		for(int i=1; i<graph.length; i++) {
			if(graph[v][i] == 1 && visited[i] == false) 
				dfs(i);
		}
	}
	
	
	static void bfs(int v) {
		Queue<Integer> queue = new ArrayDeque<>();
		queue.add(v);
		visited[v] = true;
		System.out.print(v+" ");
		
		while(!queue.isEmpty()) {
			int val = queue.poll();
			
			for(int i=1; i<graph.length; i++) {
				if(graph[val][i] == 1 && visited[i] == false) {
					queue.add(i);
					visited[i] = true;
					System.out.print(i+" ");
				}
			}
		}
	}

}
