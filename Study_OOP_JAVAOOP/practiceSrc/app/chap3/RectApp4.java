package app.chap3;

import java.awt.Frame;
import java.awt.Graphics;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import lib.adapter.FormMainWindowAdapter;

public class RectApp4 extends Frame {
	
	private int x1;
	private int x2;
	private int y1;
	private int y2;
	
	private boolean firstClick = true;
	
	public RectApp4() {
		this.setVisible(true);
		this.setSize(1200, 600);
		this.addWindowListener(new FormMainWindowAdapter());
		this.addMouseListener(new MouseKeeper());
	}
	
	public static void main(String[] args) {
		
		RectApp4 f1 = new RectApp4();
	}
	
	
	private class MouseKeeper extends MouseAdapter{

		@Override
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


	@Override
	public void paint(Graphics g) {
		g.drawLine(x1, y1, x2, y2);
	}
	
	

}
