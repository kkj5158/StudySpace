package lib.playtool;

import java.awt.Color;
import java.awt.Graphics;
import java.util.Random;

/**
 * 추가해야할 기능 
 * 
 * 1. 카드덱 비우기 0
 * 
 * 2. 카드덱 max까지 한번에 쭉 채우기 기능 (랜덤카드 ) (이미 채워진 카드가 있으면, 그 카드 위로 카드를 채워넣는다. )
 * 
 * 3. 카드를 원하는 숫자만큼 구현하는 기능 (이미 채워진 카드가 있으면, 그 카드 위로 카드를 채워넣는다. )
 * 
 * 4. 
 * 
 *
 * @author KJS
 *
 */

public class CardPile {
	
	final static int MAXCARDS = 52;
	
	public int x;
	public int y;
	public Card thePile[];
	public int count;
	public boolean wideDisplay;
	
	Random rand = new Random();
	public int suit;
	public int rank;
	
	public CardPile(int xl, int yl) {
		x = xl; y = yl;
		thePile = new Card[MAXCARDS];
		count = 0;
		wideDisplay = false;
	}
	
	public void addCard(Card aCard) {
		if(count < MAXCARDS) {
			thePile[count] = aCard;
			aCard.moveTo(x, y);
			count = count + 1;
		}
	}
	
	public void addAllCard() {
		if(count < MAXCARDS) {
			for(int i = count; i<MAXCARDS; i++)
			{
				
			}
		}
	}
	
	
	public void pullEveryCard() {
		count = 0;
	}
	
	
	
	
	public Card topCard() {
		if(count > 0) {
			count = count - 1;
			return thePile[count];
		}
		return null;
	}
	
	public boolean includes(int tx, int ty) {
		//======
		for(int k = count; k > 0; k--)
			if(thePile[k-1].includes(tx, ty))
				return true;
		return false;
	}
	
	public void select(int tx, int ty) {
		// do nothing
	}
	
	
	

	public void display(Graphics g) {
		g.setColor(Color.orange);
		if(count == 0)
			g.drawRect(x, y, Card.cardWidth, Card.cardHeight);
		else
			thePile[count-1].draw(g);
	}
	
	public void display(Graphics g, int xOffset) {
		g.setColor(Color.orange);
		if(count == 0)
			g.drawRect(x, y, Card.cardWidth, Card.cardHeight);
		else {
			int tx = 0;
			for(int i = count; i > 0; i--) {
				thePile[i-1].moveTo(x+tx, y);
				thePile[i-1].draw(g);
				tx = tx + xOffset;
			}
		}
	}
	
	
	public boolean canTake(Card aCard) {
		return false; 
	}
	




}
