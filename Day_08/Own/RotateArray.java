import java.util.Arrays;

public class RotateArray

{
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5, 6, 7 };
        int d = 2;
        int[] ansArr = new int[arr.length];
        // arr.length - d = 4
        // copy elements from 3,4,5,6,7
        // then, copy all elements from 0 to d.
        for (int i = 0; i < arr.length; i++) {
            if (i < d) {
                continue;
            }
            ansArr[i - d] = arr[i];
        }
        for (int i = 0; i < d; i++) {
            ansArr[(arr.length - d) + i] = arr[i];
        }
        System.out.println(Arrays.toString(ansArr));
    }
}
