package app.chap2;

import java.awt.*;
import java.awt.event.*;

@SuppressWarnings("serial")
public class PenApp6 extends Frame {
	
	public int x1;
	public int y1;
	public int x2;
	public int y2;
	public boolean firstClick = true;
	
	public static void main(String[] args) {
		PenApp6 window = new PenApp6();
		window.setVisible(true);
	}
	
	public PenApp6() {
		setSize(600, 500);
		setTitle("Pen 응용");
		addMouseListener(new MouseKeeper());
		
	}
	
	private class MouseKeeper extends MouseAdapter{
		
		public void mousePressed(MouseEvent e) {
			if(firstClick) {
				x1 = e.getX();
				y1 = e.getY();
				firstClick = false;
			}
			else {
				x2 = e.getX();
				y2 = e.getY();
				firstClick = true;
				repaint();
			}
		}
	}
	
	public void paint(Graphics g) {
		g.setColor(Color.red);
		g.drawLine(x1, y1, x2, y1);
		g.drawLine(x1, y1, x1, y2);
		g.drawLine(x2, y2, x2, y1);
		g.drawLine(x2, y2, x1, y2);
		
	}
	
	

}

/*
	serial warning 의 의미는 무엇인가 ? 

*/