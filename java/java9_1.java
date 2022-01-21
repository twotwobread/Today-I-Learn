// file name : lab9_1.java
// test.txt 파일로부터 학생 정보를 입력받고 Student 클래스 배열에 담고 ouput.txt 파일에 출력한다.
// 만약, 학생 정보의 score가 0<=score<=100 이 범위에서 벗어난다면 예외 발생.
// author : Lee Suyoung (2022-01-21)
package lab9;

import java.io.*;

public class lab9_1 {
    class Student { // 학생 정보 클래스
        private int ID;
        private String name;
        private int score;

        // 생성자
        Student() {this(0, "", 0);}
        Student(int ID, String name, int score) {this.ID = ID; this.name = name; this.score = score;}
        // accessor
        void setID(int ID) {this.ID = ID;}
        void setName(String name) {this.name = name;}
        void setScore(int score) {this.name = name;}
        // mutator
        int getID() {return ID;}
        String getName() {return name;}
        int getScore() {return score;}
        public String toString() {return name + "'s ID is " + ID + " and his/her score is " + score;}
    }
    class ScoreException extends Exception{ // 학생 스코어의 범위를 위한 예외 ( 0 to 100 )
        public ScoreException(){
            super("this is new Exception");
        }
        public ScoreException(String message){
            super(message);
        }
        public String toString(){
            return "0 to 100 RANGE OVER EXCEPTION !!!!!";
        }
    }
    public static void main(String[] args) throws IOException{
        FileReader fin = null;
        FileWriter fout = null;
        BufferedReader bin = null;

        try{
            lab9_1 l = new lab9_1();
            fin = new FileReader("C:/Users/IT/Desktop/test/test.txt");
            fout = new FileWriter("C:/Users/IT/Desktop/test/output.txt");
            bin = new BufferedReader(fin);
            String line;
            String[] word = new String[3];
            Student[] students = new Student[10];
            int i = 0;
            // test.txt 파일로부터 한줄씩 학생 정보를 읽어와서 해당 정보를 배열에 담고
            // ouput.txt 파일에 출력하는 부분
            while((line=bin.readLine())!=null){
                word = line.split(",");
                int ID = Integer.parseInt(word[0].trim());
                String name = word[1].trim();
                int score = Integer.parseInt(word[2].trim());

                if ((score<0)||(score>100)) throw l.new ScoreException();
                // 위의 조건문으로 예외처리를 하는데 이 예외가 발생할 경우 파일을 닫지 못하는 경우 발생
                // 그 이유가 파일객체변수들이 catch에서 선언이 안되어있어서 였음.
                // 그래서 try 바깥으로 선언부를 빼고 try 안에서 객체를 만드는 부분을 넣었고
                // 그랬을 경우 IOException을 처리하라는 오류 발생
                // throws를 통해서 IOException을 떠넘겨서 오류 발생하지 않음.

                students[i] = l.new Student(ID, name, score);
                System.out.println(students[i]);
                fout.write(students[i].toString());
                fout.write("\n");
                // 파일 출력이 안되는 문제에 직면 밑의 라인으로 확인한 결과 파일을 닫지 않아서 생기는 문제임을 발견
                //bout.close();
                i++;
            }
            bin.close(); fin.close(); fout.close(); // 파일 입출력을 위한 객체들을 닫는 부분.
        } catch (FileNotFoundException e){
            System.out.println("File is NOT FOUND !!!!");
        } catch (IOException e2){
            System.out.println("File is NOT FOUND !!!!");
        } catch (ScoreException e3){
            System.out.println(e3);
        } finally { // 파일 close를 위해 catch를 해도 실행되는 finally 이용
            if (bin!=null){
                bin.close();
            }
            if (fin!=null){
                fin.close();
            }
            if(fout!=null){
                fout.close();
            }
        }
    }
}
