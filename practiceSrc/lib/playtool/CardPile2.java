package lib.playtool;

/**
 * CardPile1 하고 비교하면서 더 기능적이고 좋은 코드를 짤려면 어떻게 짜야하는지. 내가 실수한 부분은 어디인지 피드백 받기 
 */

import java.awt.Graphics;

import lib.figure.Rect;

public class CardPile2 extends Rect {

	final static int MAXCARDS = 52;

	final static int PileWidth = 50;
	final static int PileHeight = 70;

	private Card[] thepile = new Card[MAXCARDS];
	private int restCard;

	public Card[] getThepile() {
		return thepile;
	}

	public void setThepile(Card[] thepile) {
		this.thepile = thepile;
	}

	public int getRestCard() {
		return restCard;
	}

	public void setRestCard(int restCard) {
		this.restCard = restCard;
	}

	public CardPile2(int x1, int y1) {
		upperLeftX = x1;
		upperLeftY = y1;
		lowerRightX = x1 + PileWidth;
		lowerRightY = y1 + PileHeight;
		int count = 0;

		for (int i = 0; i < 4; i++) {
			for (int j = 1; j < 14; j++) {
				thepile[count] = new Card(upperLeftX, upperLeftY, i, j);
				count++;
			}
		}

	}

	public void draw(Graphics g) {
		super.draw(g);
		g.drawString("DECK", upperLeftX, upperLeftY);
		g.drawLine(upperLeftX + 15, upperLeftY + 5, upperLeftX + 15, upperLeftY + 65);
		g.drawLine(upperLeftX + 35, upperLeftY + 5, upperLeftX + 35, upperLeftY + 65);
		g.drawLine(upperLeftX + 5, upperLeftY + 20, upperLeftX + 45, upperLeftY + 20);
		g.drawLine(upperLeftX + 5, upperLeftY + 35, upperLeftX + 45, upperLeftY + 35);
		g.drawLine(upperLeftX + 5, upperLeftY + 50, upperLeftX + 45, upperLeftY + 50);
	}

	public int findSelectedCardNum(int x, int y) {

		int cardnum = -1;

		for (int i = 0; i < MAXCARDS; i++) {
			if (thepile[i].includes(x, y) == true) {
				cardnum = i;
				break;
			}
		}

		return cardnum;
	}

}
