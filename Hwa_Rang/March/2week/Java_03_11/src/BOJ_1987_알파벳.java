import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1987_알파벳 {
	
	static int[] dy = {-1, 1, 0, 0};
	static int[] dx = {0, 0, -1, 1};
	
	static char[][] map;
	
	static boolean[] check;
	static boolean[][] visited;
	
	static int r, c;
	static int max = 0;
	static int cnt = 0;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		
		map = new char[r][c];
		visited = new boolean[r][c];
		
		for(int i=0; i<r; i++) {
			map[i] = br.readLine().toCharArray();
		}
		
		
		//'Z'-'A'+1
		check = new boolean[90-65+1];
		
		dfs(0, 0);
		if(max == 0) {
			System.out.println(1);
		}
		else {
			System.out.println(max);			
		}
		
		
	}
	
	static void dfs(int y, int x) {
		//종료조건
		if(check[(int)(map[y][x]-'A')]) {
			if(max < cnt) max = cnt;
			return;
		} 
		
		check[(int)(map[y][x]-'A')] = true;
		visited[y][x] = true;
		
		//재귀
		for(int d=0; d<4; d++) {
			int ny = y+dy[d];
			int nx = x+dx[d];
			
			if(ny >= 0 && ny < r && nx >= 0 && nx < c) {
				if(!visited[ny][nx]) {
					cnt++;
					dfs(ny, nx);
					cnt--;
					visited[ny][nx] = false;
				}

			}
		}
		
		check[(int)(map[y][x]-'A')] = false;
	}
}
