// file name : lab4_2.py
// ComplexNumber 클래스를 만들어보고 구현이 잘되었는지 테스트해라.
// author : Lee Suyoung
package lab4;
import java.lang.Math;
import java.util.Scanner;
class ComplexNumber{
    private double realPart, imagPart;

    ComplexNumber(){
        this(0.0,0.0);
    }
    ComplexNumber(double realPart, double imagPart){
        this.realPart = realPart;
        this.imagPart = imagPart;
    }
    void setRealPart(double realPart){
        this.realPart = realPart;
    }
    void setImagPart(double imagPart){
        this.imagPart = imagPart;
    }
    void printNumber(){
        System.out.println("복소수 : "+this.realPart+" "+this.imagPart+" i");
        System.out.println("Magnitude : "+this.magnitude());
    }
    double getRealPart(){
        return this.realPart;
    }
    double getImagPart(){
        return this.imagPart;
    }
    double magnitude(){
        double sum;
        sum = Math.sqrt(Math.pow(this.realPart, 2)+Math.pow(this.imagPart, 2));
        return sum;
    }
    ComplexNumber add(ComplexNumber n) {
        ComplexNumber cn;
        cn = new ComplexNumber();
        cn.realPart = this.realPart + n.realPart;
        cn.imagPart = this.imagPart + n.imagPart;
        return cn;
    }
    ComplexNumber subtract(ComplexNumber n){
        ComplexNumber cn;
        cn = new ComplexNumber();
        cn.realPart = this.realPart - n.realPart;
        cn.imagPart = this.imagPart - n.imagPart;
        return cn;
    }
}
public class lab4_2 {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        String[] str_num = new String[2];
        System.out.print("복소수의 값을 실수, 허수순으로 입력하시오 : ");
        str_num = in.nextLine().split(",");

        double[] num = new double[2];
        num[0] = Double.parseDouble(str_num[0].trim());
        num[1] = Double.parseDouble(str_num[1].trim());

        ComplexNumber cn = new ComplexNumber();
        cn.setRealPart(num[0]);
        cn.setImagPart(num[1]);

        ComplexNumber an = new ComplexNumber(1.0, 2.0);
        an = cn.add(an);
        an.printNumber();
        an = cn.subtract(an);
        an.printNumber();
    }
}
