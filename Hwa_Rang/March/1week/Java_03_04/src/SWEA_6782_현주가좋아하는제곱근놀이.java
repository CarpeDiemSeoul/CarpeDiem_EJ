import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SWEA_6782_현주가좋아하는제곱근놀이 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int t = Integer.parseInt(br.readLine().trim());
		
		
		
		for(int tc=1; tc<=t; tc++) {
			long n = Long.parseLong(br.readLine().trim());
			
			int cnt = 0;
			while(true) {
				if(n == 2)break;
				
				double tmp = Math.sqrt(n);
				
				if(tmp - (long)tmp == 0) {
					n = (long)tmp;
					cnt++;
				}
				else {
					cnt += (int)(((long)tmp + 1) * ((long)tmp + 1) - n + 1);
					n = (long)tmp + 1;
					
				}
			}
			
			System.out.println("#"+tc+" "+cnt);
		}
		
	}
}
