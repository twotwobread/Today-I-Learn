package 단계별로풀어보기.입출력과사칙연산;

// 자바 에디터가 없어서 메모장으로 짠 버전
// 내일 에디터가서 확인 문법적인 부분 확인해봐야할 듯
// 이렇게 메모장으로 문법익히는 것도 좋은 것 같다.
// 맞았다.!!


import java.io.*;
public class 덩치 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        // n 입력
        int n = Integer.parseInt(br.readLine());
        // 덩치 정보 입력
        int[][] bulk = new int[n][2];
        for (int i = 0; i<n; i++){
            //
            String[] str = br.readLine().split(" ");
            bulk[i][0] = Integer.parseInt(str[0]);
            bulk[i][1] = Integer.parseInt(str[1]);
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i<n; i++) {
            int count = 1;
            for (int j = 0; j < n; j++) {
                if (bulk[i][0] < bulk[j][0] && bulk[i][1] < bulk[j][1]) {
                    count += 1;
                }
            }
            sb.append(Integer.toString(count)+" ");
        }
        System.out.println(sb);
    }
}
