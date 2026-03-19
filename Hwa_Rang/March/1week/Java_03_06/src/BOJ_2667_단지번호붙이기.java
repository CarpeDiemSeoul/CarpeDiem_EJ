import java.util.*;
import java.io.*;

public class BOJ_2667_단지번호붙이기 {
	//상하좌우
	static int[] dy = {-1, 1, 0, 0};
	static int[] dx = {0, 0, -1, 1};
	
	static char[][] map;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		map = new char[n][n];
		
		for(int i=0; i<n; i++) {
			map[i] = br.readLine().toCharArray();
		}
		int count = 0;
		
		List<Integer> list = new ArrayList<>();
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				
				if(map[i][j] == '1') {
					count++;
					list.add(bfs(i, j));
				}
			}
		}
		
		System.out.println(count);
		
		Collections.sort(list);
		for(int i: list) {
			System.out.println(i);
		}
		
	}
	
	static int bfs(int y, int x) {
		Queue<Integer> q = new ArrayDeque<>();
		
		map[y][x] = '0';
		
		//개수세기
		int cnt = 1;
		
		//좌표 넣기
		q.add(y);
		q.add(x);
		
		while(!q.isEmpty()) {
			
			//좌표 꺼내기
			int r = q.poll();
			int c = q.poll();
			
			for(int d=0; d<4; d++) {
				int nr = r + dy[d];
				int nc = c + dx[d];
				
				if(nr >= 0 && nr < map.length && nc >= 0 && nc < map.length) {
					
					if(map[nr][nc] == '1') {
						q.add(nr);
						q.add(nc);
						map[nr][nc] = '0';
						cnt++;
					}
					
				}
			}
		}
		
		
		return cnt;
	}
}
