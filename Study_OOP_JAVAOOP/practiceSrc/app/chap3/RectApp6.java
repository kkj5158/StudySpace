package app.chap3;

import java.awt.Color;
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import lib.adapter.FormMainWindowAdapter;
import lib.figure.ColorRect;

public class RectApp6 extends Frame {

	private ColorRect rect = new ColorRect();

	public RectApp6() {
		this.setVisible(true);
		this.setSize(1200, 600);
		this.addWindowListener(new FormMainWindowAdapter());
		this.addMouseListener(new MouseKeeper());

		rect.setWidth(20);
		rect.setHeight(15);

	}

	public static void main(String[] args) {

		RectApp6 f1 = new RectApp6();

	}

	@Override
	public void paint(Graphics g) {

		if(rect != null)
			rect.draw(g);
	}

	private class MouseKeeper extends MouseAdapter {

		@Override
		public void mousePressed(MouseEvent e) {

			if (rect.checkRectIn(e.getX(), e.getY())) {

				int mouse = e.getButton();
				rect.setLeftupperx(e.getX());
				rect.setLeftuppery(e.getY());
				
				if (mouse == MouseEvent.BUTTON1) {
					rect.setColor(Color.blue);
					rect.sizeUP(10, 10);
					repaint();
				}
				else if (mouse == MouseEvent.BUTTON3) {
					rect.setColor(Color.red);
					rect.sizeUP(-10, -10);
					repaint();

				}

			}

		}
	}
}
