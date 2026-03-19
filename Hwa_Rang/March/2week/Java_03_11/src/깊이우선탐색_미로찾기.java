import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.StringTokenizer;

/*
탐색방향은 상우하좌 순서
벽 또는 미로를 벗어나면 진행할 수 없음
 */




public class 깊이우선탐색_미로찾기 {
	//상우하좌
	static int[] dy = {-1, 0, 1, 0};
	static int[] dx = {0, 1, 0, -1};
	
	static boolean[][] visited;
	static int[][] map;
	
	static int r, c;
	
	static List<int[]> result = new ArrayList<>();
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		
		map = new int[r][c];
		visited = new boolean[r][c];
		
		for(int i=0; i<r; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<c; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		dfs(0, 0);
	}
	
	static void dfs(int y, int x) {
		if(map[y][x] == 2) {
			System.out.println("미로탈출");
			return;
		}
		
		visited[y][x] = true;
		
		for(int d=0; d<4; d++) {
			int nr = y+dy[d];
			int nc = x+dx[d];
			
			if(nr >= 0 && nr < map.length && nc >= 0 && nc < map.length) {
				if(!visited[nr][nc] && map[nr][nc] != 1) {
					dfs(nr, nc);
				}
			}
		}

		
	}
}
