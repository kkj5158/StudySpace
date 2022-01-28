package app.chap1;
import java.util.Scanner;

//=============================================================
//Simple Grade Application in Java
//정수형 배열의 크기를 입력받고 크기만큼의 점수를 입력받아 평균을 구함
//각 점수가 평균 이상이면 pass, 이하면 fail을 출력
//=============================================================


public class GradeApp {
	
	
	public static void main(String[] args) {
		int n;
		int sum = 0;
		double avg;
		
		Scanner s = new Scanner(System.in);
		
		System.out.print("점수의 갯수를 입력하시오 " );
		n = s.nextInt();
		
		int score[] = new int[n];
		
		for(int i=0; i<score.length; i++)
		{
			System.out.print("점수를 입력하시오 " );
			score[i] = s.nextInt();
			sum = sum + score[i];
		}
		
		s.close();
		
		avg = sum/score.length;
		
		for(int i=0; i<score.length;  i++ ) {
			if(score[i] >= avg)
			System.out.println("pass");
			else
			System.out.println("fail");
		}
		
		

		
		
	}

}

/*
 * 
 * 
 */
