import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_14502_연구소 {
	static int[][] map;
	static int[] dy = {-1, 1, 0, 0};
	static int[] dx = {0, 0, -1, 1};
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		map = new int[n][m];
		
		List<int []> list = new ArrayList<>();
		
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if(map[i][j] == 0) list.add(new int[] {i, j});
			}
		}
		
		int[][] copyMap = new int[n][m];
		
		for(int i=0; i<n; i++) {
			copyMap[i] = Arrays.copyOf(map[i], m);
		}
		
		int max = 0;
		for(int i=0; i<list.size(); i++) {
			int a = list.get(i)[0];
			int b = list.get(i)[1];
			
			for(int j=i+1; j<list.size(); j++) {
				int r = list.get(j)[0];
				int c = list.get(j)[1];
				
				for(int k=j+1; k<list.size(); k++) {
					int y = list.get(k)[0];
					int x = list.get(k)[1];
					
					map[a][b] = map[r][c] = map[y][x] = 1;
					
					for(int nr=0; nr<n; nr++) {
						for(int nc=0; nc<m; nc++) {
							if(map[nr][nc] == 2) {
								bfs(nr, nc);
							}
						}
					}

					
					int cnt = 0;
					for(int nr=0; nr<n; nr++) {
						for(int nc=0; nc<m; nc++) {
							if(map[nr][nc] == 0) {
								cnt++;
							}
						}
					}
					
					if(max < cnt) max = cnt;
					
					for(int t=0; t<n; t++) {
						map[t] = Arrays.copyOf(copyMap[t], m);
					}


				}
				
			}
		}
		
		System.out.println(max);
	}
	
	static void bfs(int y, int x) {
		Queue<Integer> q = new ArrayDeque<>();
		q.add(y);
		q.add(x);
		
		while(!q.isEmpty()) {
			int r = q.poll();
			int c = q.poll();
			
			for(int d=0; d<4; d++) {
				int nr = r+dy[d];
				int nc = c+dx[d];
				if(nr >= 0 && nr < map.length && nc >= 0 && nc < map[0].length) {
					
					if(map[nr][nc] == 0) {
						q.add(nr);
						q.add(nc);
						
						map[nr][nc] = 2;
					}
				}
			}
		}
	}
}
