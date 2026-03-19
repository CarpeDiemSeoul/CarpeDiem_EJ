import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

class Shark{
	int r, c;
	int speed;
	int direction;
	int size;
	
	public Shark(int r, int c, int speed, int direction, int size) {
		this.r = r;
		this.c = c;
		this.speed = speed;
		this.direction = direction;
		this.size = size;
	}

	@Override
	public String toString() {
		return "Shark [r=" + r + ", c=" + c + ", speed=" + speed + ", direction=" + direction + ", size=" + size + "]";
	}
	
	
	
}


public class BOJ_17143_낚시왕 {
	
	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()); 
		
		//0번째는 안씀 상하우좌
		int[] dy = {0, -1, 1, 0, 0};
		int[] dx = {0, 0, 0, 1, -1};
		int[] change = {0, 2, 1, 4, 3};
		
		//격자크기
		int R = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
		
		//상어의 개수
		int M = Integer.parseInt(st.nextToken());
		
		
		List<Shark> sharks = new ArrayList<>();
		for(int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			//상어 좌표
			int r = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			//속도
			int s = Integer.parseInt(st.nextToken());
			//방향
			int d = Integer.parseInt(st.nextToken());
			
			//사이즈
			int z = Integer.parseInt(st.nextToken());
			
			Shark shark = new Shark(r-1, c-1, s, d, z);
			
			sharks.add(shark);
		}
		
		Collections.sort(sharks, (o1, o2) -> {
			if(o1.c == o2.c) return o1.r - o2.r;
			
			return o1.c - o2.c;
		});
		
		int sumSize = 0;
		if(!sharks.isEmpty()) {
			for(int time=0; time<C; time++) {
				//상어잡기
				
				for(int i=0; i<sharks.size(); i++) {
					if(sharks.get(i).c == time) {
						sumSize += sharks.get(i).size;
						sharks.remove(i);
						break;
					}
				}
				
				//상어를 저장할 배열
				Shark[][] map = new Shark[R][C];
				
				
				//상어들 이동
				for(Shark shark: sharks) {
					
					//상어 속도만큼 방향으로 이동
					
					int nr = shark.r;
					int speed_r = shark.speed % (2 * (R-1));
					for (int i = 0; i < speed_r; i++) {
					    int nextR = nr + dy[shark.direction];
					    
					    // 다음 칸이 범위를 벗어난다면?
					    if (nextR < 0 || nextR >= R) {
					        shark.direction = change[shark.direction]; // 방향 반대로
					        nextR = nr + dy[shark.direction]; // 반대 방향으로 한 칸 이동할 위치 계산
					    }
					    nr = nextR;
					}
					
					int nc = shark.c;
					int speed_c = shark.speed % (2 * (C-1));
					for (int i = 0; i < speed_c; i++) {
					    int nextC = nc + dx[shark.direction];
					    
					    // 다음 칸이 범위를 벗어난다면?
					    if (nextC < 0 || nextC >= C) {
					        shark.direction = change[shark.direction]; // 방향 반대로
					        nextC = nc + dx[shark.direction]; // 반대 방향으로 한 칸 이동할 위치 계산
					    }
					    nc = nextC;
					}
					
					
					
					shark.r = nr;
					shark.c = nc;
					
					if(map[nr][nc] == null || map[nr][nc].size < shark.size) {
						map[nr][nc] = shark;
					}
					
					
				}
				
				sharks.clear();
				
				for(int i=0; i<R; i++) {
					for(int j=0; j<C; j++) {
						if(map[i][j] != null) {
							sharks.add(map[i][j]);
						}
					}
				}
				
				
				Collections.sort(sharks, (o1, o2) -> {
					if(o1.c == o2.c) return o1.r - o2.r;
					
					return o1.c - o2.c;
				});
				
			}
		}
		
		
		System.out.println(sumSize);
		
		
		
	}
}
