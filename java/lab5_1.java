// file name : lab5_1.java
// 학생 정보를 관리하는 프로그램을 구현
// 각 학생을 나타내는 Student 클래스는 다음 페이지에 기술된 멤버를 갖는다.
// Student 클래스의 필드 중 studentID는 생성자에서 값을 할당한다.
// author : Lee suyoung ( 2022-01-20 )
package lab5;

public class lab5_1 {
    class Student{
        private static int staticID = 2017000;
        private int studentID;
        private String studentName;
        private double midScore, finalScore;

        public Student(){this("",0,0);}
        public Student(String studentName, double midScore, double finalScore){
            this.studentName = studentName;
            this.midScore = midScore;
            this.finalScore = finalScore;
            studentID = staticID;
            staticID += 1;
        }

        void setStudentName(String studentName){this.studentName = studentName;}
        void setMidScore(double midScore){this.midScore = midScore;}
        void setFinalScore(double finalScore){this.finalScore = finalScore;}
        String getStudentName(){return studentName;}
        double getMidScore(){return midScore;}
        double getFinalScore(){return finalScore;}
        public double getAvgScore(){ return (midScore+finalScore)/2; }

        public String toString(){
            return studentName+"( "+studentID+" ) : "+ midScore+", "+finalScore+", "+getAvgScore();
        }
        static Student findBestStudent(Student[] st){
            lab5_1 l = new lab5_1();
            Student s_max = l.new Student();
            Student temp = l.new Student();
            s_max = st[0];
            for(int i = 1; i<st.length; i++){
                if(s_max.getAvgScore() < st[i].getAvgScore())
                    s_max = st[i];
            }
            return s_max;
        }
        static Student findWorstStudent(Student[] st){
            lab5_1 l = new lab5_1();
            Student s_min = l.new Student();
            Student temp = l.new Student();
            s_min = st[0];
            for(int i = 1; i<st.length; i++){
                if(s_min.getAvgScore() > st[i].getAvgScore())
                    s_min = st[i];
            }
            return s_min;
        }
    }
    public static void main(String[] args){
        lab5_1 l = new lab5_1();
        Student[] st = new Student[3];

        st[0] = l.new Student("1", 57.8, 79.5);
        st[1] = l.new Student("2", 67.8, 89.5);
        st[2] = l.new Student("3", 77.8, 99.5);

        System.out.println("------ Student LIST ((StudentID) Name, MidScore, FinalScore, AvgScore ------");
        for(int i = 0; i<3; i++){
            System.out.println(st[i]);
        }

        System.out.println();

        System.out.println("The best student : "+Student.findBestStudent(st));
        System.out.println("The worst student : "+Student.findWorstStudent(st));
    }
}


