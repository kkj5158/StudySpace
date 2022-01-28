/*
 * gui를 띄오고 나서 마우스 왼쪽 오른쪽 클릭에 따라서 왼쪽클릭, 오른쪽 클릭 내용 출력하기 
 */

package chap2;

import java.awt.*;
import java.awt.event.*;


@SuppressWarnings("serial")
public class MouseListenerex3 extends Frame {
	
	public Point newp = null;
	
	public String str1 = new String("왼쪽 클릭");
	public String str2 = new String("오른쪽 클릭");
	
	public int flag = 0;
	
	public static void main(String[] args) {
		MouseListenerex3 window = new MouseListenerex3();
		window.setVisible(true);		
	}
	

	public MouseListenerex3() {
		setSize(600, 500);
		setTitle("frame 공부중");
		
		MouseKeeper mouse = new MouseKeeper();
		addMouseListener(mouse);
		
		
		
	}
	
	private class MouseKeeper extends MouseAdapter{
		
		public void mousePressed(MouseEvent e) {
			
			newp = e.getPoint();

			
			if(e.getButton() == MouseEvent.BUTTON1) {
				flag = 0;
				repaint();
			}
			else if(e.getButton() == MouseEvent.BUTTON3) {
				flag = 1;
				repaint();
			}
		}
	}
	
	public void paint(Graphics g) {
		if(flag == 0) {
		g.drawString(str1, newp.x, newp.y);
		}
		else if(flag == 1) {
			g.drawString(str2, newp.x, newp.y);
		}
	}

}

//import 명령어가 패키지 명에 따른 폴더구조를 사용자 시스템내에 설치해준다. -> import 명령어 정리하기
// 열혈 자바 책 참고하기 
/*
* 프레임 클레스에 대한 이해 -> 프레임을 어떻게 생성하는가 / 설정하는가 
* 마우스 이벤트 이해하기 
* 프레임에 텍스트 출력하기 
*/




