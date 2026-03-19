import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class SWEA_1767_프로세서연결하기 {
	
	static int[] dy = {-1, 1, 0, 0};
	static int[] dx = {0, 0, -1, 1};
	
	static List<int[]> coreList;
	
	static int[][] map;
	static int n;
	static int min;
	static int maxCore;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int t = Integer.parseInt(br.readLine().trim());
		for(int tc=1; tc<=t; tc++) {
			sb.append("#").append(tc).append(" ");
			n = Integer.parseInt(br.readLine().trim());
			
			map = new int[n][n];
			coreList = new ArrayList<>();
			min = Integer.MAX_VALUE;
			maxCore = 0;
			
			for(int i=0; i<n; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j=0; j<n; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
					if(i != 0 && j != 0 && i != n-1 && j != n-1 && map[i][j] == 1) {
						coreList.add(new int[] {i, j});
					}
				}
			}
			
			combination(0, 0, 0, 0);
			if(min == Integer.MAX_VALUE) {
				sb.append(0).append("\n");
			}
			else
				sb.append(min).append("\n");
		}
		System.out.println(sb.toString());
	}
	
	static void combination (int idx, int depth, int sum, int coreCnt) {
		
		//종료조건
		if(depth == coreList.size()) {
			if(coreCnt > maxCore) {
				maxCore = coreCnt;
				min = sum;
			}
			else if(coreCnt == maxCore) {
				if(min > sum) min = sum;
				
			}
			
			return;
		}
		
		//조합뽑기

		for(int d=0; d<4; d++) {
			
			boolean isOk = true;
			int y = coreList.get(idx)[0];
			int x = coreList.get(idx)[1];
			
			while(true) {
				y += dy[d];
				x += dx[d];
				
				//경계선 체크 => 무조건 한 칸이상
				if(y >= 0 && y < n && x >= 0 && x < n) {
					if(map[y][x] == 0) {
						map[y][x] = 2;
						sum++;
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
				combination(idx+1, depth+1, sum, coreCnt+1);
			}
			
			//원상복구
			while(true) {
				y -= dy[d];
				x -= dx[d];
				
				//경계선 체크 => 무조건 한 칸이상 원상복구
				if(y >= 0 && y < n && x >= 0 && x < n) {
					if(map[y][x] == 2) {
						map[y][x] = 0;
						sum--;
					}
					
					else {
						break;
					}
				}
				
				//경계선밖 => 연결 끝
				else {
					break;
				}
				
			}
			
			
		}
		
		//코어포기
		combination(idx+1, depth+1, sum, coreCnt);

	}
	
	
}
