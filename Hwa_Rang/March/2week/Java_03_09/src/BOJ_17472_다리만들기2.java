import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_17472_다리만들기2 {
	
	static int[][] map;
	
	static int[] dy = {-1, 1, 0, 0};
	static int[] dx = {0, 0, -1, 1};
	
	static int mapCnt, n, m;
	
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
			}
		}
		
		mapCnt = 0;
		
		//섬 개수 세기
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				
				if(map[i][j] == 1) {
					mapCnt++;
					bfs(i, j);
				}
				
			}
		}
		
		
		//맵좌표만들기
		int[][] visited = new int[8][8];
		
		//다리개수 저장
		int h = 0;
		//맵좌표저장
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				if(map[i][j] != 0) {
					
					for(int d=0; d<4; d++) {
						int y = i;
						int x = j;
						
						int cnt = 0;
						 
						while(true) {
							y += dy[d];
							x += dx[d];
							
							if(y >=0 && y < n && x >= 0 && x < m) {
								if(map[y][x] == map[i][j]) break;								
								if(map[y][x] != 0) {
									if(cnt < 2) break;
									
									if(visited[map[y][x]][map[i][j]] != 0 && cnt < visited[map[y][x]][map[i][j]]){
										visited[map[i][j]][map[y][x]] = visited[map[y][x]][map[i][j]] = cnt;
										}
									
									else if(visited[map[y][x]][map[i][x]] == 0) {
										visited[map[i][j]][map[y][x]] = visited[map[y][x]][map[i][j]] = cnt;
										h++;	//다리 건설 성공
									}
									break;
								}
								cnt++;
							}
							
							else break;
						}	
							

					}
				}
			}
		}
		
		//좌표 저장 맵 순회 -> 1개만 저장인거는 패스 아닌것중에 다리 하나씩 없애기
		
		List<Integer> pass = new ArrayList<>();
		
		for(int i=2; i<8; i++) {
			int count = 0;
			for(int j=2; j<8; j++) {
				if(visited[i][j] != 0) count++;
			}
			//다리가 한 개인 섬 맵핑
			if(count <2) pass.add(i);
		}
		
		if(h < mapCnt-1) {
			System.out.println(-1);
		}
		
		else {
			int min = Integer.MAX_VALUE;
			
			List<int[]> xy = new ArrayList<>();
			
			for(int i=2; i<8; i++) {
				for(int j=i+1; j<8; j++) {
					System.out.print(visited[i][j]+" ");
				}
				System.out.println();
			}

			for(int i=2; i<8; i++) {
				for(int num: pass) {
					for(int j=i+1; j<8; j++) {
						if(num == i || num == j) continue;
						if(visited[i][j] != 0) xy.add(new int[]{i, j});
					}
				}
			}
			
			
			for(int[] target: xy) {
				int result = 0;
				int y = target[0];
				int x = target[1];
				
				for(int i=2; i<8; i++) {
					for(int j=i+1; j<8; j++) {
						if(i == y && j == x) continue;
						result += visited[i][j];
					}
				}
				
				if(result < min) min = result;
			}
			
			System.out.println(min);

		}
		
		
	}
	static void bfs(int y, int x) {
		Queue<Integer> q = new ArrayDeque<>();
		map[y][x] += mapCnt;
		
		q.add(y);
		q.add(x);
		
		while(!q.isEmpty()) {
			int r = q.poll();
			int c = q.poll();
			
			for(int d=0; d<4; d++) {
				int nr = r + dy[d];
				int nc = c + dx[d];
				
				if(nr >= 0 && nr < n && nc >= 0 && nc < m) {
					
					if(map[nr][nc] == 1) {
						map[nr][nc] += mapCnt;
						
						q.add(nr);
						q.add(nc);
					}
				}
			}
		}
	}
}
