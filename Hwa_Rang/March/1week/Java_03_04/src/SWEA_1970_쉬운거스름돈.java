import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SWEA_1970_쉬운거스름돈 {
	public static void main(String[] args) throws IOException{
		int[] cash = {50000, 10000, 5000, 1000, 500, 100, 50, 10};
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine().trim());
		
		for(int tc=1; tc<=t; tc++) {
			int[] count = new int[cash.length];
			int money = Integer.parseInt(br.readLine().trim());
			
			System.out.println("#"+tc);
			for(int i=0; i<cash.length; i++) {
				if(money >= cash[i]) {
					count[i] += money/cash[i];
					money %= cash[i];
				}
				
				System.out.print(count[i]+" ");
			}
			System.out.println();
			
			
		}
	}
}
