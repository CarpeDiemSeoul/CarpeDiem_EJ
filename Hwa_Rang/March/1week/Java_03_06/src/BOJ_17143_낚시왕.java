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
	
	
}


public class BOJ_17143_낚시왕 {
	
	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()); 
		
		//0번째는 안씀 상하좌우
		int[] dy = {0, -1, 1, 0, 0};
		int[] dx = {0, 0, 0, -1, 1};
		
		//격자크기
		int R = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
		
		//상어의 개수
		int M = Integer.parseInt(st.nextToken());
		
		Shark[][] map = new Shark[R][C];
		
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
			
			Shark shark = new Shark(r, c, s, d, z);
			
			sharks.add(shark);
		}
		
		Collections.sort(sharks, (o1, o2) -> {
			if(o1.r == o2.r) return o1.c - o2.c;
			
			return o1.r - o2.r;
		});
		
		int sumSize = 0;
		for(int time=0; time<C; time++) {
			//상어잡기
			sumSize = sharks.get(0).size;
			sharks.remove(0);
			
			
			//상어들 이동
			for(Shark shark: sharks) {
				
				//상어 속도만큼 방향으로 이동
				int nr = shark.r + dy[shark.direction]*shark.speed;
				int nc = shark.c + dx[shark.direction]*shark.speed;
				
				//경계초과
				if(nr < 0 || nr >= R || nc < 0 || nc >= C) {

				} 
			}
			
		}
		
		
		
		
		
	}
}
