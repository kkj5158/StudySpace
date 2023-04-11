/*
 * 프레임 클래스 생성후 종료 이벤트 실행시켜보기 - 윈도우 api와의 연관성 생각하기 
 */

package chap2;

import java.awt.Frame;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;

import javax.swing.JFrame;

@SuppressWarnings("serial")
public class FrameCloseex1 extends Frame {
	
	public FrameCloseex1() {
		this.setVisible(true);
		this.setSize(600, 300);
		this.addWindowListener(new FormMainWindowAdapter());
	}
	
	public static void main(String[] args) {
		
		FrameCloseex1 f1 = new FrameCloseex1();
		
		f1.setVisible(true);
		f1.setSize(600, 300);
		
	}
	
	
	
	

}

class FormMainWindowAdapter extends WindowAdapter{
	public void windowClosing(WindowEvent e) {
		System.exit(0);
	}
}
