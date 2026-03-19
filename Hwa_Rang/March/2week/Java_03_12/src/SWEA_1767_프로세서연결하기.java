import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class SWEA_1767_프로세서연결하기 {
	
	static int[] dy = {-1, 1, 0, 0};
	static int[] dx = {0, 0, -1, 1};
	
	static List<int[]> coreList;
	
	static int[][] map;
	static int n;
	static int min;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int t = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=t; tc++) {
			sb.append("#").append(tc).append(" ");
			n = Integer.parseInt(br.readLine().trim());
			
			map = new int[n][n];
			coreList = new ArrayList<>();
			min = Integer.MAX_VALUE;
			
			for(int i=0; i<n; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j=0; j<n; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
					if(i != 0 && j != 0 && map[i][j] == 1) {
						coreList.add(new int[] {i, j});
					}
				}
			}
			
			combination(0, 0);
			
			System.out.println(min);
		}
	}
	
	static void combination (int idx, int depth) {
		
		//종료조건
		if(depth == coreList.size()) {
			int sum = 0;
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					if(map[i][j] == 2) sum++;
				}
			}
			if(min > sum) min = sum;
//			for(int[] arr: map) {
//				System.out.println(Arrays.toString(arr));
//			}
//			System.out.println(min);
//			System.out.println();
			return;
		}
		
		
		//조합뽑기
		for(int i=idx; i<coreList.size(); i++) {
			
			for(int d=0; d<4; d++) {
				
				int[][] tempMap = new int[n][n];
				
				for(int k=0; k<n; k++) {
					tempMap[i] = Arrays.copyOf(map[i], n);
				}
				
				int y = coreList.get(i)[0];
				int x = coreList.get(i)[1];
				
				boolean isOk = true;
				
				while(true) {
					y += dy[d];
					x += dx[d];
					
					//경계선 체크 => 무조건 한 칸이상
					if(y >= 0 && y < n && x >= 0 && x < n) {
						if(map[y][x] == 0) {
							map[y][x] = 2;
						}
						
						else {
							isOk = false;
							break;
						}
					}
					
					//경계선밖 => 연결 끝
					else {
						break;
					}
					
				}
				
				if(isOk) {
					//끝이랑 연결됨
					//재귀
					combination(i+1, depth+1);
					
				}
				
				for(int k=0; k<n; k++) {
					map[i] = Arrays.copyOf(tempMap[i], n);
				}
				
				
				for(int[] arr: map) {
					System.out.println(Arrays.toString(arr));
				}
				System.out.println();
				
			}
		}
	}
}
