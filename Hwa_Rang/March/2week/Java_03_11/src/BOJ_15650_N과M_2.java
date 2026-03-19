import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Set;
import java.util.StringTokenizer;

public class BOJ_15650_N과M_2 {

	static int[] result;
	static StringBuilder sb = new StringBuilder();
	
	static int n, m;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		result = new int[m];
		
		dfs(0, 1);
		
		System.out.println(sb.toString());

	}
	
	static void dfs(int depth, int v) {
		
		
		if(depth == m) {
			for(int i: result) {
				sb.append(i).append(" ");
			}
			sb.append("\n");
			return;
		}
		
		
		for(int i=v; i<=n; i++) {
			if(depth == 0 && i == n && m != 1) break;
			
			result[depth] = i;
			dfs(depth+1, i+1);
			
		}
		
	}
}
