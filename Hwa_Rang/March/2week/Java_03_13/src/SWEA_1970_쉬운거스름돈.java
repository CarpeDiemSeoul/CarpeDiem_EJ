import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SWEA_1970_쉬운거스름돈 {
	static int[] arr = {50000, 10000, 5000, 1000, 500, 100, 50, 10};
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int t = Integer.parseInt(br.readLine().trim());
		
		for(int tc=1; tc<=t; tc++) {
			sb.append("#").append(tc).append("\n");
			int money = Integer.parseInt(br.readLine());
			
			int[] count = new int[arr.length];
			
			for(int i=0; i<arr.length; i++) {
				if(money >= arr[i]) {
					count[i] = money/arr[i];
					money %= arr[i];
				}
			}
			
			for(int coin: count) {
				sb.append(coin).append(" ");
			}
			
			sb.append("\n");
			
		}
		
		System.out.println(sb.toString());
	}
}
