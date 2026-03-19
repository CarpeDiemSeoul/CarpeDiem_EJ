import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_14502_연구소 {
	
	static int[] dy = {-1, 1, 0, 0};
	static int[] dx = {0, 0, -1, 1};
	
	static List<int[]> zeroList = new ArrayList<>();
	static List<int[]> startList = new ArrayList<>(); 
	
	static int[][] map;
	static int n, m;
	static int max = 0;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		map = new int[n][m];
		
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				
				if(map[i][j] == 0) zeroList.add(new int[] {i, j});
				if(map[i][j] == 2) startList.add(new int[] {i, j});
			}
		}
		

		combination(0, 0);
		
		System.out.println(max);
		
	}
	
	static void dfs(int y, int x) {
				
		for(int d=0; d<4; d++) {
			int ny = y+dy[d];
			int nx = x+dx[d];
			
			if(ny >= 0 && ny < n && nx >= 0 && nx < m) {
				if(map[ny][nx] == 0) {
					map[ny][nx] = 3;
					dfs(ny, nx);
				} 
			}
		}
	}
	
	static void combination(int idx, int depth) {
		if(depth == 3) {
			
			int[][] tempMap = new int[n][m];
			
			for(int i=0; i<n; i++) {
				tempMap[i] = Arrays.copyOf(map[i], m);
			}
			
			for(int[] arr: startList) {
				int y = arr[0];
				int x = arr[1];
				dfs(y, x);
			}
			
			int cnt = 0;
			
			//0세기
			for(int i=0; i<n; i++) {
				for(int j=0; j<m; j++) {
					if(map[i][j] == 0) cnt++;
				}
			}
			
			if(max < cnt) max = cnt;
			
			for(int i=0; i<n; i++) {
				map[i] = Arrays.copyOf(tempMap[i], m);
			}
			
			return;
		}
		
		for(int i=idx; i<zeroList.size(); i++) {
			int r = zeroList.get(i)[0];
			int c = zeroList.get(i)[1];
			map[r][c] = 1;
			combination(i+1, depth+1);
			map[r][c] = 0;
		}
	}
}
