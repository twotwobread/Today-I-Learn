package 단계별로풀어보기.입출력과사칙연산;

import java.util.ArrayList;
import java.util.Scanner;

public class 하노이타워 {
    //public static ArrayList<Move> arr = new ArrayList<Move>();
    public static StringBuilder arr = new StringBuilder();
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        // n 입력
        int n = sc.nextInt();
        int result = hanoiTower(1, n, 1,3,2);
        System.out.println(result);
        System.out.print(arr);
    }
    public static int hanoiTower(int count, int num, int start, int end, int temp){
        if (num == 1){
            arr.append(start+" "+end+"\n");
            return count;
        }
        int sum = hanoiTower(count+1, num-1, start, temp, end);
        arr.append(start+" "+end+"\n");
        sum = hanoiTower(sum+1, num-1, temp, end, start);
        return sum;
    }
    /*
    public static int hanoiTower(int count, int num, int start, int end, int temp){
        if (num == 1){
            arr.add(new Move(start, end));
            return count;
        }
        int sum = hanoiTower(count+1, num-1, start, temp, end);
        arr.add(new Move(start, end));
        sum = hanoiTower(sum+1, num-1, temp, end, start);
        return sum;
    }
    public static class Move{
        int start, end;

        Move(int start, int end){
            this.start = start;
            this.end = end;
        }
        public String toString(){
            return start+" "+end;
        }
    }
    */
}


// class 이용해서 풀었는데 시간초과 발생 -> 출력과정에서 시간초과가 발생하는 것으로 예상.
// String을 이용해서 한줄로 만들 생각.
// StringBuilder를 이용해서 append하여 한줄로 만들고 그대로 출력 -> 시간초과 발생 X
