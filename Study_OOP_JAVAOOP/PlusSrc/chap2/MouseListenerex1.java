package chap2;

import java.awt.*;
import java.awt.Frame;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

/* 다양한 마우스 리스너 인터페이스의 메소드들 오버라이딩해서 사용해보기 */
/* 1. 오른쪽 왼쪽 클릭에 따른 문자열 출력 구분 */


@SuppressWarnings("serial")
public class MouseListenerex1 extends Frame {
	
	public int x1;
	public int y1;

	public String str1 = "left click";
	public String str2 = "right click";
	
	public int mousestate = 100;
	
	public static void main(String[] args) {
		
		MouseListenerex1 f1 = new MouseListenerex1();
		
		
	}
	
	public MouseListenerex1() {
		setVisible(true);
		setSize(1200, 600);
		addWindowListener(new FormMainWindowAdapter());
		addMouseListener(new MouseKeeper());

	}
	
	public void paint(Graphics g) {
		g.setColor(Color.BLUE);
		
		if(mousestate == 0) {
		g.drawString(str1, x1, y1);
		}
		else if(mousestate == 1) {
			g.drawString(str2, x1, y1);
		}
	}
	
	private class MouseKeeper extends MouseAdapter{
		
		public void mousePressed(MouseEvent e) {
			
			//System.out.println("mouse event");
			
			if(e.getButton() == MouseEvent.BUTTON1)
			{
				//System.out.println("getbutton");
				mousestate = 0;
				
				x1=e.getX();
				y1=e.getY();
				
				repaint();
				
			}
			else if(e.getButton() == MouseEvent.BUTTON3)
			{
				//System.out.println("getbutton2");

				mousestate = 1;
				
				x1=e.getX();
				y1=e.getY();
				
				repaint();
			}
		}

	


}



}


