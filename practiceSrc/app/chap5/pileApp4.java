package app.chap5;

import java.awt.*;
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.Random;

import lib.adapter.FormMainWindowAdapter;
import lib.playtool.Card;
import lib.playtool.CardPile;

//=====================================================
//Card Application in Java
//오른쪽 버튼으로 디스카드 파일의 접고 펼치기
//펼쳐진 상태에서 개별적 카드 선택시 뒤집기
//DeckPile 클래스의 select 메소드에서 faceup 조정
//모두 뒷면 버튼 생성
//클릭시 평쳐진 디스카드 파일의 모든 카드를 뒷면으로
//윈도우 closing 버튼 동작
//모두 뒷면 버튼, 윈도우 closing 버튼 다중 상속
/**
++ question 더하기 : IDE를 사용하지 않고 폴더 디렉토리 구조에서 메모장을 사용해서 프로젝트 진행해보기
-> 무엇을 배울수 있는지에 대해서 상상해보자. 
컴파일도 직접 cmd 창을 이용해서 시도해보자. 구동역시. 실행해보면서 무엇을 배울수 있을지에대해서 상상해보자. 
**/

// 내 프로젝트 코드들은 모두들 인지하고 관리하기, node에서는 내가 작성하고 있는 글들 관리하고 , 깃허브 블로그 통해서 코드관리하기 , 노드에서 기술 관련 글들 작성하고 블로그 관리하기
// 내프로젝트 내코드들 내 기술관련 글들 내 글들 하나하나 작성해나가기 

//git
// 코드흐름 공부흐름 복구하기 

class DeckPile extends CardPile {

	public DeckPile(int x, int y) {

		super(x, y);

		for (int i = 0; i < 4; i++)
			for (int j = 0; j <= 12; j++)
				addCard(new Card(0, 0, i, j));

		// 카드 섞기
		Random generator = new Random();
		for (int i = 0; i < 52; i++) {
			int j = Math.abs(generator.nextInt() % 52);
			// 카드 치환
			Card tempCard = thePile[i];
			thePile[i] = thePile[j];
			thePile[j] = tempCard;
		}

	}

	public void select(int tx, int ty) {
		if (count == 0)
			return;
		Card tempCard = topCard();
//		tempCard.flip();						//======
		pileApp4.theDiscard.addCard(tempCard);
	}

}

public class pileApp4 extends Frame {

	public static DeckPile theDeck;
	public static CardPile theDiscard;
	public boolean wideDisplay = false;

	public pileApp4() {
		this.setVisible(true);
		this.setSize(1200, 600);
		this.setTitle("Pile 응용");
		this.addWindowListener(new FormMainWindowAdapter());
		this.addMouseListener(new MouseKeeper());

		theDeck = new DeckPile(100, 100);
		theDiscard = new CardPile(200, 100);

		DualListener dual = new DualListener();

	}

	public static void main(String[] args) {
		pileApp4 window = new pileApp4();
	}

	private class MouseKeeper extends MouseAdapter {

		public void mousePressed(MouseEvent e) {
			int x = e.getX();
			int y = e.getY();
			// ======
			if (e.getButton() == MouseEvent.BUTTON3) {
				if (theDiscard.includes(x, y)) {
					if (wideDisplay)
						wideDisplay = false;
					else if (theDiscard.thePile[theDiscard.count - 1].includes(x, y))
						wideDisplay = true;
					repaint();
				}
			} else {
				if (theDeck.includes(x, y))
					theDeck.select(x, y);
				if (theDiscard.includes(x, y)) { // ======
					for (int i = 0; i < theDiscard.count; i++) {
						if (theDiscard.thePile[i].includes(x, y)) {
							theDiscard.thePile[i].flip();
							break;
						}
					}
				}
				repaint();
			}
		}
	}

	private class DualListener extends WindowAdapter implements ActionListener {
		// Window
		public void windowClosing(WindowEvent e) {
			System.exit(0);
		}

		// Button
		public void actionPerformed(ActionEvent e) {
			if (wideDisplay) {
				for (int i = 0; i < theDiscard.count; i++)
					theDiscard.thePile[i].setFaceup(false);
			}
			repaint();
		}

	}
	

	@Override
	public void paint(Graphics g) {

		theDeck.display(g);

		if (wideDisplay)
			theDiscard.display(g, Card.cardWidth);
		else
			theDiscard.display(g);
	}

}
