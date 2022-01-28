package app.chap1;

//=============================================================
//Simple Hello Application in Java
//실수들을 main의 인자로 전달받아 평균값을 구함
//=============================================================


public class HelloApp {
	
	public static void main(String[] args) {
		double sum = 0;
		
		for(int i = 0; i < args.length; i ++)
		{
			sum += Double.parseDouble(args[i]);
		}
		
		System.out.println("합 " + sum);
		System.out.println("평균" + sum/args.length);
	}

}

// cmd 에서 한번 확인하기 !! 

/* chap 01 java의 콘솔 입출력 구현하기 -> 콘솔 입출력 능숙해지기 */

/*
 * 
 * Q1. 패키지 경로란 무엇인가. 패키지에 대해서 구체적으로 설명하시오.
 * 
 * 	IDE를 사용하지 않고 메모장과 cmd 창을 이용하여 컴파일, 코딩 구현시 폴더 들이 어떻게 형성되는지 패키지 이름과 연관지어서 
 * 	실습해보고 설명하시오 
 * 
 * 
 * 
 */

