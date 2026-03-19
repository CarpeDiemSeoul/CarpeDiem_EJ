import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;


public class SWEA_1868_파핑파핑지뢰찾기 {
	
	//상하좌우 왼위, 왼아래, 오위, 오아래
	static int[] dy = {-1, 1, 0, 0, -1, 1, -1, 1};
	static int[] dx = {0, 0, -1, 1, -1, -1, 1, 1};
	
	static char[][] map;
	static int n, clickCnt;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int t = Integer.parseInt(br.readLine());
		
		for(int tc=1; tc<=t; tc++) {
			sb.append("#").append(tc).append(" ");
			n = Integer.parseInt(br.readLine());
			
			map = new char[n][n];
			
			for(int i=0; i<n; i++) {
				map[i] = br.readLine().toCharArray();
			}
			
			clickCnt = 0;
			
			//연쇄폭발
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					
					if(map[i][j] == '.' && boom(i, j) != -1) {
						clickCnt++;
						bfs(i, j);
					}
				}
			}
			
			//잔반처리
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					if(map[i][j] == '.') {
						map[i][j] = '0';
						clickCnt++;
					}
				}
			}
			
			sb.append(clickCnt).append("\n");
			
			
		}
		System.out.println(sb.toString());
	}
	static int boom(int y, int x) {

		int cnt = 8;
		int check = 0;
		
		for(int d=0; d<8; d++) {
			int nr = y + dy[d];
			int nc = x + dx[d];
			
			if(nr < 0 || nr >= n || nc < 0 || nc >= n || map[nr][nc] == '0') {
				cnt--;
				continue;
			};
			
			if(map[nr][nc] == '.') {
				check++;
			}
		}
		if(cnt == check) return check;
		
		return -1;
	} 
	
	static void bfs(int y, int x) {

		Queue<Integer> q = new ArrayDeque<>();
		//좌표저장
		q.add(y);
		q.add(x);
		map[y][x] = '0';
		
		while(!q.isEmpty()) {
			
			int r = q.poll();
			int c = q.poll();
			
			for(int d=0; d<8; d++) {
				int nr = r + dy[d];
				int nc = c + dx[d];
				
				if(nr < 0 || nr >= n || nc < 0 || nc >= n) {
					continue;
				};
				
				if(map[nr][nc] == '.') {
					map[nr][nc] = '0';
					
					// 모든 범위가'0'이어도 안됨 최소 1개이상
					if(boom(nr, nc) >= 1) {
						q.add(nr);
						q.add(nc);					
					}
				}
				
			}
 		}
	}
}

