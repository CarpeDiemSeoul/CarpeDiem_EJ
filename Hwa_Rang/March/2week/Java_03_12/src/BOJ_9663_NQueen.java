import java.util.*;
import java.io.*;

public class BOJ_9663_NQueen {
	
	//왼위, 왼아래, 오위, 오아래
	static int[] dy = {-1, 1, -1, 1}; 
	static int[] dx = {-1, -1, 1, 1}; 
	
	static boolean[][] map;
	static int cnt = 0;
	static int n;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		map = new boolean[n][n];
		
		dfs(0);
		System.out.println(cnt);
	}
	
	static void dfs(int row) {
		//종료조건
		if(row == n) {
			cnt++;
			return;
		}
		
		for(int i=0; i<n; i++) {
			//if문으로 범위체크하고 괜찮으면 dfs실행
			if(isOk(row, i)) {
				map[row][i] = true;
				dfs(row+1);
				map[row][i] = false;
			} 
		}
	}
	
	static boolean isOk(int y, int x) {	
		
		for(int i=0; i<n; i++) {
			
			if(map[i][x]) {			
				return false;
			}
			
			if(map[y][i]) return false;
			
		}
		
		for(int d=0; d<4; d++) {
			int ny = y;
			int nx = x;
			while(true) {
				ny += dy[d];
				nx += dx[d];
				
				//종료
				if(ny < 0 || ny >= n || nx < 0 || nx >= n) break;
				
				//검증
				if(map[ny][nx] == true) return false;
			}
		}
		
		
		return true;
	}
}
