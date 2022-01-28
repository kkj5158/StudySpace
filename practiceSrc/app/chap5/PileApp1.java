package app.chap5;

import java.awt.Frame;
import java.awt.Graphics;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;


import lib.adapter.FormMainWindowAdapter;
import lib.playtool.Card;
import lib.playtool.CardPile;
import lib.playtool.CardPile2;

/* 덱에서 카드 펼치기를 할수 있는 프로그램 */


/**
 * 1. 카드덱 보이기 구현 0 / 카드 덱은 총 52장이 있다. 
 * 
 * 2. 덱위에서 왼쪽 첫번째 클릭시 가장위에 있는 카드 선택, 두번째 클릭에 필드를 선택할시. 그 필드 위치에 그 카드가 위치됨 ( 카드 이동 )
 * 
 * 3. 필드의 카드를 왼쪽 첫번째클릭시 선택, 두번째 클릭에 필드의 위치중 하나를 선택할시 , 그 필드 위치에 그 카드가 위치함 ( 카드 이동 )
 * 
 * 4. 필드의 카드를 오른쪽 클릭시. 그 필드의 카드가 플립( 뒤집히는 기능 ) 구현하기 . 
 * 
 * 
 * @author KJS
 *
 */


public class PileApp1 extends Frame {
	
	private CardPile deck = new CardPile(50 , 100);
	
	
	private int deckcount = 0;
	
	private int sdcardnum;
	private Card sdcard;
	
	
	public PileApp1() {
		this.setVisible(true);
		this.setSize(1200, 600);
		this.addWindowListener(new FormMainWindowAdapter());
		this.addMouseListener(new MouseKeeper());
	}
	
	
	public static void main(String[] args) {
		PileApp1 window1 = new PileApp1();
		
		
	}
	
	private class MouseKeeper extends MouseAdapter{
		
		private boolean firstClick = true;

		@Override
		public void mousePressed(MouseEvent e) {
			
			if(e.getButton()==MouseEvent.BUTTON1) {
				
				//deck 클릭시 
				if(firstClick && deck.includes(e.getX(), e.getY())) {
					sdcard = pile[deckcount++];				
					firstClick = false;
				}
				else if(firstClick == false) {
					
					sdcard.moveTo(e.getX(), e.getY());
					firstClick = true;
					repaint();
				}
				
			}
			else if(e.getButton() == MouseEvent.BUTTON3) {
				
				sdcardnum = deck.findSelectedCardNum(e.getX(), e.getY());
				
				if(sdcardnum != -1) {
					sdcard = pile[sdcardnum];
					sdcard.flip();
				}
				
		
				repaint();
			}
		}
		
	}

	@Override
	public void paint(Graphics g) {
		
		deck.display(g);
	}
	
	

}
