package app.chap5;

import java.awt.Frame;
import java.awt.Graphics;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import lib.adapter.FormMainWindowAdapter;
import lib.playtool.CardPile;

public class PileApp2 extends Frame {
	
	private CardPile deck = new CardPile(0, 0);

	public static void main(String[] args) {
		
		

	}
	
	public PileApp2() {
		this.setVisible(true);
		this.setSize(1200, 600);
		this.addWindowListener(new FormMainWindowAdapter());
		this.addMouseListener(new MouseKeeper());
		
	}
	
	private class MouseKeeper extends MouseAdapter{
		
		private boolean firstClick = true;

		@Override
		public void mousePressed(MouseEvent e) {
			

		}
		
		
		
		
		
		
	
	}
	
	
	public void paint(Graphics g) {
		
		deck.display(g);
	}
	
	
	
	

}
