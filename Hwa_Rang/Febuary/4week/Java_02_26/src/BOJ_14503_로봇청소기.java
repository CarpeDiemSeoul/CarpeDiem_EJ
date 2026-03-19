import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_14503_로봇청소기 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int[][] map = new int[n][m];
		
		//상, 하, 좌, 우
		int[] dx = {0, 0, -1, 1};
		int[] dy = {-1, 1, 0, 0};
		
		st = new StringTokenizer(br.readLine());
		int r = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		
		int d = Integer.parseInt(st.nextToken());
		
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		int cnt = 0;
		int y = r;
		int x = c;
		while(true) {
		
			if(map[y][x] == 0) {
				cnt++;
				map[y][x] = 2;
			}
			
			boolean isFind = false;
			for(int k=0; k<4; k++) {
				int ny = y+dy[k];
				int nx = x+dx[k];
				
				if(ny >= 0 && ny < n && nx >= 0 && nx < m) {
					if(map[ny][nx] == 0) isFind = true;
				}
			}
			
			if(isFind) {
				if(d == 0) {
					d = 3;
					if(map[y][x-1] == 0){
						x --;
					}
				}
				
				else if(d == 1) {
					d = 0;
					if(map[y-1][x] == 0) {
						y--;
					}
				}
				
				else if(d == 2) {
					d = 1;
					if(map[y][x+1] == 0) {
						x++;
					}
				}
				
				else {
					d = 2;
					if(map[y+1][x] == 0) {
						y++;
					}
				}
			}
			
			else {
				if(d==0) {
					if(map[y+1][x] != 1) {
						y++;
					}
					else break;
				}
				
				else if(d==1) {
					if(map[y][x-1] != 1) {
						x--;
					}
					else break;
				}
				
				else if(d==2) {
					if(map[y-1][x] != 1) {
						y--;
					}
					
					else break;
				}
				
				else {
					if(map[y][x+1] != 1) {
						x++;
					}
					else break;
				}
			}
			
			
		}
		
		System.out.println(cnt);
	}
}
