import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SWEA_14510_나무높이 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		int[] tree = new int[n];
		
		int max = 0;
		int idx = 0;
		
		for(int i=0; i<n; i++) {
			tree[i] = Integer.parseInt(br.readLine());
			if(max < tree[i]) {
				max = tree[i];
				idx = i;
			}
		}
		
		int date = 0;
		
		
		
	}
}
