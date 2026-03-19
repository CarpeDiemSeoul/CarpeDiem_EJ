import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class 깊이우선탐색DFS {
	static String input = "7 9\r\n"
			+ "1 2\r\n"
			+ "1 3\r\n"
			+ "1 6\r\n"
			+ "2 4\r\n"
			+ "2 7\r\n"
			+ "3 4\r\n"
			+ "4 7\r\n"
			+ "5 6\r\n"
			+ "5 7";
	
	static int V, E; //정점의 수, 간선의 수
	static int[][] adjArr; //인접행렬
	static boolean[] visited; //방문
	
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(input);
		
		V = sc.nextInt();
		E = sc.nextInt();
		
		adjArr = new int[V+1][V+1];
		visited = new boolean[V+1];
		
		//간선입력
		for(int i=0; i<E; i++){
			int st = sc.nextInt();	//시작정점
			int ed = sc.nextInt();	//도착정점
			adjArr[st][ed] = adjArr[ed][st] = 1; //무향그래프
			
		}
		
		dfs(1);
		
	}
	
	static void dfs(int v) {
		visited[v] = true; //방문체크
		System.out.println(v); 	//지금은 단순한 출력 -> 추후에는 동작을 하는 코드 작성
		
		for(int i=1; i<=V; i++) {
			//인접하니?
			if(adjArr[v][i] == 1 && !visited[i]) {
				dfs(i);
			}
		}
	}
}
