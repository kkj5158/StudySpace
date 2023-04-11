/*
 * 프레잌 클래스를 띄우고 마우스 왼쪽클릭. 오른쪽클릭 설정하기 
 */

package chap2;

import java.awt.*;
import java.awt.event.*;
import java.util.Scanner;

@SuppressWarnings("serial")
public class MouseListenerpt1 extends Frame {

	public Point ptn = new Point();

	public String leftstr = new String("왼쪽 클릭 ");
	public String rightstr = new String("오른쪽 클릭");

	public int flag = 0;

	public MouseListenerpt1() {
		setTitle("Ex2");
		setSize(600 , 1200);

		addMouseListener(new mouseKeeper());
	}

	public static void main(String[] args) {

		MouseListenerpt1 window = new MouseListenerpt1();

		window.setVisible(true);

	}

	private class mouseKeeper implements MouseListener {

		@Override
		public void mouseClicked(MouseEvent e) {
			// TODO Auto-generated method stub

		}

		@Override
		public void mousePressed(MouseEvent e) {
			ptn = e.getPoint();

			if (e.getButton() == MouseEvent.BUTTON1) {
				flag = 0;
				repaint();

			} else if (e.getButton() == MouseEvent.BUTTON3) {
				flag = 1;
				repaint();
			}

		}

		@Override
		public void mouseReleased(MouseEvent e) {
			// TODO Auto-generated method stub

		}

		@Override
		public void mouseEntered(MouseEvent e) {
			// TODO Auto-generated method stub

		}

		@Override
		public void mouseExited(MouseEvent e) {
			// TODO Auto-generated method stub

		}

	
	}
	
	public void paint(Graphics g) {
		if (flag == 0) {
			g.drawString(leftstr, ptn.x, ptn.y);
		} else if (flag == 1) {
			g.drawString(rightstr, ptn.x, ptn.y);
		}
	}
}

/*
 *  프레임 닫는법 설정하는법 익히기 
 */
