import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SWEA_5650_핀볼게임 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		//방향: 상하좌우
		int[] dy = {-1, 1, 0, 0};
		int[] dx = {0, 0, -1, 1};
		
		//상하좌우 기준으로 블록을 만났을 때 방향전환 배열
		int[][] block = {
				{}, // 0번째 블록은 빈공간
				{1, 3, 0, 2}, 	//1번째 블록
				{3, 0, 1, 2},	//2번째 블록
				{2, 0, 3, 1},	//3번째 블록
				{1, 2, 3, 0}, 	//4번째 블록
				{1, 0, 3, 2} 	//5번째 블록 전부 반사
		};
		
		int t = Integer.parseInt(br.readLine().trim());
		for(int tc=1; tc<=t; tc++) {
			sb.append("#").append(tc).append(" ");
			
			int n = Integer.parseInt(br.readLine().trim());
			
			//map만들기
			int[][] map = new int[n][n];
			
			//웜홀좌표 저장
			int[][] holl = new int[11][2];
			
			//map에 값 넣어주기, 값이 5이상이면 웜홀이므로 좌표를 누적으로 저장
			for(int i=0; i<n; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j=0; j<n; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
					
					if(map[i][j] > 5) {
						
						holl[map[i][j]][0] += i; 
						holl[map[i][j]][1] += j; 
					}
				}
			}
			
			
			int max = 0;
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					// 맵의 값들 순회하는데 빈블록 아니면 점프
					if(map[i][j] != 0) continue;
									
					for(int start_d=0; start_d<4; start_d++) {
						int y = i;
						int x = j;
						int cnt = 0;
						int d = start_d;
						
						while(true) {
							y += dy[d];
							x += dx[d];
							
							//시작좌표 다시 도착 혹은 블랙홀밟음
							if((y == i && x == j) || (y>=0 && y<n && x>=0 && x<n && map[y][x] == -1)) {
								break;
							}
							
							//경계라서 벽에 닿음
							if(y>=n || y<0 || x>=n || x<0) {
								cnt++;
								//방향전환
								d = block[5][d];
								continue;
							}
							
							//숫자블록
							if(map[y][x] >= 1 && map[y][x] <= 5) {
								cnt++;
								int k = map[y][x];
								d = block[k][d];
							}
							
							//웜홀
							if(map[y][x] > 5) {
								int k = map[y][x];
								y = holl[k][0] - y;
								x = holl[k][1] - x;
							}
						}
						
						if(max < cnt) max = cnt;
					}
					
					
					
				}
			}
			sb.append(max).append("\n");
			
		}//tc
		System.out.println(sb.toString());
		
	}
}
