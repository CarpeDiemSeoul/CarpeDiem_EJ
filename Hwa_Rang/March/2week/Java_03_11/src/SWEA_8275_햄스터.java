import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SWEA_8275_햄스터 {
	// 햄스터의 수가 최대 -> 여러개일 경우 사전순
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int t = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=t; tc++) {
			//미리 작성
			sb.append("#").append(tc).append(" ");
			
			st = new StringTokenizer(br.readLine());
			
			//우리 번호(1번부터 n번까지)
			int n = Integer.parseInt(st.nextToken());
			
			//우리마다 햄스터 개수(0 ~ x까지)
			int x = Integer.parseInt(st.nextToken());
			
			//경근이의 기록 -> 반복문 횟수 
			int m = Integer.parseInt(st.nextToken());
			
			//0번우리 버림
			int[] cage = new int[n+1];
			
			for(int i=0; i<m; i++) {
				st = new StringTokenizer(br.readLine());
				
				//l => 시작우리
				int l = Integer.parseInt(st.nextToken());
				
				//마지막 우리
				int r = Integer.parseInt(st.nextToken());
				
				//시작부터 마지막까지의 햄스터의 수
				int s = Integer.parseInt(st.nextToken());
			}
		}
		

	}
}
