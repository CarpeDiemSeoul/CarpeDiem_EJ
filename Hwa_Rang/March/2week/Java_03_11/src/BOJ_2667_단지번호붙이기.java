import java.util.*;
import java.io.*;


public class BOJ_2667_단지번호붙이기 {
	
	//상, 하, 좌, 우
	static int[] dy = {-1, 1, 0, 0};
	static int[] dx = {0, 0, -1, 1};
	
	static char[][] map;
	
	static int n;
	static int cnt;
	static int mapCnt;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		n = Integer.parseInt(br.readLine());
		map = new char[n][n];
		
		for(int i=0; i<n; i++) {
			map[i] = br.readLine().toCharArray();
		}
		
		List<Integer> list = new ArrayList<>();
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				if(map[i][j] == '1') {
					mapCnt++;
					cnt = 0;
					dfs(i, j);
					list.add(cnt);
				}
			}
		}
		
		Collections.sort(list);
		System.out.println(mapCnt);
		for(int i : list) {
			System.out.println(i);
		}
		
	}
	
	static void dfs(int y, int x) {
		
		//종료조건
		if(map[y][x] == '0') return;
		
		else if(map[y][x] == '1') {
			
			map[y][x] = 'm';
			cnt++;
			
			for(int d=0; d<4; d++) {
				int ny = y+dy[d];
				int nx = x+dx[d];
				
				if(ny >= 0 && ny < n && nx >= 0 && nx < n) {
					dfs(ny, nx);
				}
			}
		}
	}
}
