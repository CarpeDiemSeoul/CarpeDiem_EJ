import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Set;
import java.util.StringTokenizer;

public class BOJ_15651_N과M_3 {

	static int[] result;
	static StringBuilder sb = new StringBuilder();
	
	static int n, m;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		result = new int[m];
		
		dfs(0);
		
		System.out.println(sb.toString());

	}
	
	static void dfs(int depth) {
		
		
		if(depth == m) {
			for(int i: result) {
				sb.append(i).append(" ");
			}
			sb.append("\n");
			return;
		}
		
		
		for(int i=1; i<=n; i++) {
			
			result[depth] = i;
			dfs(depth+1);
			
		}
		
	}
}
