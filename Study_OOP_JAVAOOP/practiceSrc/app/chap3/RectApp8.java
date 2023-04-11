package app.chap3;

import java.awt.Color;
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import lib.adapter.FormMainWindowAdapter;
import lib.figure.ColorRect;

public class RectApp8 extends Frame {

	private int maxnumofRect = 10;
	private int Rectindex = 0;
	private ColorRect[] arrRect = new ColorRect[maxnumofRect];

	private boolean firstClick = true;
	private int mouseButton;

	public static void main(String[] args) {

		RectApp8 f1 = new RectApp8();

	}

	public void setfirstClicktoTrue() {
		firstClick = true;
	}

	public void setfirstClicktoFalse() {
		firstClick = false;
	}

	public RectApp8() {
		this.setVisible(true);
		this.setSize(1200, 600);
		this.addWindowListener(new FormMainWindowAdapter());
		this.addMouseListener(new MouseKeeper());
	}

	private class MouseKeeper extends MouseAdapter {

		@Override
		public void mousePressed(MouseEvent e) {

			if (Rectindex < maxnumofRect) {

				mouseButton = e.getButton();

				if (firstClick) {
					
					arrRect[Rectindex] = new ColorRect();
					
					arrRect[Rectindex].setLeftupperx(e.getX());
					arrRect[Rectindex].setLeftuppery(e.getY());
					setfirstClicktoFalse();
				} else {
					arrRect[Rectindex].setRightdownx(e.getX());
					arrRect[Rectindex].setRightdowny(e.getY());
					arrRect[Rectindex].setHeight();
					arrRect[Rectindex].setWidth();

					if (mouseButton == MouseEvent.BUTTON1) {

						arrRect[Rectindex].setColor(Color.blue);

					} else if (mouseButton == MouseEvent.BUTTON3) {

						arrRect[Rectindex].setColor(Color.red);

					}

					repaint();
					setfirstClicktoTrue();
					Rectindex++;
				}

			}

		}
	}

	@Override
	public void paint(Graphics g) {
		
			
			for(int i = 0; i< Rectindex; i++) {
				arrRect[i].draw(g);
			}
		

	}

}
