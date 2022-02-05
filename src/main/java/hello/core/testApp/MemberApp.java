package hello.core.testApp;

import hello.core.AppConfig;
import hello.core.member.Grade;
import hello.core.member.Member;
import hello.core.member.MemberService;
import hello.core.member.MemberServiceImpl;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

/* 테스트 코드 없이 테스트 진행하기 */

public class MemberApp {

    public static void main(String[] args){

        //given

        /*
        AppConfig appConfig = new AppConfig();
        MemberService memberService = appConfig.memberService();
        */

        ApplicationContext applicationContext = new AnnotationConfigApplicationContext(AppConfig.class);
        // 스프링 컨테이너의 등록 //
        MemberService memberService = applicationContext.getBean("memberService", MemberService.class);

        Member memberA = new Member(1L, "memberA", Grade.VIP);

        //when

        memberService.join(memberA);
        Member findmember = memberService.findMember(1L);

        //then

        System.out.println("new member =" + memberA);
        System.out.println("findMember =" + findmember);

        //

    }
}
