package app.chap3;

import java.awt.*;
import java.awt.event.*;
import lib.adapter.FormMainWindowAdapter;
import lib.figure.ColorRect;

@SuppressWarnings("serial")
public class RectApp2 extends Frame {

	public boolean firstClick = true;
	public ColorRect rect = new ColorRect();
	public int wsu = 5;
	public int hsu = 5;

	public RectApp2() {
		this.setVisible(true);
		this.setSize(900, 1600);
		this.addWindowListener(new FormMainWindowAdapter());
		this.addMouseListener(new MouseKeeper());

	}

	public static void main(String[] args) {
		RectApp2 f1 = new RectApp2();

	}

	private class MouseKeeper extends MouseAdapter {

		int mouse;

		public void mousePressed(MouseEvent e) {
			int x = e.getX();
			int y = e.getY();

			mouse = e.getButton();

			if (mouse == MouseEvent.BUTTON1) {

				if (firstClick) {
					rect.setLeftupperx(x);
					rect.setLeftuppery(y);
					firstClick = false;
				} else {
					rect.setRightdownx(x);
					rect.setRightdowny(y);
					
					rect.setWidth();
					rect.setHeight();
					
					firstClick = true;
					repaint();
				}
			}

			else {
				
				rect.sizeUP(wsu, hsu);
				repaint();

			}

		}
	}

	public void paint(Graphics g) {
		if (rect != null)
			rect.draw(g);
	}

}

