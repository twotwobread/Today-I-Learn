// file name : lab6_1.java
// Employee class와 이를 상속받는 Manager class를 구현하고 
// 이를 통해 사원들의 정보를 출력하는 프로그램
// author : Lee Suyoung (2022-01-22)
class Employee{
    protected String name; // 이름
    private  int salary; // 봉급
    protected String ID; // 사번

    // constructor
    Employee(){ this("", 0, ""); }
    Employee(String name, int salary, String ID){
        this.name = name;
        this.salary = salary;
        this.ID = ID;
    }
    //accessors
    void setName(String name){ this.name = name; }
    void setSalary(int salary){ this.salary = salary; }
    void setID(String ID){ this.ID = ID; }
    // mutators
    int getSalary(){ return salary; }
    String getName(){ return name; }
    String getID(){ return ID; }

    // overriding
    public String toString(){
        return "["+this.getClass().getSimpleName()+"] "+name+"( "+ID+" ) : salary = "+salary+"\n";
    }
}
class Manager extends Employee{
    private String department; // 책임부서이름

    // constructor
    Manager() { this("", 0, "", ""); }
    Manager(String name, int salary, String ID, String department){
        super(name, salary, ID);
        this.department = department;
    }
    //accessors
    void setDepartment(String department){ this.department = department; }
    //mutators
    String getDepartment(){ return this.department; }

    //overriding
    public String toString(){
        return "["+this.getClass().getSimpleName()+"] "+name+"( "+ID+" ) : salary = "+super.getSalary()+", salary = "+this.getSalary()+"\t department = "+department+"\n";
    }
}
public class lab6_1 {
    Employee e1, e2, e3;
    Manager m1, m2, m3;
    // 생성자 및 메소드를 구현하여 코드가 훨씬 깔끔하고 보기편하고
    // main문의 코드가 최대한 줄어든 모습이다.
    public lab6_1(){
        e1 = new Employee("아이유", 3000000, "kd039482");
        e2 = new Employee("김건모", 3500000, "ek039482");
        e3 = new Employee();
        m1 = new Manager("에일리", 7000000, "lg837593", "인사부");
        m2 = new Manager("서태지", 6000000, "je837593", "관리부");
        m3 = new Manager();
    }
    public void showInfo(){
        String info = "사원 정보 (직급, 이름, 사번, 월급, 관리부서)";
        info += "\n=======================================================\n";
        info += e1+"\n"+e2+"\n"+e3+"\n"+m1+"\n"+m2+"\n"+m3;
        System.out.println(info);
    }
    public static void main(String[] argv){
        lab6_1 l = new lab6_1();
        l.showInfo();
        System.exit(0);
    }
}
