package 단계별로풀어보기.입출력과사칙연산;

import java.io.*;

/*
버퍼리더, 버퍼라이터를 이용해서 한줄씩 출력하는 것을 이용함.
그리고 가장 작은 단위에서 출력을 할때 5번째에서 빈칸이 출력되는 것을
이용했고 size = n/3을 이용해서 단위가 달라질 수 있게 만들었음.
그리고 빈칸의 부분에서 반복문을 이용해서 빈카을 저장하도록 했음.
 */

public class 별찍기 {
    static char[][] arr;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());

        arr = new char[n][n];
        DrawStar(0, 0, n, false);
        for(int i=0; i<n; i++){
            bw.write(arr[i]);
            bw.write("\n");
        }
        bw.flush();
        bw.close();
    }
    public static void DrawStar(int x, int y, int n, boolean blank){
        if (blank){
            for(int i=x; i<x+n; i++){
                for(int j=y; j<y+n; j++){
                    arr[i][j] = ' ';
                }
            }
            return;
        }
        if (n==1){
            arr[x][y] = '*';
            return;
        }

        int size = n/3;
        int count = 0;
        for(int i = x; i<x+n; i+=size){
            for (int j=y; j<y+n; j+=size){
                count++;
                if(count==5){
                    DrawStar(i, j, size, true);
                }
                else{
                    DrawStar(i,j,size,false);
                }
            }
        }
    }
}
