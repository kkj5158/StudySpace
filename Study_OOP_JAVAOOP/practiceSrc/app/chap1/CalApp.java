package app.chap1;
import java.util.Scanner;

public class CalApp {
	
	public static void main(String[] args) {
		double x,y;
		int op;
		Scanner sc = new Scanner(System.in);
		
		System.out.println("두 실수를 입력하세요 ");
		
		x = sc.nextDouble();
		y = sc.nextDouble();
		
		System.out.println("원하는 연산의 번호를 선택하세요");
		System.out.println("(1) + , (2) -, (3) *, (4) /: ");
		
		op = sc.nextInt();
		
		switch(op) {
		
		case 1: System.out.println("덧셈 결과는 " + (x+y) + "입니다.");
				break;
		case 2: System.out.println("뺄셈 결과는 " + (x-y) + "입니다.");
				break;
		case 3: System.out.println("곱셈 결과는 " + (x*y) + "입니다.");
				break;
		case 4: System.out.println("나눗셈 결과는 " + (x/y) + "입니다.");
				break;
		default:
				System.err.println("입력 오류!!");
		}
		
		sc.close();
	}

}

/*


*/