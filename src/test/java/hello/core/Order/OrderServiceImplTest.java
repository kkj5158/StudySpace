package hello.core.Order;

import hello.core.member.Grade;
import hello.core.member.Member;
import hello.core.member.MemberService;
import hello.core.member.MemberServiceImpl;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class OrderServiceImplTest {

    //given

    MemberService memberService = new MemberServiceImpl();
    OrderServiceImpl orderService = new OrderServiceImpl();

    @Test
    void createOrder() {

        //given
        long memberId = 1L;

        Member member = new Member(memberId, "KJS" , Grade.VIP);


        //when
        memberService.join(member);

        int exdiscountprice = 1000;

        Order order = orderService.createOrder(1L, "apple", 10000);

        //then

        Assertions.assertThat(order.getDiscountPrice()).isEqualTo(1000);
    }
}