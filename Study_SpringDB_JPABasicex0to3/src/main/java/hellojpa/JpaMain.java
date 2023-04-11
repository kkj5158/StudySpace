package hellojpa;

import javax.persistence.*;
import java.util.List;

public class JpaMain {

    public static void main(String[] args) {
        //
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("jpabook");

        EntityManager em = emf.createEntityManager();

        EntityTransaction  tx = em.getTransaction();

        try {
            tx.begin();
            logic(em);
            tx.commit();

        }catch (Exception e){
            tx.rollback();
        }finally {
            em.close();
        }
        emf.close();

    }

    // 비즈니스 로직
    private static void logic(EntityManager em) {

        Member member3 = new Member();
        Member member4 = new Member();


        member3.setUserName("kim22");
        member3.setAge(232);

        member4.setUserName("lee22");
        member4.setAge(322);


        em.persist(member3);
        em.persist(member4);





    }
}
