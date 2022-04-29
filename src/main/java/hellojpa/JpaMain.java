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

        // 멤버 등록

        String id = "id1";
        Member member = new Member();

        member.setId(id);
        member.setUserName("지한");
        member.setAge(2);

        em.persist(member);

        // 수정
        member.setAge(20);

        // 한건 조회

        Member findMember = em.find(Member.class, id);
        System.out.println("findMember =" + findMember.getUserName() + ", age" + findMember.getAge());

        // 목록 조회

        List<Member> members = em.createQuery("select m from Member m", Member.class).getResultList();

        System.out.println("member.size =" + members.size());

        // 멤버 삭제

        //em.remove(member);


    }
}
