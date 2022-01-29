package hello.core.testApp;


import hello.core.Order.Order;
import hello.core.Order.OrderServiceImpl;
import hello.core.member.*;

import java.awt.*;

public class OrderApp {

    public static void main(String[] args) {

        //given

        MemberService memberService = new MemberServiceImpl();

        long memberId = 1L;

        Member member = new Member(memberId, "KJS" , Grade.VIP);

        OrderServiceImpl orderService = new OrderServiceImpl();

        // when

        memberService.join(member);

        int exdiscountprice = 1000;

        Order order = orderService.createOrder(1L, "apple", 10000);

        // then

       System.out.println("order = " + order);


    }




}
