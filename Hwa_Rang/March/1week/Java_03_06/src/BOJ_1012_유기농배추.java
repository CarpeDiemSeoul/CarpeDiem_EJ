import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_1012_유기농배추 {
	static int[] dy = {-1, 1, 0, 0};
	static int[] dx = {0, 0, -1, 1};
	
	static int[][] map;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int t = Integer.parseInt(br.readLine());
		
		for(int tc=0; tc<t; tc++) {
			st = new StringTokenizer(br.readLine());
			
			//가로
			int m = Integer.parseInt(st.nextToken());
			//세로
			int n = Integer.parseInt(st.nextToken());
			//배추의 위치 개수
			int k = Integer.parseInt(st.nextToken());
			
			map = new int[n][m];
			
			//배추심기
			for(int i=0; i<k; i++) {
				st = new StringTokenizer(br.readLine());
				
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				
				map[y][x] = 1;
			}
			
//			for(int[] arr: map)
//				System.out.println(Arrays.toString(arr));
			
			//벌레의 개수
			int cnt = 0;
			
			//순회
			for(int i=0; i<n; i++) {
				for(int j=0; j<m; j++) {
					
					if(map[i][j] == 1) {
						cnt++;
						bfs(i, j);
					}
				}
			}
			
			System.out.println(cnt);
			
		}
	}
	
	static void bfs(int y, int x) {
		Queue<Integer> q = new ArrayDeque<>();
		
		q.add(y);
		q.add(x);
		
		map[y][x] = 0;
		
		while(!q.isEmpty()) {
			
			int r = q.poll();
			int c = q.poll();
			
			for(int d=0; d<4; d++) {
				int nr = r + dy[d];
				int nc = c + dx[d];
				
				if(nr >= 0 && nr < map.length && nc >= 0 && nc < map[0].length) {
					
					if(map[nr][nc] == 1) {
						q.add(nr);
						q.add(nc);
						
						map[nr][nc] = 0;
					}
					
				}
			}
			
			
			
		}
	}//bfs
	
}
