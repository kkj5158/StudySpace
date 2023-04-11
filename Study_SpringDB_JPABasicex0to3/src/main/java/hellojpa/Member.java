package hellojpa;

import javax.persistence.*;
import javax.xml.bind.annotation.XmlInlineBinaryData;
import java.util.Date;


@Entity
@Table(name="MEMBER", uniqueConstraints = {@UniqueConstraint(name = "NAME_AGE_UNIQUE", columnNames = {"NAME", "AGE"})})
public class Member {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "ID")
    private Long id;

    @Column(name="NAME", nullable = false, length = 10)
    private String username;

    //매핑 정보가 없는 필드
    private Integer age;

    @Enumerated(EnumType.STRING)
    private  RoleType roleType;

    @Temporal(TemporalType.TIMESTAMP)
    private  Date createdDate;

    @Temporal(TemporalType.TIMESTAMP)
    private Date lastModifiedDate;

    @Lob
    private String description;


    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getUserName() {
        return username;
    }

    public void setUserName(String name) {
        this.username = name;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }
}
