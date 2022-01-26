import javax.swing.*;
import java.awt.*;
public class test2 extends JFrame{
    test2(){
        setTitle("나의 첫번째 구이");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        //setSize(600, 500);

        Container cp = getContentPane();
        //cp.setLayout(new FlowLayout());

        cp.add(new ToolPanel());
        cp.add(new DrawPanel());
// 패널 2개 선언 크기 100,500, 빨, 그리드로 3개의 위젯(버튼, 레이블, 텍스트 필드 ) / 500,500, 노
        cp.setPreferredSize(new Dimension(600,500));
        pack();
        setResizable(false);
        setVisible(true);
    }

    class ToolPanel extends JPanel{
        ToolPanel() {
            setBackground(Color.red);
            setSize(100, 500);
            setLayout(new GridLayout(3,1));
            add(new JButton("버튼입니다."));
            add(new JLabel(new ImageIcon("C:/Users/LeeSuyoung/IdeaProjects/SuyoungLee/src/img.jpg")));
            add(new JTextField(10));
        }
    }
    class DrawPanel extends JPanel{
        DrawPanel() {
            setBackground(Color.yellow);
            setSize(500, 500);
        }
    }
    public static void main(String[] args){
        new test2();
    }
}


