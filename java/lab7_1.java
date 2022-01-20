// file name : lab5_1.java
// 졸업자와 비졸업자를 나누어 관리하는 프로그램
// 각각의 학생의 정보를 입력받은 후 출력하는 
// author : Lee suyoung ( 2022-01-20 )
package lab7;

public class lab7_1 {
    abstract class Student{
        private String name;
        private int id;

        // 생성자
        Student() {
            //    this("", 0);
        }
        Student(String name, int id){
            this.name = name;
            this.id = id;
        }
        //setter
        void setName(String name){
            this.name = name;
        }
        void setId(int id){
            this.id = id;
        }
        //getter
        String getName(){
            return name;
        }
        int getId(){
            return id;
        }
        // toString(출력)
        public String toString(){
            return name+"("+id+")"+" : "+this.getClass().getSimpleName();
        }
        abstract int getAnnualSalary();
    }
    class Undergraduate extends Student{
        private int semesterSalary;

        //생성자
        Undergraduate(){
            this("",0,0);
        }
        Undergraduate(String name, int id, int semesterSalary){
            super(name, id);
            this.semesterSalary = semesterSalary;
        }
        // toString(출력)
        public String toString(){
            return this.getName()+"("+this.getId()+")"+" : "+this.getClass().getSimpleName()+", semester salary : "+semesterSalary+", annual salary : "+getAnnualSalary();
        }
        //연봉 구하는 함수
        int getAnnualSalary(){
            return 2*semesterSalary;
        }
    }
    class Graduate extends Student{
        private int monthSalary;

        //생성자
        Graduate(){
            this("", 0, 0);
        }
        Graduate(String name, int id, int monthSalary){
            super(name, id);
            this.monthSalary = monthSalary;
        }
        // toString 출력함수
        public String toString(){
            return this.getName()+"("+this.getId()+")"+" : "+this.getClass().getSimpleName()+", month salary : "+monthSalary+", annual salary : "+getAnnualSalary();
        }
        //연봉구하는 함수
        int getAnnualSalary(){
            return 12*monthSalary;
        }
    }
    public static void main(String[] args){
        lab7_1 l = new lab7_1();
        Student[] s = new Student[8];

        s[0] = l.new Graduate("Giggs", 20168349, 10);
        s[1] = l.new Graduate("Park", 20168348, 20);
        s[2] = l.new Graduate("Kim", 20168347, 30);

        s[3] = l.new Undergraduate("Gcccc", 20168346, 40);
        s[4] = l.new Undergraduate("Gzzzzz", 20168345, 50);
        s[5] = l.new Undergraduate("Gsssss", 20168344, 60);
        s[6] = l.new Undergraduate("fsesd", 20168343, 70);
        s[7] = l.new Undergraduate("fsesd", 20168342, 80);
        System.out.println("프린트");
        for(int i = 0; i<s.length; i++){
            System.out.println(s[i]);
        }
    }
}
