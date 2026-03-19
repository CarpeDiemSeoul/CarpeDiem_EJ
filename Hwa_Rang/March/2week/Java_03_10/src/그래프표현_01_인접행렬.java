import java.util.Scanner;

public class 그래프표현_01_인접행렬 {
	public static void main(String[] args) {
		//V E 정점의 수, 간선의 수
		//0 1
		//0 2 ... E개의 줄에 걸쳐 시작 정점, 도착정점이 주어진다.
		Scanner sc = new Scanner(System.in);
		int V = sc.nextInt();//정점의 수: 시작 정점의 번호가 0인지 1인지를 확인
		int E = sc.nextInt();//간선의 수: 두 개의 정점을 준다. -> 순서대로 준 것인지 확인
		
		//인접행렬 2차원 배열: 값은 1로 표현, 가중치가 있다면 해당 값으로 표현
		//간선이 있으면 1, 없으면 0 -> boolean이 좋지 않나? -> 차수계산등 여러 이유로 인해 int형이 편하다.
		int[][] adjArr = new int[V][V];//0번 정점부터 시작한다.
		
		//간선입력
		for(int i=0; i<E; i++) {
			//0 1 10 (시작정점, 도착정점, 가중치)
			int A = sc.nextInt();
			int B = sc.nextInt();
			int W = sc.nextInt(); //가중치가 있다면... 입력없으면 생략
			
			//adjArr[A][B] = 1; 유,무향 상관없이 저장 
			adjArr[A][B] = adjArr[B][A] = 1; //무향일 경우 반대의 경우도 저장
			
			adjArr[A][B] = adjArr[B][A] = W; //한 줄로 가능
		}
	}
}
