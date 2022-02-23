package 단계별로풀어보기.입출력과사칙연산;

import java.util.Scanner;
public class 소트인사이드 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        String num = sc.next();
        String[] oneNum = num.split("");

        quickSort(oneNum, 0, oneNum.length-1);
        for (int i = 0; i<oneNum.length; i++)
            System.out.print(oneNum[i]);
        return;
    }

    public static void quickSort(String[] array, int start, int end){
        if (start >= end)
            return;
        int pivot = (start + end)/2;

        int newPivot = start;
        int pivotValue = Integer.parseInt(array[pivot]);

        String temp = array[pivot];
        array[pivot] = array[end];
        array[end] = temp;
        for (int i = start; i<end; i++){
            if (pivotValue < Integer.parseInt(array[i])){
                temp = array[i];
                array[i] = array[newPivot];
                array[newPivot++] = temp;
            }
        }
        temp = array[end];
        array[end] = array[newPivot];
        array[newPivot] = temp;

        quickSort(array, start, newPivot-1);
        quickSort(array, newPivot+1, end);
        return;
    }
}
