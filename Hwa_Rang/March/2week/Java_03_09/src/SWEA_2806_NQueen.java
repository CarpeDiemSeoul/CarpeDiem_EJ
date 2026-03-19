import java.util.Scanner;

public class SWEA_2806_NQueen {
	static int N; 	//n개의 Queen
	static int[] col; 	//배치
	static int ans; 	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc = 1; tc <= T; tc++) {
			N = sc.nextInt();
			col = new int[N];
			ans = 0;
			
			System.out.println("#"+tc+" "+ans);
		}
	}
	
	//row번째 행에 퀸을 놓겠다
	static void make(int row) {
		//종료파트
		if(row == N) {
			ans++;
			return;
		}
		//재귀파트
		
		//row행에 c열 위치에 두겠다!
		for(int c = 0; c<N; c++) {
			col[row] = c;
			
			//유망성 검사를 통해 별 이상이 없다면 다음 스텝으로...
			if(isPossible(row)) {
				make(row+1);
			}
		}
		
		
	}
	
	static boolean isPossible(int row) {
		for(int i=0; i<row; i++) {
			//같은 열이면 불가능
			if(col[i] == col[row]) {
				return false;
			}
			//대각선에 있으면 불가능
			if(Math.abs(row-i) == Math.abs(col[row] - col[i])) {
				return false;
			}
		}
		
		return true;
	}
}
