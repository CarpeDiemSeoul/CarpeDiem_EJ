import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_17070_파이프옮기기1 {
	static int n;
	static int cnt;
	static int[][] map; 
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		n = Integer.parseInt(br.readLine());
		
		map = new int[n+1][n+1];
		
		for(int i=1; i<=n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=1; j<=n; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		int d=0;
		cnt = 0;
		move(2, 1, d);
		System.out.println(cnt);
		
	}
	static void move(int x, int y, int d) {
		int[] dx = {1, 1, 0};
		int[] dy = {0, 1, 1};
		
		if(x < 1 || y < 1 || x > n || y > n) {
			System.out.println(x+" "+y+" "+n);
			return ;
		}
		
		if(map[y][x] == 1) return;
		
		if(x == n && y == n) {
			cnt++;
			return;
		}
		
		//가로
		if(d==0) {
			for(int i=0; i<2; i++) {
				int nx = x+dx[i];
				int ny = y+dy[i];
				
				if(nx >= 1 && ny >= 1 && nx < n+1 && ny < n+1) {
					if(i == 1 && map[y][nx] != 1 && map[ny][x] != 1) {
						move(nx, ny, 1);
					}
					
					else if(i==0) {
						move(nx, ny, 0);
					}
				}
				
				
			}
		}
		
		//대각선
		else if(d==1) {
			for(int i=0; i<3; i++) {
				int nx = x+dx[i];
				int ny = y+dy[i];
				
				if(nx >= 1 && ny >= 1 && nx < n+1 && ny < n+1) {
					if(i == 1 && map[y][nx] != 1 && map[ny][x] != 1) {
						move(nx, ny, 1);
					}
					
					else if(i==0 || i==2) {
						move(nx, ny, i);
					}
				}

			}
		}
		
		else {
			for(int i=1; i<3; i++) {
				int nx = x+dx[i];
				int ny = y+dy[i];
				
				if(nx >= 1 && ny >= 1 && nx < n+1 && ny < n+1) {
					if(i == 1 && map[y][nx] != 1 && map[ny][x] != 1) {
						move(nx, ny, 1);
					}
					
					else if(i==2) {
						move(nx, ny, i);
					}
				}
			}

		}
	}
	
}
