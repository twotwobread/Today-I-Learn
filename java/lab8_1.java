// file name : lab8_1.java
// 추상 클래스를 만들어 두 클래스에서 반복적으로 사용되는 메소드, 필드를 정의를 하고 
// 삼각형, 사각형 클래스에서 상속을 받아 오버라이딩한다. 그리고 원하는 위치에 그리는 drawAt과 해당 도형을 그리는 drawHere
// 이용하여 도형을 그린다.
// author : Lee Suyoung ( 2022-01-23 )

abstract class Figure{
    private String figureName;

    Figure() { this(""); }
    Figure(String figureName){
        this.figureName = figureName;
    }

    public String getFigureName(){ return this.figureName; }

    abstract public void drawAt(int offset_x, int offset_y);
    abstract public void drawHere(int offset_x);
}
class Rectangle extends Figure{
    private int width;
    private int height;

    Rectangle(){ this("", 0, 0); }
    Rectangle(String figureName, int width, int height){
        super(figureName);
        this.width = width;
        this.height = height;
    }

    int getWidth(){ return this.width; }
    int getHeight(){ return this.height; }

    @Override
    public void drawHere(int offset_x) {
        for(int i = 0; i<height; i++) {
            for(int j = 0; j<offset_x; j++){
                System.out.print(" ");
            }
            for(int k = 0; k<width; k++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
    @Override
    public void drawAt(int offset_x, int offset_y) {
        for(int i = 0; i<offset_y; i++){
            System.out.println(i+1);
        }
        for(int i = 0; i<offset_x; i++){
            System.out.print(i+1);
        }
        System.out.println("<"+super.getFigureName()+">");
        this.drawHere(offset_x);
    }
}

class Triangle extends Figure{
    private int base;

    Triangle() { this("", 0); }
    Triangle(String figureName, int base){
        super(figureName);
        this.base = base;
    }

    @Override
    public void drawHere(int offset_x) {
        for(int i = 0; i<base; i++){
            for(int j = 0; j<offset_x; j++){
                System.out.print(" ");
            }
            for(int k = 0; k<=i; k++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
    @Override
    public void drawAt(int offset_x, int offset_y) {
        for(int i = 0; i<offset_y; i++){
            System.out.println(i+1);
        }
        for(int i = 0; i<offset_x; i++){
            System.out.print(i+1);
        }
        System.out.println("<"+super.getFigureName()+">");
        this.drawHere(offset_x);
    }
}

public class lab8_1 {
    public static void main(String[] argv){
        Figure f;
        Rectangle r = new Rectangle("사각형1", 3, 4);
        f=r;
        f.drawAt(5, 5);
        Triangle t = new Triangle("삼각형2", 5);
        f=t;
        f.drawAt(2,3);
    }
}
