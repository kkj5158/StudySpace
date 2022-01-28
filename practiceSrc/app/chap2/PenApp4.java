package app.chap2;

import java.awt.*;
import java.awt.event.*;

@SuppressWarnings("serial")
public class PenApp4 extends Frame {
	
	public Point oldp = null;
	public Point newp = null;
	
	public static void main(String[] args) {
		PenApp4 window = new PenApp4();
		window.setVisible(true);
	}
	
	public PenApp4() {
		setSize(500, 600);
		setTitle("renew lines");
		oldp = new Point(0,0);
		newp = new Point(0,0);

		
		MouseKeeper mouse = new MouseKeeper();
		addMouseListener(mouse);
		
	}
	
	private class MouseKeeper extends MouseAdapter{
		
		public void mousePressed(MouseEvent e) {
			
			oldp = newp;
			newp = e.getPoint();
			
			repaint();
		
		}
	}
	
	public void paint(Graphics g) {
		g.drawLine(oldp.x, oldp.y, newp.x, newp.y);
	}
	
	/*
	 * Q1.이벤트와 리스너 어댑터의 차이점은 무엇인가 . 
	 * https://coding-factory.tistory.com/262
	 * 
	 * 	이벤트 중심 프로그래밍이란 무엇인가 . 
	 * 
	 * Q2. repaint() 와 paint() 의 차이점은 무엇인가 . ? 
	 * 
	 */

	
	
	
	
	
	
	
	
	
	

}
