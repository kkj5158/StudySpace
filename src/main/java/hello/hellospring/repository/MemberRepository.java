package hello.hellospring.repository;

import hello.hellospring.controller.domain.Member;

import java.util.List;
import java.util.Optional;

public interface MemberRepository {
    Member save(Member member);
    Optional<Member> findById(Long id);
    Optional<Member> findByNames(String name);
    List<Member> findAll();

    void clearStore();
}
