package app.chap4;

import java.awt.*;
import java.awt.event.*;
import java.util.Random;

import lib.adapter.FormMainWindowAdapter;
import lib.figure.Rect;
import lib.playtool.Card;

// 경기장이 있고 . 10개의 카드를 5*2 배열로 생성 . 왼쪽 클릭시에는 카드 뒤집기 , 오른쪽 클릭 후 또 오른쪽 클릭후에는 카드 위치 이동 

// 카드 문양하고 숫자는 랜덤 

public class CardApp2 extends Frame {

	private Rect play;
	private Card[] cards = new Card[10];
	private Random random = new Random();

	public CardApp2() {
		this.setVisible(true);
		this.setSize(1200, 1600);
		this.addWindowListener(new FormMainWindowAdapter());
		this.addMouseListener(new MouseKeeper());

		play = new Rect(100, 100, 1000, 1000);

		int dx = 150;
		int dy = 300;

		for (int i = 0; i < cards.length; i++) {

			int suit = random.nextInt(3);
			int rank = random.nextInt(13);

			if (i == cards.length / 2) {
				dx = 150;
				dy = 500;
			}

			cards[i] = new Card(dx, dy, suit, rank);

			dx = dx + 100;

		}

	}

	public static void main(String[] args) {

		CardApp2 window1 = new CardApp2();

	}

	private class MouseKeeper extends MouseAdapter {

		private boolean firstClick = true;
		private int index;

		@Override
		public void mousePressed(MouseEvent e) {

			int mouse = e.getButton();

			if (mouse == MouseEvent.BUTTON1) {

				for (int i = 0; i < cards.length; i++) {
					if (cards[i].includes(e.getX(), e.getY()) == true) {
						cards[i].flip();
						repaint();
						break;
					}
				}

			}

			if (mouse == MouseEvent.BUTTON3) {
				if (firstClick) {	

					for (int i = 0; i < cards.length; i++) {
						if (cards[i].includes(e.getX(), e.getY())) {
							firstClick = false;
							index = i;
							break;
						}
					}

				}

				else {
					cards[index].setUpperLeftX(e.getX());
					cards[index].setUpperLeftY(e.getY());
					cards[index].setLowerRightX(e.getX() + Card.cardWidth);
					cards[index].setLowerRightY(e.getY() + Card.cardHeight);
					firstClick = true;
					repaint();
				}
			}

		}

	}

	@Override
	public void paint(Graphics g) {

		play.draw(g);

		for (int i = 0; i < cards.length; i++) {
			cards[i].draw(g);
		}

	}

}
