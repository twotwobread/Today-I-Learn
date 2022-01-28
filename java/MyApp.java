// file name : MyApp.java
// 원하는 도형을 그리는 GUI 프로그램.
// 현재 왼쪽 상단에서 오른쪽 하단으로 마우스를 눌렀다가 떼는 만큼의 크기의 도형을 그린다.
// 다른 경우의 예외는 생각하지 않은 간단한 프로그램.
// author : Lee Suyoungj (2022-01-27)
// last updated : (2022-01-28) 원래 마우스 이벤트를 버튼 클래스 내부에 addActionListener에서 선언하여 기다렸으나
//                             DrawPanel에서 기다리게 만듬.

package gui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

public class MyApp extends JFrame {
    FunctionPanel functionPanel;
    DrawPanel drawPanel;
    DrawButton presentBtn = null; // addActionLister나 addMouseListener에서 버튼 객체를 컨트롤하기 위함.
    ArrayList<Shape> arrayList = new ArrayList<Shape>();
    DrawButton beforeBtn=null; // 버튼을 누르면 색을 주고 다른 버튼이 눌렸을 경우 이전 버튼의 색을 돌리기 위함.

    MyApp(){ // Frame 관련 생성자
        setTitle("My First GUI App");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(600, 600);

        Container cp = getContentPane(); // 컨테이너 타입으로 업캐스팅
        functionPanel = new FunctionPanel();
        drawPanel = new DrawPanel();
        cp.add(functionPanel); // 기능 패널 추가
        cp.add(drawPanel); // 그림판 패널 추가

        setResizable(false);
    }
    class FunctionPanel extends JPanel{ // 기능 패널을 위한 사용자 정의 클래스
        FunctionPanel(){
            setBounds(0,0,100,600);
            setLayout(new GridLayout(3,1));
            //setBackground(Color.red);
            DrawButton cirBtn = new DrawButton("원"); // 원을 그리는 버튼
            DrawButton lineBtn = new DrawButton("라인"); // 라인을 그리는 버튼
            DrawButton rectBtn = new DrawButton("사각형"); // 사각형을 그리는 버튼

            add(lineBtn);
            add(cirBtn);
            add(rectBtn);
        }
    }

    class DrawPanel extends JPanel { // 그림판 패널을 위한 사용자 정의 클래스
        DrawPanel() {
            setBounds(100,0,500,600);
            setBackground(Color.white);
            addMouseListener(new MouseAdapter() { // 오른쪽 그림판 패널에서의 마우스 이벤트가 발생할때
                Point start, end;

                @Override
                public void mousePressed(MouseEvent e) { // 마우스가 눌려질떄
                    start = e.getPoint();
                }

                @Override
                public void mouseReleased(MouseEvent e) { // 마우스가 떼질때
                    try { // NullPointerException이 발생할 수 있기에 해당 예외발생 하면 버튼이 선택되지 않았다고 알림.
                        end = e.getPoint();
                        //System.out.println(selfObject);
                        System.out.println(presentBtn.getShape());
                        String shape = presentBtn.getShape();
                        if (shape == "원") { // 원이 눌렸다면
                            Circle circle = new Circle(start, end);
                            //System.out.println("원");
                            arrayList.add(circle);
                        } else if (shape == "사각형") { // 사각형이 눌렸다면
                            Rectangle rectangle = new Rectangle(start, end);
                            //System.out.println("사각형");
                            arrayList.add(rectangle);
                        } else if (shape == "라인") { // 라인이 눌렸다면
                            Line line = new Line(start, end);
                            //System.out.println("라인");
                            arrayList.add(line);
                        } // 각각의 형태에 해당하는 클래스 객체를 만들어서 arrayList에 저장한다.
                    } catch (NullPointerException nullPointerException){
                        System.out.println("버튼이 선택되지 않았습니다.");
                    }
                    paintComponent(getGraphics()); // arrayList에 들어있는 객체를 차례대로 출력함
                }
            });
        }

        public void paintComponent(Graphics g){ // 컴포넌트를 그리기 위한 함수
            super.paintComponent(g);
            functionPanel.paintComponents(functionPanel.getGraphics());
            for(int i = 0; i<arrayList.size(); i++){
                arrayList.get(i).draw(g);
            }
        }
    }

    class DrawButton extends JButton{ // 도형을 그리는 버튼을 위한 사용자 정의 클래스
        private String shape; // 어떤 도형을 위한 버튼
        DrawButton selfObject;

        DrawButton(){ this(""); }
        DrawButton(String shape){
            super(shape);
            this.shape = shape;
            selfObject = this;

            addActionListener(new ActionListener() { // 버튼 클릭을 기다리기 위함.
                
                @Override
                public void actionPerformed(ActionEvent e) { // 버튼이 클릭 되었을 때, 동작
                    System.out.println(shape);
                    if(beforeBtn==null){ // 처음 버튼이 눌렸을때, 빨간색으로 바꿈.
                        setBackground(Color.red);
                        presentBtn = selfObject;
                        beforeBtn = selfObject;
                    }
                    else{ // 이전 눌렸던 버튼이 있는경우, 이전 버튼의 색을 흰색으로 돌리고 현재 버튼을 빨갛게 바꿈.
                        beforeBtn.setBackground(Color.white);
                        setBackground(Color.red);
                        presentBtn = selfObject;
                        beforeBtn = selfObject;
                    }
                }
            });
        }
        String getShape() { return this.shape; }
    }
    public static void main(String[] args){
        new MyApp().setVisible(true); // 객체를 만들면 GUI에 관련된 스레드가 따로 생성되기때문에 레퍼런스 변수로 받을 필요가 없다.
    }
}

abstract class Shape{ // 추상 클래스 선언 -> 상속하기 위함.
    private Point start;
    private Point end;

    Shape(Point start, Point end){
        this.start = start;
        this.end = end;
    }

    void setStart(Point start){ this.start=start; }
    void setEnd(Point end){ this.end=end; }
    Point getStart(){ return start; }
    Point getEnd(){ return end; }

    abstract void draw(Graphics g); // 추상 메소드 상속받는 클래스에서 무조건 오버라이딩 하기 위함.
}

// Shape를 상속받은 도형 클래스들.
class Circle extends Shape{
    Circle(Point start, Point end) {
        super(start, end);
    }

    @Override
    void draw(Graphics g) {
        g.drawOval(getStart().x, getStart().y, getEnd().x- getStart().x, getEnd().y- getStart().y);
    }
}
class Rectangle extends Shape{
    Rectangle(Point start, Point end) {
        super(start, end);
    }

    @Override
    void draw(Graphics g) {
        g.drawRect(getStart().x, getStart().y, getEnd().x- getStart().x, getEnd().y- getStart().y);
    }
}
class Line extends Shape{
    Line(Point start, Point end) {
        super(start, end);
    }

    @Override
    void draw(Graphics g) {
        g.drawLine(getStart().x, getStart().y, getEnd().x, getEnd().y);
    }
}
