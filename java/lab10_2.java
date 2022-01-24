// file name : lab10_2.java
// ArrayList를 활용한 프로그램.
// 파일로부터 학생 정보를 받아와서 학생 정보를 출력하고
// 최고점 학생의 정보를 출력하라.
// author : Lee Suyoung ( 2022-01-24 )
package lab10;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.sql.Struct;
import java.util.ArrayList;
import java.util.Vector;

public class lab10_2 {
    Student findMax(ArrayList<lab10_2.Student> v){
        Student result = v.get(0);
        for(int i = 1; i<v.size(); i++){
            if(result.getScore() < v.get(i).getScore())
                result = v.get(i);
        }
        return result;
    }
    class Student {
        private int ID;
        private String name;
        private int score;

        // Constructors
        Student(){ this(0, "", 0); }
        Student(int ID, String name, int score){
            this.ID = ID;
            this.name = name;
            this.score = score;
        }

        //mutators
        void setID(int ID){ this.ID = ID; }
        void setName(String name){ this.name = name; }
        void setScore(int score){ this.score = score; }
        //accessors
        int getID(){ return ID; }
        String getName(){ return name; }
        int getScore(){ return score; }
        public String toString(){
            return name+"( "+ID+" ) -> 점수 = "+score+"\n";
        }
    }
    public static void main(String[] args){
        lab10_2 l = new lab10_2();
        FileReader fin;
        BufferedReader bin;
        try{
            ArrayList <Student> st_array = new ArrayList<Student>(6);
            String temp;
            String[] str_array = new String[3];
            Student s;
            fin = new FileReader("C:/Users/LeeSuyoung/IdeaProjects/SuyoungLee/data.txt");
            bin = new BufferedReader(fin);

            while ((temp=bin.readLine()) != null){
                str_array = temp.split(",");
                s = l.new Student(Integer.parseInt(str_array[0].trim()), str_array[1].trim(), Integer.parseInt(str_array[2].trim()));
                st_array.add(s);
            }
            System.out.println("파일로부터 입력받은 학생 정보 : ");
            for(int i = 0; i<st_array.size(); i++)
                System.out.print(st_array.get(i));

            Student max_student = l.findMax(st_array);
            System.out.println("\n최고점을 받은 학생 정보 : ");
            System.out.print(max_student);
        }
        catch (FileNotFoundException e){
            System.out.println("ERROR : I CAN'T FIND FILE!!!!!!");
        } catch (IOException e2){

        }
    }
}
