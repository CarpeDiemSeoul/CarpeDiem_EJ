import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_15649_N과M_1 {

	static int[] result;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		result = new int[m];
		
		dfs(n, m);

	}
	
	static void dfs(int n, int m) {
		if(m == 0) {
			for(int i: result) {
				System.out.print(i+" ");
			}
			System.out.println();
			return;
		}
		
		for(int i=1; i<=n; i++) {
			
			boolean isFind = false;
			for(int j=0; j<result.length; j++) {
				if(i == result[j]) {
					isFind = true;
					break;
				} 
			}
			
			if(isFind) continue;
			
			result[result.length-m] = i;
			
			dfs(n, m-1);
			
			result[result.length-m] = 0;
		}
		
	}
}
