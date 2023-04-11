package hello.core.testApp;


import hello.core.AppConfig;
import hello.core.Order.Order;
import hello.core.Order.OrderService;
import hello.core.Order.OrderServiceImpl;
import hello.core.member.*;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

/*
테스트 앱 없이 테스트 진행하기
*/

public class OrderApp {

    public static void main(String[] args) {

        //given
       // AppConfig appconfig = new AppConfig();
        //MemberService memberService = appconfig.memberService();
        // OrderService orderService = appconfig.orderService();

        ApplicationContext applicationContext = new
                AnnotationConfigApplicationContext(AppConfig.class);

        MemberService memberService =
                applicationContext.getBean("memberService", MemberService.class);

        OrderService orderService = applicationContext.getBean("orderService",
                OrderService.class);

        long memberId = 1L;

        Member member = new Member(memberId, "KJS" , Grade.VIP);

        // when

        memberService.join(member);

        int exdiscountprice = 1000;

        Order order = orderService.createOrder(1L, "apple", 10000);

        // then

       System.out.println("order = " + order);


    }




}
