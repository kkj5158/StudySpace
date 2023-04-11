package hello.core.singleton;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

public class SingletonService {

    //1. static 영역에 객체를 딱 1개만 생성해둔다.

    private  static final SingletonService instance = new SingletonService();

    // 구체적인 구현 클래스의 존재 -> OCP 와 DI 원칙을 위배한다.

    /*
    앞서서 논의한 바와 같이, 두가지 원칙을 지키기 위해서 APPConfig와 같은 역할을 하는 클래스를 등장시킬 차례이다. -> 싱글톤 컨테이너의 등장
     */

    /* 언제나 static 키워드는 T메모리 구조상에서, static 영역에 해당하므로 코드가 클래스
    내부에 존재하더라도, 인스턴스의 생성여부와 상관없이 자바 머신의 시작과 동시에 메모리에 적재됨을
    알아두자.
     */

    //2. public 으로 열어서 객체 인스턴스가 필요하면 이 static 메서드를 통해서만 조회하도록 허용한다.
    public static SingletonService getInstance(){
        return instance;
    }

    private SingletonService() {
    }

    public void logic() {
        System.out.println("싱글톤 객체 로직 호출");
    }


}
