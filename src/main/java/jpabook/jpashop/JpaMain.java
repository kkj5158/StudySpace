package jpabook.jpashop;

import jpabook.jpashop.domain.Member;
import jpabook.jpashop.domain.Team;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;
import java.util.List;

public class JpaMain {

    // insert 쿼리 안나가는 오류 해결하기 !!

    public static void main(String[] args) {

        //엔티티 매니저 팩토리 생성
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
        // 앤티티 매니저 생성
        EntityManager em = emf.createEntityManager();
        // 트랜잭션 - 획득
        EntityTransaction tx = em.getTransaction();

        businessLogic(em);

        emf.close();



    }

    private static void businessLogic(EntityManager em) {




        /*
        try{

        } catch (Exception e){
        } finally {
        }

         */
    }


}
