import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SWEA_1952_수영장	{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int t = Integer.parseInt(br.readLine());
		
		for(int tc=1; tc<=t; tc++) {
			
			st = new StringTokenizer(br.readLine());
			
			int day = Integer.parseInt(st.nextToken());
			int month = Integer.parseInt(st.nextToken());
			int month_3 = Integer.parseInt(st.nextToken());
			int year = Integer.parseInt(st.nextToken());
			
			int[] arr = new int[12];
			
			st = new StringTokenizer(br.readLine());
			
			for(int i=0; i<12; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
				
			}
			
			if(month > month_3) {
				
			}
			
			
			
		}
		
	}
}
