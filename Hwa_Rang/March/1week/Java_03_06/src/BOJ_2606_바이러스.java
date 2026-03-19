import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2606_바이러스 {
	static int cnt = 0;
	static int[][] computer;
	static boolean[] visited;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		//컴퓨터 수
		int com = Integer.parseInt(br.readLine());
		
		
		//이어져있는 쌍의 개수
		int n = Integer.parseInt(br.readLine());
		
		//컴퓨터 배열
		computer = new int[com+1][com+1];
		
		//방문여부
		visited = new boolean[com+1];
		
		
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			
			int r = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			computer[r][c] = computer[c][r] = 1;
		}
		
		dfs(1);
		
		System.out.println(cnt);
		
		
	}
	
	static void dfs(int v) {
		visited[v] = true;
		
		if(v == computer.length)return;
		
		for(int i=1; i<computer.length; i++) {
			if(computer[v][i] == 1 && !visited[i]) {
				cnt++;
				dfs(i);
			}
		}
	}
}
