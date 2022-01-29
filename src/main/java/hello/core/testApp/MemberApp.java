package hello.core.testApp;

import hello.core.member.Grade;
import hello.core.member.Member;
import hello.core.member.MemberService;
import hello.core.member.MemberServiceImpl;

public class MemberApp {

    public static void main(String[] args){

        //given

        MemberService memberService = new MemberServiceImpl();
        Member memberA = new Member(1L, "memberA", Grade.VIP);

        //when

        memberService.join(memberA);
        Member findmember = memberService.findMember(1L);

        //then

        System.out.println("new member =" + memberA);
        System.out.println("findMember =" + findmember);

    }
}
