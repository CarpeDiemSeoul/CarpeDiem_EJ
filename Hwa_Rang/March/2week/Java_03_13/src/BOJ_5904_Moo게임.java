import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_5904_Moo게임 {
	static String s;
	static StringBuilder sb;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int k = Integer.parseInt(br.readLine());
		int n = 25;
		
		String[] dp = new String[n+1];
		
		
		for(int i=1; i<=n/2; i++) {
			if(i==1) {
				dp[i] = "moo";
				continue;
			}
			
			
			sb = new StringBuilder();
			dp[i] = sb.append(dp[i-1]).append(dp[i-1]).append("o").append(dp[i-1]).toString();
			
		}

		System.out.println(dp[n/2].charAt(k-1));
	}

}
