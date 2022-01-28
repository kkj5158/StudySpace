package lib.playtool;

import java.awt.Color;
import java.awt.Graphics;

import lib.figure.Rect;

public class Card extends Rect {

	final public static int cardWidth = 50;
	final public static int cardHeight = 70;

	final public static int heart = 0;
	final public static int spade = 1;
	final public static int diamond = 2;
	final public static int club = 3;

	private boolean faceup;
	private int suit;
	private int rank;

	public Card(int ulx, int uly, int suit, int rank) {

		super(ulx, uly, ulx + 50, uly + 70);

		this.suit = suit;
		this.rank = rank;
	}
	
	
	

	public boolean isFaceup() {
		return faceup;
	}




	public void setFaceup(boolean faceup) {
		this.faceup = faceup;
	}




	public int getSuit() {
		return suit;
	}




	public void setSuit(int suit) {
		this.suit = suit;
	}




	public int getRank() {
		return rank;
	}




	public void setRank(int rank) {
		this.rank = rank;
	}




	public void flip() {
		faceup = !faceup;
	}

	public Color color() {

		if (faceup)
			if (suit == heart || suit == diamond)
				return Color.red;
			else
				return Color.black;
		return Color.blue;

	}

	public void draw(Graphics g) {
		String names[] = { "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" };
		// 카드 면 확보와 경계선 그리기
		g.clearRect(upperLeftX, upperLeftY, cardWidth, cardHeight);
		super.draw(g);
		// 각 카드의 이미지 그리기
		g.setColor(color());
		if (faceup) {
			g.drawString(names[rank], upperLeftX + 3, upperLeftY + 15);
			if (suit == heart) {
				g.drawLine(upperLeftX + 25, upperLeftY + 30, upperLeftX + 35, upperLeftY + 20);
				g.drawLine(upperLeftX + 35, upperLeftY + 20, upperLeftX + 45, upperLeftY + 30);
				g.drawLine(upperLeftX + 45, upperLeftY + 30, upperLeftX + 25, upperLeftY + 60);
				g.drawLine(upperLeftX + 25, upperLeftY + 60, upperLeftX + 5, upperLeftY + 30);
				g.drawLine(upperLeftX + 5, upperLeftY + 30, upperLeftX + 15, upperLeftY + 20);
				g.drawLine(upperLeftX + 15, upperLeftY + 20, upperLeftX + 25, upperLeftY + 30);
			} else if (suit == spade) {
				g.drawLine(upperLeftX + 25, upperLeftY + 20, upperLeftX + 40, upperLeftY + 50);
				g.drawLine(upperLeftX + 40, upperLeftY + 50, upperLeftX + 10, upperLeftY + 50);
				g.drawLine(upperLeftX + 10, upperLeftY + 50, upperLeftX + 25, upperLeftY + 20);
				g.drawLine(upperLeftX + 23, upperLeftY + 45, upperLeftX + 20, upperLeftY + 60);
				g.drawLine(upperLeftX + 20, upperLeftY + 60, upperLeftX + 30, upperLeftY + 60);
				g.drawLine(upperLeftX + 30, upperLeftY + 60, upperLeftX + 27, upperLeftY + 45);
			} else if (suit == diamond) {
				g.drawLine(upperLeftX + 25, upperLeftY + 20, upperLeftX + 40, upperLeftY + 40);
				g.drawLine(upperLeftX + 40, upperLeftY + 40, upperLeftX + 25, upperLeftY + 60);
				g.drawLine(upperLeftX + 25, upperLeftY + 60, upperLeftX + 10, upperLeftY + 40);
				g.drawLine(upperLeftX + 10, upperLeftY + 40, upperLeftX + 25, upperLeftY + 20);
			} else if (suit == club) {
				g.drawOval(upperLeftX + 20, upperLeftY + 25, 10, 10);
				g.drawOval(upperLeftX + 25, upperLeftY + 35, 10, 10);
				g.drawOval(upperLeftX + 15, upperLeftY + 35, 10, 10);
				g.drawLine(upperLeftX + 23, upperLeftY + 45, upperLeftX + 20, upperLeftY + 55);
				g.drawLine(upperLeftX + 20, upperLeftY + 55, upperLeftX + 30, upperLeftY + 55);
				g.drawLine(upperLeftX + 30, upperLeftY + 55, upperLeftX + 27, upperLeftY + 45);
			}
		} else { // 뒷면
			g.drawLine(upperLeftX + 15, upperLeftY + 5, upperLeftX + 15, upperLeftY + 65);
			g.drawLine(upperLeftX + 35, upperLeftY + 5, upperLeftX + 35, upperLeftY + 65);
			g.drawLine(upperLeftX + 5, upperLeftY + 20, upperLeftX + 45, upperLeftY + 20);
			g.drawLine(upperLeftX + 5, upperLeftY + 35, upperLeftX + 45, upperLeftY + 35);
			g.drawLine(upperLeftX + 5, upperLeftY + 50, upperLeftX + 45, upperLeftY + 50);
		}
	}
	
	
}
