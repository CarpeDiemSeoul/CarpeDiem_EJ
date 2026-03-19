import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SWEA_1952_수영장	{
	static int day, m1, m3, year;
	static int[] month;
	static int ans;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int t = Integer.parseInt(br.readLine());
		
		for(int tc=1; tc<=t; tc++) {
			
			st = new StringTokenizer(br.readLine());
			
			day = Integer.parseInt(st.nextToken());	//일일
			m1 = Integer.parseInt(st.nextToken());	//한달
			m3 = Integer.parseInt(st.nextToken());	//3달
			year = Integer.parseInt(st.nextToken());	//1년
			
			month = new int[13];
			
			st = new StringTokenizer(br.readLine());
			
			for(int i=1; i<13; i++) {
				month[i] = Integer.parseInt(st.nextToken());	
			}
			
//			ans = Integer.MAX_VALUE; //최소비용 구해라 -> 아주 큰 수로 초기화
			ans = year;
			
			swimFee(1, 0);
			System.out.println("#"+tc+" "+ans);
		}
		
	}
	
	//m: 이용권을 고르기 위한 달
	//fee: 지금까지 누적해온 요금
	
	//고민을 해보자
	//ans는 내가 베스트라고 알고 있는 값
	
	static void swimFee(int m, int fee) {
		//종료파트
		if(m>12) {
			//현재 가지고 있는 정답과 이번에 만들어진 fee를 가지고 생신
			//두개의 값을 가지고 갱신을 한다.
			ans = Math.min(ans, fee);
//			ans = ans > fee ? fee : ans;
			return;
		}
		
		//재귀파트
		
		//1일권
		swimFee(m+1, fee + day * month[m]);
		
		//한달권
		swimFee(m+1, fee+m1);
		
		//세달권
		swimFee(m+3, fee+m3);
	}
}
