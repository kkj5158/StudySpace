package app.chap2;


import java.awt.*;
import java.awt.event.*;

@SuppressWarnings("serial")
public class PenApp2 extends Frame {
	
	public int count = 0;
	public Point pnt = null;
	
	public PenApp2() {
		setSize(600, 500);
		setTitle("몇 번째 선일까요 ?");
		
		MouseKeeper mouse = new MouseKeeper();
		addMouseListener(mouse);
	
	}
	

	public static void main(String[] args) {
		
		PenApp2 window = new PenApp2();
		window.setVisible(true);

	}
	
	
	private class MouseKeeper extends MouseAdapter{
		
		public void mousePressed(MouseEvent e) {
			pnt = e.getPoint();
			
			count = count + 1;
			
			repaint();
		}
	} 
	
	public void paint(Graphics g) {
		g.drawLine(0, 0, pnt.x, pnt.y);
		String str = count + "번째 선 ";
		g.drawString(str, pnt.x, pnt.y);
	}
	
	

}



/*
 * chap 02 java gui 구현하기 : 다양한 개념 공부하고 복습하기 
 * 
 * 
 * 
 * Q0 . 프레임 클래스는 무엇인가 .
 * 
 * Q1 . 리스너랑 어댑터 클래스란 무엇인가 . 
 * 
 * https://coding-factory.tistory.com/262
 * 
 * 	1) 이벤트 , 리스너 , 어댑터 개념 이해하기 
 * 
 * 	2) 이벤트 프로그래밍이란 무엇인가 
 * 
 * 	3) 
 * 
 * 
 * 
 * Q. 네스티드 클래스란 무엇인가 (개념 공부하기 ) , 아우터 , 이너 클래스는 무엇인가 
 * https://sims-solve.tistory.com/12
 * 
 * 	네스티드. 이너클래스의 존재 이유는 무엇인가, 장점은 무엇인가
 * 
 * 	메인함수에서 네스티드,이너 클래스에 어떻게 접근해야하는가 . 
 */

/*
 * 
 * 
 * 
 * 
 */
