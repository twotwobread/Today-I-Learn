import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// n 입력
		int n = sc.nextInt();	
		// n개의 원소 입력
		int[] array = new int[n];
		for (int i = 0; i<n; i++){
            array[i] = sc.nextInt();
        }
        // 퀵 소팅 
        quickSort(array, 0, array.length-1);
        for (int i = 0; i<n; i++){
            System.out.println(array[i]);
        }
    }
    public static int NewPivot(int[] array, int start, int end, int pivot){
        int pivotValue = array[pivot];
        int temp = array[pivot];
        array[pivot] = array[end];
        array[end] = temp;
        int newPivot = start;
        for (int i = start; i<end; i++){
            if (pivotValue > array[i]){
                temp = array[i];
                array[i] = array[newPivot];
                array[newPivot] = temp;
                newPivot++;
            }
        }

        temp = array[newPivot];
        array[newPivot] = array[end];
        array[end] = temp;

        return newPivot;
    }
    public static void quickSort(int[] array, int start, int end){
        if (start >= end)
            return;
        int pivot = (end+start)/2;
        int newPivot = NewPivot(array, start, end, pivot);

        quickSort(array, start, newPivot-1);
        quickSort(array, newPivot+1, end);
        return;
    }
}
			
