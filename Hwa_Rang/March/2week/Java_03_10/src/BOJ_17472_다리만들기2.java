import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

public class BOJ_17472_다리만들기2 {
	
	static int[][] map;
	static int[][] visited;
	
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
		visited = new int[8][8];
		
		List<int[]> ladders = new ArrayList<>();
		
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
									
									int from = map[i][j];
									int to = map[y][x];
									
									if(cnt < 2) break;
									
									if(visited[from][to] != 0 && cnt < visited[from][to]){
										visited[from][to] = visited[to][from] = cnt;
										}
									
									else if(visited[from][to] == 0) {
										visited[from][to] = visited[to][from] = cnt;
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
		
		//사다리 리스트 만들기 (좌표, 개수 저장)
		
		for(int i=2; i<8; i++) {
			
			for(int j=i+1; j<8; j++) {
				
				if(visited[i][j] != 0) {
					ladders.add(new int[] {i, j, visited[i][j]});
				}
			}
		}
		
		//사다리 리스트 조합으로 최소비용구하기
		//사다리 개수는 섬개수(mapCnt)-1
		
		//사다리 개수가 최소가 안됨
		if(ladders.size() < mapCnt-1) {
			System.out.println(-1);
		}
		//바로 비용출력
		else if(ladders.size() == mapCnt-1) {
			int sum = 0;
			for(int[] ladder : ladders) {
				sum += ladder[2];
			}
			System.out.println(sum);
		}
		else {
			
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
	
	static boolean connectedBfs() {
		Queue<Integer> q = new ArrayDeque<>();
		
		Set<Integer> con = new HashSet<>();
		for(int i=2; i<mapCnt+2; i++) {
			con.add(i);
		}
		
		Set<Integer> other = new HashSet<>();
		q.add(2);
		other.add(2);
		
		while(!q.isEmpty()) {
			int i;
			for(i=q.poll(); i<mapCnt+2; i++) {
				for(int j=i+1; j<mapCnt+2; j++) {
					if(visited[i][j] != 0) {
						q.add(j);
						other.add(j);
					}
				}
			}
		}
		
		return con.equals(other);
		
	}
}
