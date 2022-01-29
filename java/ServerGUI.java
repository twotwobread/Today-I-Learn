package Server;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Vector;

public class ServerGUI extends JFrame{ // 클라이언트 프로그램 GUI
    /* 각 패널들에 대한 필드 */
    InfoIP infoIP;
    PrintMessage printMessage;
    InputMessage inputMessage;
    /* 버튼이 눌렸을 때 스트링 입력값을 얻기 위한 필드 */
    JTextField jTextField;
    JButton jButton;
    /* socket 통신을 통핸 메세지를 관리하기 위한 필드 */
    Vector<Server.MessageType> messageTypeVector = new Vector<Server.MessageType>(); // 보내고 받은 메세지를 담기 위한 필드
    BufferedReader in;
    BufferedWriter out;
    Socket socket = null;

    ServerGUI() throws IOException { // 프레임 설정하기 위한 Constructor
        setTitle("Server GUI Program");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(300, 500);

        Container cp = getContentPane();
        cp.setLayout(new BorderLayout());

        infoIP = new InfoIP();
        printMessage = new PrintMessage();
        inputMessage = new InputMessage();

        cp.add(infoIP, BorderLayout.NORTH);
        cp.add(printMessage, BorderLayout.CENTER);
        cp.add(inputMessage, BorderLayout.SOUTH);

        new Server();// 서버 구동
        setResizable(false);
    }

    /* IP 정보 출력하는 패널에 관한 클래스들 */
    class InfoIP extends JPanel{ // 연결할 서버 IP와 자신의 IP 정보를 출력하기 위한 패널
        InfoIP(){
            setBounds(0,0,300, 100);
            setBackground(Color.red);

        }
    }

    /* Message 출력하는 패널에 관한 클래스들 */
    class PrintMessage extends JPanel{ // 보내고 받은 메세지를 출력하기 위한 패널
        PrintText jLabel;
        PrintMessage(){
            setBounds(0,100, 300, 300);
            setBackground(Color.yellow);

            jLabel = new PrintText();
            add(jLabel);
        }
        class PrintText extends JLabel{
            @Override
            public void paintComponents(Graphics g) {
                super.paintComponents(g);
                if(socket == null)
                    g.drawString("클라이언트 대기중 ,,,,,", 10, 10);

                for(int i=0; i<messageTypeVector.size(); i++){
                    if(messageTypeVector.get(i).getType()=='s') // 보낸 문자열과 받은 문자열을 다르게 출력하기 위함.
                        g.drawString(messageTypeVector.get(i).getTxt(), 20*(i+1), 10*(i+1));
                    else
                        g.drawString(messageTypeVector.get(i).getTxt(), 10*(i+1), 10*(i+1));
                }
            }
        }
        @Override
        public void paintComponents(Graphics g) {
            super.paintComponents(g);
            inputMessage.paintComponents(inputMessage.getGraphics());
            infoIP.paintComponents(infoIP.getGraphics());
            jLabel.paintComponents(jLabel.getGraphics());
        }
    }

    /* Input하는 패널에 관한 클래스들 */
    class InputMessage extends JPanel{ // 보낼 메세지를 입력할 부분
        InputMessage(){
            setBounds(0,400, 300, 200);
            setBackground(Color.BLUE);
            setLayout(new BorderLayout());

            JLabel label = new JLabel("입력창");
            label.setHorizontalAlignment(SwingConstants.CENTER);
            label.setVerticalAlignment(SwingConstants.CENTER);

            jTextField = new InputTextField();
            jButton = new JButton("Send");

            this.add(jTextField, BorderLayout.CENTER);
            this.add(label, BorderLayout.NORTH);
            this.add(jButton, BorderLayout.SOUTH);
        }
    }
    class InputTextField extends JTextField implements ActionListener{

        @Override
        public void actionPerformed(ActionEvent e) {
            if(e.getSource()==jButton){
                try {
                    String msg = jTextField.getText();
                    out.write(jTextField.getText()+'\n');
                    out.flush();

                    Server.MessageType messageType = new Server.MessageType(msg, 's');
                    setText("");
                    messageTypeVector.add(messageType);

                    paintComponents(printMessage.getGraphics());
                } catch (IOException ex) {
                    ex.printStackTrace();
                }
            }
        }
    }

    /* Socket을 위한 Server의 구동부 */
    class Server {
        Server() {
            try {
                ServerSocket serverSocket = new ServerSocket(50000);
                System.out.println("클라이언트 대기중 ,,,,");
                socket = serverSocket.accept();
                System.out.println("클라이언트 연결성공 !!!!");

                in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                out = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));

                RecvThread recvThread = new RecvThread();
                recvThread.start();

                out.write("날라가유\n");
                out.flush();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }


        static class MessageType{ // message가 받은 메세지인지 보낸 메세지인지도 확인하기 위한 클래스
            private String txt;
            private char type; // s = send, r = read

            MessageType(String txt, char type){
                this.txt = txt;
                this.type = type;
            }

            String getTxt(){ return txt; }
            char getType(){ return type; }
        }

        class RecvThread extends Thread{

            @Override
            public void run() {
                while (true) {
                    try {
                        String message = in.readLine();
                        if ( message == "EXIT") {
                            System.out.println("상대방이 채팅방을 나갔습니다.");
                            break;
                        }
                        else{
                            System.out.println(message);
                            MessageType msg = new MessageType(message, 'r');
                            messageTypeVector.add(msg);
                            paintComponents(printMessage.getGraphics());
                        }
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        new ServerGUI().setVisible(true);
    }
}
