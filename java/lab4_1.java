// file name : lab4_1.java
// Rectangle 클래스 테스트
// 순차적으로 x1, y1, x2, y2의 좌표를 받고 x1,y1은 왼쪽 하단 x2,y2는 오른쪽 상단의 꼭짓점으로 가정
// 좌표를 입력받았을때 직사각형의 넓이를 구하여라
// author : Lee Suyoung(2022-01-19)
package lab4;

public class lab4_1 {
    class Rectangle{
        private int x1, y1, x2, y2;

        int getX1(){
            return this.x1;
        }
        int getY1(){
            return this.y1;
        }
        int getX2(){
            return this.x2;
        }
        int getY2(){
            return this.y2;
        }
        Rectangle(){
            this(0,0,0,0);
        }
        Rectangle(int x1, int y1, int x2, int y2){
            set(x1,y1,x2,y2);
        }
        void set(int x1, int y1, int x2, int y2){
            this.x1 = x1;
            this.y1 = y1;
            this.x2 = x2;
            this.y2 = y2;
        }
        boolean check(){
            if((x2-x1)>0 && (y2-y1)>0)
                return true;
            else
                return false;
        }
        int getArea(){
            if(check()){
                return (x2-x1)*(y2-y1);
            }
            else
                return 0;
        }
        void show(){
            if(check()){
                System.out.println("4개의 점에 관한 정보 : "+x1+" "+y1+" "+x2+" "+y2+" ");
            }
            else
                System.out.println("직사각형 구성이 불가능하여 출력 불가합니다.");

        }
        boolean equals(Rectangle r){
            if(((x2-x1)==(r.getX2()-r.getX1()))&&((y2-y1)==(r.getY2()-r.getY1())))
                return true;
            else
                return false;
        }
    }
    public static void main(String[] args){
        lab4_1 l = new lab4_1();
        lab4_1.Rectangle r = l.new Rectangle();
        lab4_1.Rectangle s = l.new Rectangle(1, 1, 2, 3);

        r.show();
        s.show();
        System.out.println(s.getArea());
        r.set(2,1,4,5);
        r.show();
        System.out.println(r.getArea());
        if(r.equals(s))
            System.out.println("두 사각형은 같습니다.");
    }
}
