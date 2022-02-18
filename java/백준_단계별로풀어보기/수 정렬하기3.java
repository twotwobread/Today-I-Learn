import java.util.Scanner;

class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] array = new int[10001];
        for(int i=0; i<n; i++){
            int num = sc.nextInt();
            array[num] += 1;
        }
        for(int j=1; j<n+1; j++){
            if (array[j] == 0)
                continue;
            for(int i = 0; i<array[j]; i++){
                System.out.println(j);
            }
        }
    }
}
