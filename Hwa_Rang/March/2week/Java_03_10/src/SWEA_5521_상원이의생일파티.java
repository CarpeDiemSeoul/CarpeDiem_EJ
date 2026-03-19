import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;

public class SWEA_5521_상원이의생일파티 {
	
	static int[][] bestFriends;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int t = Integer.parseInt(br.readLine().trim());
		for(int tc=1; tc<=t; tc++) {
			
			st = new StringTokenizer(br.readLine().trim());
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			
			bestFriends = new int[n+1][n+1];
			List<Integer> myFriends = new ArrayList<>();
			Set<Integer> guestSet = new HashSet<>();

			
			for(int i=1; i<=m; i++) {
				st = new StringTokenizer(br.readLine().trim());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				
				bestFriends[a][b] = bestFriends[b][a] = 1;
				
				if(a == 1) {
					myFriends.add(b);
					guestSet.add(b);
				} 
			}
			
			for(int i: myFriends) {
				for(int j=2; j<n+1; j++) {
					if(bestFriends[i][j] == 1) guestSet.add(j);
				}
			}
			
			
			
			System.out.println("#"+tc+" "+guestSet.size());
			
			
			
			
		}//tc
	}
}
