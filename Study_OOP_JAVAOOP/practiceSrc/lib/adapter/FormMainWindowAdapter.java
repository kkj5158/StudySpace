package lib.adapter;

import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

/*
 윈도우 api 함수를 사용하여서 프로그래밍 구현하기. -> gui 끼리의 결합과정을 컨테이너와 컴포넌트 개념을 더하여 설명하기. 
이를 학생들에게 설명하여라. -> 질문리스트 추가 
*/ 

public class FormMainWindowAdapter extends WindowAdapter {
	public void windowClosing(WindowEvent e) {
		System.exit(0);
	}
	
	
}