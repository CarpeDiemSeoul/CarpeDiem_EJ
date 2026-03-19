import java.util.Scanner;

//비트마스킹 방식도 가능하다 -> 추후에 언젠가 해볼것!

public class SWEA_2806_NQueen2 {
	static int N; // 개의 Queen
	static int ans;
	static boolean[] usedCol; //해당열을 사용했는가
								//값의 범위는 0 ~ (2*N-2)
	static boolean[] usedDiag1; //  /(우상향)대각선 사용여부 row+col이 같음
	static boolean[] usedDiag2; //  \(좌상향)대각선 사용여부 row-col이 같음(음수가 나오므로 N-1 만큼 쉬프트)
	

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			N = sc.nextInt();
			usedCol = new boolean[N];
			usedDiag1 = new boolean[2*N-1];
			usedDiag2 = new boolean[2*N-1];
			ans = 0;
			make(0);
			System.out.println("#"+tc +" "+ans);
		}//tc
	}//main
	
	
	//row번째 행에 퀸을 놓겠다!
	static void make(int row) {
		//종료파트
		if(row == N) {
			ans++;
			return;
		}
		//재귀파트
		//row 행에 c 열 위치에 두겠다!
		for(int col = 0; col<N; col++) {
			// 우상향 대각선 번호
			int d1 = row + col;
			// 좌상향 대각선 번호
			int d2 = row - col + N - 1;
			
			//이미사용중인 열, 대각선인 경우는 다음 스텝으로 넘어가자
			if(usedCol[col] || usedDiag1[d1] || usedDiag2[d2]) {
				continue;
			}
			
			///////////////////
			usedCol[col] = true;
			usedDiag1[d1] = true;
			usedDiag2[d2] = true;
			//////////////////
			make(row+1); //다음 스텝으로
			//////////////////
			usedCol[col] = false;
			usedDiag1[d1] = false;
			usedDiag2[d2] = false;
			/////////////////
			
		}
	}


	
	
	
	
	
	
	
	
	
	
	
}
