
public class 동적계획법01_피보나치 {
	public static void main(String[] args) {
		System.out.println(fibo1(7));
	}
	
	static int fibo1(int N) {
		if(N < 2)
			return N;
		
		return fibo1(N-1)+fibo1(N-2);
	}
}
