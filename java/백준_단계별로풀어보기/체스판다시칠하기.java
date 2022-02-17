/*
체스판은 검은색과 흰색이 번갈아서 칠해져야함.
MxN 크기의 보드를 8x8 크기로 잘라 만듬.
두 가지 경우, 하나는 맨왼쪽 위칸이 흰색인 경우, 하나는 검은색인 경우
지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램 작성
8 <= N, M <= 50
N개의 줄에 보드의 각 행의 상태, B = 검은색, W = 흰색
 */
package 단계별로풀어보기.입출력과사칙연산;

import java.io.*;
public class 체스판다시칠하기 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // n,m 입력
        String[] str = br.readLine().split(" ");
        int n = Integer.parseInt(str[0]);
        int m = Integer.parseInt(str[1]);

        // 보드 색칠 정보 입력
        String[][] board = new String[n][m];
        for (int i = 0; i<n; i++){
            board[i] = br.readLine().split("");
        }
        // 8x8으로 잘라가면서 가장 최소로 색깔을 바꿔도 되는 경우 출력
        int temp = 65; // 바꾸는 값 중 가장 큰 경우
        for (int i = 0; i<n-7; i++){ // 8개를 자를 수 있는 최대치까지 반복. ( 시작 로우 )
            for (int j = 0; j<m-7; j++){ // 8개를 자를 수 있는 최대치까지 반복. ( 시작 콜론 )
                int count = 0;
                int index = 1;
                for ( int row = i; row<i+8; row++){
                    index -= 1; // 다음 행으로 넘어갈때 다른 패턴을 주기 위함.
                    for ( int col = j; col < j+8; col++){
                        if ( index%2==0 && board[row][col].equals("B")) // 짝순데 W가 아닌 경우
                            count += 1;
                        if ( index%2!=0 && board[row][col].equals("W")) // 홀순데 B가 아닌 경우
                            count += 1;
                        index+=1;
                    }
                }
                if (temp > count)
                    temp = count;
                count = 0;
                index = 1;
                for ( int row = i; row<i+8; row++){
                    index -= 1; // 다음 행으로 넘어갈때 다른 패턴을 주기 위함.
                    for ( int col = j; col < j+8; col++){
                        if ( index%2==0 && board[row][col].equals("W")) // 짝순데 B가 아닌 경우
                            count += 1;
                        if ( index%2!=0 && board[row][col].equals("B")) // 홀순데 W가 아닌 경우
                            count += 1;
                        index+=1;
                    }
                }
                if (temp > count)
                    temp = count;
            }
        }
        System.out.println(temp);
    }
}
// 시간이 165ms 정도 걸렸는데
// 50*50*(50*50 + 50*50) 정도의 복잡도여서
// 대략 나누기 10000 정도 한 ms라고 생각하면 될꺼같다.
